#!/usr/bin/env bash

# Get absolute path of the script.
PARENT_PATH=$( cd "$(dirname "${BASH_SOURCE}")" ; pwd -P )
ROOT_PATH=$( cd "$(dirname "${PARENT_PATH}")" ; pwd -P )

# Bundle frontend app
echo -e "-- Running npm run build \n --"

WEB_DIR="$ROOT_PATH/web"
npm --prefix $WEB_DIR run build


# Build docker images from source code.
echo -e "-- Building application containers --\n"

if [[ $1 = "full" ]] ; then
    docker-compose -f docker-compose-staging.yml build --no-cache
else
    docker-compose -f docker-compose-staging.yml build
fi

# Push docker images to dockerhub registry.
docker-compose -f docker-compose-staging.yml push

echo -e "\n-- Application containers have been built and pushed --"
