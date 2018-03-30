# Step 1 - Delete logs directory
# Step 2 - Stop all containers
# Step 3 - Remove all containers
# Step 4 - Build images
# Step 5 - Remove webdata and appstatic volumes
# Step 6 - Start docker-compose service


# Delete logs directory
echo -e "\nDeleting logs directory..."
rm -rf logs

# Stop all containers
echo -e "\nRunning dc stop -t 1..."
docker-compose stop -t 1

# Remove all containers
echo -e "\nRunning dc rm -fv..."
docker-compose rm -fv

# Build images
echo -e "\nRunning dc build..."
docker-compose build

# Remove webdata and appstatic volumes
echo -e "\nRunning docker volume rm webdata, appstatic..."
docker volume rm webdata
docker volume rm appstatic

# Start docker-compose service
echo -e "\nRunning dc up -d..."
docker-compose up -d
