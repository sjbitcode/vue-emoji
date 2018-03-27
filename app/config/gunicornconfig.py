import os

def env(key):
    return os.environ.get(key, None)

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

bind = '{}:{}'.format(env('HOST'), env('PORT'))
reload = True

LOGS_DIR = os.path.join(os.path.dirname(BASE_DIR), 'logs')
accesslog = os.path.join(LOGS_DIR, env('GUNICORN_ACCESS_LOG'))
errorlog = os.path.join(LOGS_DIR, env('GUNICORN_ERROR_LOG'))
