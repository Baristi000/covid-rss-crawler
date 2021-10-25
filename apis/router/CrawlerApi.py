from fastapi import APIRouter, Body

from apis.dtos.ResponseDto import ResponseDto
import RssCrawler.CrawlerServices as services
from apis.dtos import exampleResponse

router = APIRouter()
response = ResponseDto()

@router.post("/test-crawler", description = "Test crawling one url", responses= exampleResponse.post_test_crawler)
def TestCrawler(url: str = Body(..., embed=True)):
    data = services.crawler(url)
    if data != None:
        return response.Success(data=data)
    return response.Badrequest("Url is not a RSS Feed url")