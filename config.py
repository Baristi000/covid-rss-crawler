import json


class Settings():
    def __init__(self):
        try:
            f = open("Resource/RssUrl.json", "r")
            self.urls = json.load(f)["url"]
            f.close()
        except:
            self.urls = []

    def AddRSSFeedUrls(self, url: str):
        try:
            if "http" not in url:
                raise False
            self.urls.append(url)
            f = open("Resource/RssUrl.json", "w")
            json.dump({"url": self.urls}, f, indent=2)
            f.close()
            return True
        except:
            return False

    def RemoveRSSFeedUrls(self, url: str):
        try:
            self.urls.remove(url)
            f = open("Resource/RssUrl.json", "w")
            json.dump({"url": self.urls}, f, indent=2)
            f.close()
            return True
        except:
            return False

    api_host = "0.0.0.0"
    api_port = 8000
    core_url = "localhost:9090"


setting = Settings()
