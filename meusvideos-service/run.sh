docker rm -f meusvideos &&
docker build -t meusvideos . &&
docker run  --name meusvideos -p 8000:8000 --network host meusvideos