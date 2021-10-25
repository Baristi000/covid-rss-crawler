from fastapi import APIRouter, Body

from apis.dtos.ResponseDto import ResponseDto
from config import setting
import RssCrawler.CrawlerServices as services
from apis.dtos import exampleResponse

router = APIRouter()
response = ResponseDto()

@router.get("/crawler-urls", description = "Get all RSS feed url", responses = exampleResponse.get_crawler_url)
def GetAllCrawlerUrls():
    return response.Create(setting.urls)

@router.post("/crawler-urls", description = "Add RSS feed url", responses = exampleResponse.post_crawler_url)
def AddRssFeedUrls(url: str = Body(..., embed = True)):
    if setting.AddRSSFeedUrls(url):
        return response.Create({
            "message":"Add urls succeed"
        })
    return response.Badrequest("Adding RSS feed url false")

@router.delete("/crawler-urls", description = "Remove RSS feed url", responses = exampleResponse.delete_crawler_url)
def RemoveRssFeedUrls(url: str = Body(..., embed = True)):
    if setting.RemoveRSSFeedUrls(url):
        return response.Success({
            "message":"Remove urls succeed"
        })
    return response.Badrequest("No matching RSS feed url")