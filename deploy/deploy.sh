#!/usr/bin/env bash

USER="deploy"
ENV="prod"

# Get absolute path of the script.
PARENT_PATH=$( cd "$(dirname "${BASH_SOURCE}")" ; pwd -P )
ROOT_PATH=$( cd "$(dirname "${PARENT_PATH}")" ; pwd -P )

# Update envs on remote server.
UPDATE_CMD="$PARENT_PATH/update.sh $ENV"

# Deploy application to remote server.
DEPLOY_CMD="$PARENT_PATH/containers.sh $ENV"

# Build containers with no cache if specified.
if [[ $1 = "full" ]] ; then
    # Build application containers.
    BUILD_CMD="$PARENT_PATH/build.sh full"
    bash $BUILD_CMD
fi

# Build containers if specified.
if [[ $1 = "build" ]] ; then
    # Build application containers.
    BUILD_CMD="$PARENT_PATH/build.sh"
    bash $BUILD_CMD
fi

# Execute commands.
bash $UPDATE_CMD
bash $DEPLOY_CMD
