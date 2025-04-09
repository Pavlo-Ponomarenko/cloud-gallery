docker build -t cloud-gallery .
docker run -p 5001:5000 --mount type=bind,source=$(pwd)/static,target=/app/static --name cloud-gallery cloud-gallery