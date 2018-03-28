# Step 1 - Delete logs directory
# Step 2 - Stop all containers
# Step 3 - Remove all containers
# Step 4 - Build images
# Step 5 - Remove web volume
# Step 6 - Create web and app volume
# Step 7 - Start docker-compose service

# Delete logs directory
echo -e "\nDeleting logs directory..."
rm -rf logs

# Stop all containers
echo -e "\nRunning dc stop -t 1..."
docker-compose -f docker-compose-staging.yml stop -t 1

# Remove all containers
echo -e "\nRunning dc rm -fv..."
docker-compose -f docker-compose-staging.yml rm -fv

# Build images
echo -e "\nRunning dc build..."
docker-compose -f docker-compose-staging.yml build

# Remove web volume
echo -e "\nRunning docker volume rm webdata, appstatic..."
docker volume rm webdata

# Create web and app volume
echo -e "\nRunning docker volume create --name=webdata..."
docker volume create --name=webdata
docker volume create --name=appstatic

# Start docker-compose service
echo -e "\nRunning dc up -d..."
docker-compose -f docker-compose-staging.yml up -d
