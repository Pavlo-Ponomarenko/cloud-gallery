docker build -t cloud-gallery .
docker run -p 5000:5000 --mount type=bind,source=$(pwd)/static,target=/app/static cloud-gallery