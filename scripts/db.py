#!/usr/bin/env python3

import argparse
import codecs
from collections import OrderedDict
import os
from os.path import abspath, dirname, join
from subprocess import run
import sys


THIS_FILENAME = __file__
DATA_PATH = 'data'
DB_BACKUPS = 'db_backups'


# ----------------------------------------------------------------------------
# Load Env helper functions.
# ----------------------------------------------------------------------------

__escape_decoder = codecs.getdecoder('unicode_escape')


def decode_escaped(escaped):
    return __escape_decoder(escaped)[0]


# https://github.com/theskumar/python-dotenv/blob/master/dotenv/main.py
def parse_dotenv(dotenv_path):
    with open(dotenv_path) as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith('#') or '=' not in line:
                continue
            k, v = line.split('=', 1)

            # Remove any leading and trailing spaces in key, value
            k, v = (
                k.strip(),
                v.strip().encode('unicode-escape').decode('ascii')
            )

            if len(v) > 0:
                quoted = v[0] == v[-1] in ['"', "'"]

                if quoted:
                    v = decode_escaped(v[1:-1])

            yield k, v


# ----------------------------------------------------------------------------
# Display Helper functions.
# ----------------------------------------------------------------------------

# https://stackoverflow.com/a/34443116
def red(x): return '\033[91m{}\033[00m'.format(x)


def cyan(x): return '\033[96m{}\033[00m'.format(x)


def lpurple(x): return '\033[94m{}\033[00m'.format(x)


def yellow(x): return '\033[93m{}\033[00m'.format(x)


def lgrey(x): return '\033[97m{}\033[00m'.format(x)


# ----------------------------------------------------------------------------
# Backup Database functions.
# ----------------------------------------------------------------------------

def backup_database(local_filename, debug=False, production=False):
    '''
    Backup the database.
    '''
    dc_filename = get_docker_compose_filename(production)
    cmd_str = (
        'docker-compose -f {} run --rm -e PGPASSWORD={} postgres '
        'pg_dump -Fc -Ox -h {} -U {} -d {} -f {}'
    ).format(
        dc_filename,
        POSTGRES_PASSWORD,
        POSTGRES_HOST,
        POSTGRES_USER,
        POSTGRES_DB,
        get_db_filename(local_filename)
    )
    cmd = cmd_str.split(' ')
    print(cyan('[back-up] the database with:\n'))
    print(yellow(cmd_str))

    # If debug, then exit.
    if debug:
        print(cyan('\n[debug] exiting...'))
        sys.exit(0)

    if os.path.exists(real_file_path(local_filename)):
        print(red('\n[error] file already exists...'))
        sys.exit(0)

    # Run the command.
    process = run(cmd)
    return process.returncode


# ----------------------------------------------------------------------------
# Backup Database functions.
# ----------------------------------------------------------------------------

def restore_database(local_filename, debug=False, production=False):
    '''
    Backup the database.
    '''
    dc_filename = get_docker_compose_filename(production)
    cmd_str = (
        'docker-compose -f {} run --rm -e PGPASSWORD={} postgres '
        'pg_restore -x --no-owner --single-transaction --clean '
        '-h {} -U {} -d {} {}'
    ).format(
        dc_filename,
        POSTGRES_PASSWORD,
        POSTGRES_HOST,
        POSTGRES_USER,
        POSTGRES_DB,
        get_db_filename(local_filename)
    )
    cmd = cmd_str.split(' ')
    print(cyan('[restore] the database with:\n'))
    print(yellow(cmd_str))

    # If debug, then exit.
    if debug:
        print(cyan('\n[debug] exiting...'))
        sys.exit(0)

    # Run the command.
    process = run(cmd)
    return process.returncode


# ----------------------------------------------------------------------------
# Argparse Helper functions.
# ----------------------------------------------------------------------------

