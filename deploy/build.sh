#!/usr/bin/env bash

# Get absolute path of the script.
PARENT_PATH=$( cd "$(dirname "${BASH_SOURCE}")" ; pwd -P )
ROOT_PATH=$( cd "$(dirname "${PARENT_PATH}")" ; pwd -P )

echo -e "-- Running npm run build \n --"
WEB_DIR="$ROOT_PATH/web"
npm --prefix $WEB_DIR run build

# echo -e "-- Building application containers --\n"

# # Build docker images from source code.
# if [[ $1 = "full" ]] ; then
#     docker-compose -f docker-compose-staging.yml build --no-cache
# else
#     docker-compose -f docker-compose-staging.yml build
# fi

# # Push docker images to dockerhub registry.
# docker-compose push

# echo -e "\n-- Application containers have been built and pushed --"
