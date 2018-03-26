# Step 1 - Pull new images
# Step 2 - Stop all containers
# Step 3 - Remove all containers
# Step 4 - Remove web volume
# Step 5 - Start docker-compose service

# dc pull && dc stop -t 1 && dc rm -fv && docker volume rm webdata && docker volume create --name=webdata && dc up -d


echo -e "\nRunning dc stop -t 1..."
docker-compose stop -t 1

echo -e "\nRunning dc rm -fv..."
docker-compose rm -fv

echo -e "\nRunning dc build..."
docker-compose build

echo -e "\nRunning docker volume rm webdata, appstatic..."
docker volume rm webdata

echo -e "\nRunning docker volume create --name=webdata..."
docker volume create --name=webdata
docker volume create --name=appstatic

echo -e "\nRunning dc up -d..."
docker-compose up -d
