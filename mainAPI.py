import uvicorn
from fastapi import FastAPI
from fastapi_utils.tasks import repeat_every
from fastapi.logger import logger
from threading import Thread

from config import setting
from apis.dtos.ResponseDto import ResponseDto
from apis.__init__ import api_router
from apis import ApiServices
from apis.dtos import exampleResponse

app = FastAPI()
response = ResponseDto()


@app.get("/", description="Hello from author!", responses=exampleResponse.helloResponse)
def hello():
    return response.Success({"message": "Welcome to TST RSS-WEB crawler server"})


''' @app.on_event("startup")
@repeat_every(seconds=60 * 60 * 2)
def crawl():
    print("\tCrawling...")
    Thread(target=ApiServices.crawlerService(), name="crawl all").start() '''


app.include_router(api_router)

if __name__ == "__main__":
    uvicorn.run("mainAPI:app", host=setting.api_host, port=setting.api_port)
