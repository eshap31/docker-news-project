# Docker News Project

This project is meant to teach development in the micro-services architecture.
This project consists of 5 micro services, that each run in their own docker container, and the entire project can be run using the docker-compose file. In addition this project includes health checks on each service:
- Redis pub-sub
- MongoDB
- News-Fetcher: a service that uses the [newsapi](https://newsapi.org/) to fetch technologically related news articles, and sends to redis pub-sub
- News-Processor: a service that reads from the redis pub-sub and writes to the mongodb database
- Frontend: a service that exposes a fastapi application that allows users to search through articles by the source. This service communicates with the mongodb

## Prerequesites
- docker version 28 and up
- wsl or linux machine

## Usage
Clone repository
```bash
git clone https://github.com/eshap31/docker-news-project
cd docker-news-project
```

Building News-Fetcher image
```bash
cd newsfetcher
docker build -t news-fetcher:v1 .
cd ..
```

Building News-Processor image
```bash
cd newsprocessor
docker build -t news-processor:v1 .
cd ..
```

Building Frontend image
```bash
cd source-request-frontend
docker build -t frontend:v1 .
cd ..
```

Creating a volume for the db:
```bash
docker volume create mongodb
```

## Running
```bash
docker-compose up -d
```

## Documentation of each service
pubsub:
- image: redis:latest
- network: news_net
- hostname in project: pubsub
- healthcheck: pinging the redis pubsub
- this service listens on pubsub:6379, and the channel that is being published to is: news-topic
- you can change the name of the channel (topic) in newsfetcher/src/configurations/config.json in the redis_topic variable, and in the newsprocessor/src/configurations/config.json in the redis_topic variable

mongodb:
- image: mongodb/mongodb-community-server:latest
- network: news_net
- hostname in project: db
- healthcheck: pinging the db
- this service listens on mongodb://db:27017/
- the name of the db is news_db
- the column that is being written to: articles
- you can customize the name of the db, and the column in the .env file in the newsprocessor folder, in the DB_NAME and DB_COL variables

News-Fetcher:
- image: news-fetcher:v1
- network: news_net
- healthcheck: checking connection to redis pub-sub
- this service gets the most recent technological articles via the newsapi, every 45 seconds, and sends them over to the redis pubsub
- you can change the publishing frequency (how often it gets articles and publishes to redis) via the newsfetcher/src/configurations/config.json in the publishing_frequency variable
- you can change the redis host to a remote one if you want, in the REDIS_HOST environment variable

News-Processor:
- image: news-processor:v1
- network: news_net
- healthcheck: checking connection to redis pub-sub, and the mongodb database
- this service listens to the redis pub-sub channel, and every time it gets and article it writes it to the mongodb database
- you can change the name of the database and the column name via the newsfetcher/.env file in the DB_NAME variable, and COL_NAME as well as in source-request-frontend/.env in the same variable names
- you can change the url of the db if you want the db to be remotely hosted in the DB_URL environment variable
- you can change the redis host to a remote one if you want, in the REDIS_HOST environment variable

Frontend:
- image: frontend:v1
- network: news_net
- healthcheck: checking the fastapi endpoint in 127.0.0.1:8000
- this service exposes a fastapi application on localhost:8000 and allows users to enter source names of news sources, and the service queries the db,
and returns articles that are published by the same source.

## License
[MIT](https://choosealicense.com/licenses/mit/)