# Step 1 - Delete logs directory
# Step 2 - Pull new images
# Step 3 - Stop all containers
# Step 4 - Remove all containers
# Step 5 - Build images
# Step 6 - Remove web volume
# Step 7 - Create web and app volume
# Step 8 - Start docker-compose service

# Delete logs directory
echo -e "\nDeleting logs directory..."
rm -rf logs

# Pulling docker containers
echo -e "\nRunning dc pull..."
docker-compose -f docker-compose-prod.yml pull

# Stop all containers
echo -e "\nRunning dc stop -t 1..."
docker-compose -f docker-compose-prod.yml stop -t 1

# Remove all containers
echo -e "\nRunning dc rm -fv..."
docker-compose -f docker-compose-prod.yml rm -fv

# Build images
echo -e "\nRunning dc build..."
docker-compose -f docker-compose-prod.yml build

# Remove web volume
echo -e "\nRunning docker volume rm webdata, appstatic..."
docker volume rm webdata

# Create web and app volume
echo -e "\nRunning docker volume create --name=webdata..."
docker volume create --name=webdata
docker volume create --name=appstatic

# Start docker-compose service
echo -e "\nRunning dc up -d..."
docker-compose -f docker-compose-prod.yml up -d

# Make .gitignore inside logs directory
touch ./logs/.gitignore
echo "[^.]*" >> ./logs/.gitignore
