# git pull code
echo "update github code"
git fetch --all
git reset --hard origin/master
git pull

#
echo "running services"
docker-compose build
docker-compose down
docker-compose up -d
