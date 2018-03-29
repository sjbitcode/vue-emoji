#!/usr/bin/env bash

echo -e "-- Building application containers --\n"

# Build docker images from source code.
if [[ $1 = "full" ]] ; then
    docker-compose -f docker-compose-staging.yml build --no-cache
else
    docker-compose -f docker-compose-staging.yml build
fi

# Push docker images to dockerhub registry.
docker-compose push

echo -e "\n-- Application containers have been built and pushed --"
