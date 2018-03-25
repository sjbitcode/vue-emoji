#!/usr/bin/env bash

USER="deploy"

# Get absolute path of the script.
PARENT_PATH=$( cd "$(dirname "${BASH_SOURCE}")" ; pwd -P )
ROOT_PATH=$( cd "$(dirname "${PARENT_PATH}")" ; pwd -P )


# Check the existence of the env argument.
if [[ $# -eq 0 ]] ; then
    echo "Please specify an env (staging | prod)"
    exit
else
    # Get env argument.
    ENV=$1
    # Build private key location.
    KEY="$PARENT_PATH/keys/$ENV/$ENV"
    echo "  Using private key: $KEY"
fi

# If specified env directory exists, then make
# the same directories on the remote server.
if [ ! -f "$KEY" ]; then
    echo -e "\n\n! Private key: $KEY does not exist !"
    exit 1
fi


# Load HOST config.
source "$PARENT_PATH/hosts/$ENV/host.sh"
echo -e "-- Updating server @ $HOST --\n"


# Copy local docker-compose-prod.yml file to the remote server.
echo -e "\n-- Copying docker-compose-prod.yml to remote server --"
LOCAL_COMPOSE_PROD="$ROOT_PATH/docker-compose-prod.yml"
REMOTE_COMPOSE_PROD="/home/$USER/docker-compose-prod.yml"
scp -i $KEY $LOCAL_COMPOSE_PROD $USER@$HOST:$REMOTE_COMPOSE_PROD


# Copy env files to remote server.
echo -e "\n-- Copying $ENV env files to remote server --"
ENV_FILE="env.$ENV.env"
LOCAL_ENV_FILE="$PARENT_PATH/secrets/$ENV_FILE"
REMOTE_ENV_DIR="/home/$USER/deploy/secrets"


# Make the env directories on the remote server.
ssh -i $KEY $USER@$HOST mkdir -p $REMOTE_ENV_DIR
scp -i $KEY $LOCAL_ENV_FILE $USER@$HOST:"$REMOTE_ENV_DIR/$ENV_FILE"


# Copy db scripts to remote server.
echo -e "\n-- Copying db scripts to remote server --"
DB_SCRIPT="db.py"
LOCAL_DB_SCRIPT="$ROOT_PATH/scripts/$DB_SCRIPT"
REMOTE_SCRIPT_DIR="/home/$USER/scripts"


# Make the script directories on the remote server.
ssh -i $KEY $USER@$HOST mkdir -p $REMOTE_SCRIPT_DIR
scp -i $KEY $LOCAL_DB_SCRIPT $USER@$HOST:"$REMOTE_SCRIPT_DIR/$DB_SCRIPT"



echo -e "\n-- Server @ $HOST has been updated --"
