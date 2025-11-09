import time
from get_news import FetchNews
from redis_integration import RedisPublisher
from configurations import LoadConfigVariables
from loggers import InitLogger
import json


class PublishNewsContinuously:
    def __init__(self, redis_publisher: RedisPublisher, news_fetcher: FetchNews):
        self.redis_publisher = redis_publisher
        self.news_fetcher = news_fetcher
        self.config_var_loader = LoadConfigVariables()

    def main_loop(self):
        while True:
            top_headlines = self.news_fetcher.get_top_articles()["articles"]
            for headline in top_headlines:
                self.redis_publisher.publish(json.dumps(headline))
                InitLogger.logger.debug(f"published this headline: '{headline}'")

            time.sleep(self.config_var_loader.load_config_variable("publishing_frequency"))
