# 1. Stop all running containers
docker stop $(docker ps -q)

# 2. Remove all containers
docker rm $(docker ps -aq)

# 3. Remove all volumes
docker volume rm $(docker volume ls -q)

# 4. Remove all networks (except default ones like bridge/host/none)
docker network prune -f

# 5. Remove all images
docker rmi $(docker images -q) -f

# 6. Remove build cache
docker builder prune -af

# 7. Final system prune (catch leftovers)
docker system prune -f

