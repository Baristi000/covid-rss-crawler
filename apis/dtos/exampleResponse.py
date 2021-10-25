from apis.dtos.ResponseDto import ResponseDto

response = ResponseDto()

helloResponse = response.genExampleResponse(
  succeed_body={
                  "status": 200,
                  "time": "2021-08-18T01:32:01.103843",
                  "data": {
                    "message": "Welcome to TST RSS-WEB crawler server"
                  }
                }
)

get_crawler_url = response.genExampleResponse(
  succeed_body={
    "status": 201,
    "time": "2021-08-18T01:32:41.010606",
    "data": [
      "http://feeds.bbci.co.uk/news/rss.xml",
      "https://news.google.com/rss/search?hl=en-US&gl=US&ceid=US:en&q=CORONA+OR+COVID19",
      "https://www.health.gov.au/news/rss.xml",
      "https://tools.cdc.gov/api/v2/resources/media/404952.rss",
      "https://news.google.com/rss/search?hl=en-US&gl=US&ceid=US:en&q=covid19+AND+vaccine+",
      "https://connect.medrxiv.org/relate/feed/181",
      "https://www.who.int/rss-feeds/covid19-news-english.xml"
    ]
  }
)

post_test_crawler = response.genExampleResponse(
  succeed_body={
    "status": 200,
    "time": "2021-08-18T01:35:08.771049",
    "data": [
      {
        "title": "India’s Covid-19 Nmbers Have Fallen. A Third Wave Still Looms. - The New York Times",
        "description": "India’s Covid-19 Nmbers Have Fallen. A Third Wave Still Looms.&nbsp;&nbsp;The New York Times",
        "link": "https://www.nytimes.com/2021/08/17/world/asia/india-covid-19.html",
        "blog title": "\"CORONA OR COVID19\" - Google News",
        "blog link": "https://news.google.com/search?hl=en-US&gl=US&ceid=US:en&q=CORONA+OR+COVID19",
        "time_published": "Tue, 17 Aug 2021 16:48:20 GMT"
      },
    ]
  }
)

post_crawler_url = response.genExampleResponse(
  create_body={
    "status": 201,
    "time": "2021-08-18T01:36:29.126840",
    "data": {
      "message": "Add urls succeed"
    }
  }
)

delete_crawler_url = response.genExampleResponse(
  succeed_body={
    "status": 200,
    "time": "2021-08-18T01:37:31.387421",
    "data": {
      "message": "Remove urls succeed"
    }
  }
)