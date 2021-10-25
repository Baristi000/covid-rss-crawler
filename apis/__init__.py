from fastapi import APIRouter
from apis.router import CrawlerApi, UrlsApi

api_router = APIRouter()

api_router.include_router(CrawlerApi.router, prefix='/Crawl', tags=['crawl'])
api_router.include_router(UrlsApi.router, prefix='/RssUrl', tags=['rss'])