# i-crawler

-----------

# Setup

1. Install Docker and docker-compose using bellow docker docs source

https://docs.docker.com/engine/installation/linux/ubuntu/#install-using-the-repository

```
pip install docker-compose==1.10.0
```

2. Add docker to group

```
sudo usermod -aG docker ${USER}
```

3. Set max_map_count value (Linux)

```
sudo sysctl -w vm.max_map_count=262144
```

4. Set app and run

```
git clone git@github.com:jarekswierek/i-crawler.git
cd i-crawler
docker-compose build
docker-compose up
```

Application will be available on **localhost:8000**
ElasticSearch will be available on **localhost:9200**
