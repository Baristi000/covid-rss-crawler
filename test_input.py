from RssCrawler.CrawlerServices import crawler
from apis.ApiServices import push_data

data = crawler(
    "https://tools.cdc.gov/api/v2/resources/media/404952.rss")

push_data(data)