def parse_args():
    parser = argparse.ArgumentParser()

    # Backup the database.
    parser.add_argument(
        '-b',
        '--backup',
        dest='backup',
        action='store_true',
        default=False,
        help='Backup the database.',
    )

    # Restore the database from a backup.
    parser.add_argument(
        '-r',
        '--restore',
        dest='restore',
        action='store_true',
        default=False,
        help='Restore the database from a backup.',
    )

    # The filename to backup to / restore from.
    parser.add_argument(
        'filename',
        nargs='?',
        type=str,
        default='',
        help='The filename to backup to / restore from.',
    )

    # Debug mode. No changes will be made.
    parser.add_argument(
        '-d',
        '--debug',
        dest='debug',
        action='store_true',
        default=False,
        help='Specify Debug mode. No changes will be made.',
    )

    # Production mode.
    # Target production envs and production docker-compose file.
    parser.add_argument(
        '-p',
        '--production',
        dest='production',
        action='store_true',
        default=False,
        help=(
            'Specify Production mode. '
            'Target production envs and production docker-compose file.'
        ),
    )

    return parser.parse_args()


def real_file_path(filename):
    '''
    Get the absolute path for the fileon the local filesystem.
    '''
    return os.path.join(DATA_PATH, DB_BACKUPS, filename)


def get_local_filename(filename):
    '''
    Return the name of file, with paths removed.
    '''
    return filename.split(os.sep)[-1]


def get_db_filename(filename):
    '''
    Build the filename for use within the database container.
    '''
    return os.path.join(POSTGRES_BACKUP_DIR, filename)


def get_env_filename(is_production):
    '''
    Build the env filename.
    '''
    env_filename = 'dev.env'
    if is_production:
        env_filename = 'prod.env'

    return join(
        dirname(dirname(abspath(THIS_FILENAME))),
        'deploy', 'secrets', env_filename
    )


def get_docker_compose_filename(is_production=False):
    '''
    Build the docker compose filename.
    '''
    docker_compose_filename = 'docker-compose.yml'
    if is_production:
        docker_compose_filename = 'docker-compose-prod.yml'

    return docker_compose_filename


def load_envs(debug=False, production=False):
    '''
    Load Postgres configs from an env file.
    '''
    global POSTGRES_PASSWORD
    global POSTGRES_HOST
    global POSTGRES_USER
    global POSTGRES_DB
    global POSTGRES_BACKUP_DIR
    # Read env file.
    env_filename = get_env_filename(production)
    env_vars = OrderedDict(parse_dotenv(env_filename))
    # Load configs.
    POSTGRES_PASSWORD = env_vars['POSTGRES_PASSWORD']
    POSTGRES_HOST = env_vars['POSTGRES_HOST']
    POSTGRES_USER = env_vars['POSTGRES_USER']
    POSTGRES_DB = env_vars['POSTGRES_DB']
    POSTGRES_BACKUP_DIR = env_vars['POSTGRES_BACKUP_DIR']
    # Display configs if debug is specified.
    if not debug:
        return
    print(cyan('[config]\n'))
    print(cyan('POSTGRES_DB: {}'.format(POSTGRES_DB)))
    print(cyan('POSTGRES_USER: {}'.format(POSTGRES_USER)))
    print(cyan('POSTGRES_PASSWORD: {}'.format(POSTGRES_PASSWORD)))
    print(cyan('POSTGRES_HOST: {}'.format(POSTGRES_HOST)))
    print(cyan('POSTGRES_BACKUP_DIR: {}'.format(POSTGRES_BACKUP_DIR)))
    print(cyan('\n[env] {}'.format(env_filename)))
    print('')


# ----------------------------------------------------------------------------
# Entry Point.
# ----------------------------------------------------------------------------

if __name__ == '__main__':
    args = parse_args()
    load_envs(args.debug, args.production)

    # Check that an action (backup, restore) is given.
    if all([
        not args.backup,
        not args.restore,
    ]):
        print(red('Please specify a restore (-r) or backup (-b) action.'))
        sys.exit(1)

    # Check that a filename is given.
    if not args.filename:
        print(red('Please specify a filename to backup to / restore from.'))
        sys.exit(1)

    local_filename = get_local_filename(args.filename)

    if args.backup:
        returncode = backup_database(
            local_filename,
            args.debug,
            args.production
        )

    elif args.restore:
        returncode = restore_database(
            local_filename,
            args.debug,
            args.production
        )

    if returncode == 0:
        print(cyan('\n[done]'))
    else:
        print(red('\n[error]'))
