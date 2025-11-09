from get_news import NewsApiInit
from loggers import InitLogger


class FetchNews:
    def __init__(self, news_initializer: NewsApiInit):
        self.news_initializer = news_initializer

    def get_top_articles(self):
        query_params_dict = self.news_initializer.query_params_dict
        top_headlines = self.news_initializer.newsapi.get_top_headlines(q=query_params_dict['q'],
                                                                        sources=query_params_dict['sources'],
                                                                        category=query_params_dict['category'],
                                                                        language=query_params_dict['language'],
                                                                        country=query_params_dict['country'])

        InitLogger.logger.debug(f"Fetched headlines, by these criteria: {top_headlines}")
        return top_headlines
