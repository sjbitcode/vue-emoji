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
echo -e "-- Copying data @ $HOST --\n"


# Copy db scripts to remote server.
echo -e "\n-- Copying data directory to local filesystem --"
LOCAL_DATA_DIR="$ROOT_PATH"
REMOTE_DATA_DIR="/home/$USER/data"


# Copy the data dir from the remote server.
scp -i $KEY -r $USER@$HOST:$REMOTE_DATA_DIR $LOCAL_DATA_DIR


echo -e "\n-- Data @ $HOST has been copied --"
