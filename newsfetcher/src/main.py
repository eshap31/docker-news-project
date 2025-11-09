from get_news import NewsApiInit
from loggers import InitLogger
from get_news import FetchNews
from redis_integration import RedisConnect
from redis_integration import RedisPublisher
from continuous_publishing import PublishNewsContinuously


def main():
    # news_api_initializer
    api_initializer = NewsApiInit()
    api_initializer.initialize("NEWSAPI_KEY")
    InitLogger.logger.info("Initialized News API")
    news_fetcher = FetchNews(api_initializer)

    # connect to redis
    connector = RedisConnect()
    connector.initialize_and_connect_to_redis()

    # publish
    publisher = RedisPublisher(connector.redis_cli)

    # test main_loop
    cont_pub = PublishNewsContinuously(publisher, news_fetcher)
    cont_pub.main_loop()


if __name__ == "__main__":
    main()
