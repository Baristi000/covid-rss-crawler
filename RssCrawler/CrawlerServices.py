import re
import feedparser
import ssl
import bs4
from selenium import webdriver
from nltk import tokenize


def clean_text(text):
    text = re.sub('<.*?>', '', text).strip()
    text = re.sub('[\+u]', '', text)
    text = re.sub('(\s)+', r'\1', text)
    return text


def sentence_segment(text):
    text.replace("\n", "")
    raw = text.split(". ")
    return raw


def crawler(rss: str = None):
    print("\tCrawling rss url:", rss)
    if hasattr(ssl, '_create_unverified_context'):
        ssl._create_default_https_context = ssl._create_unverified_context

    if rss is not None:
        blog_feed = feedparser.parse(rss)
        posts = blog_feed.entries

        post_list = []

        for post in posts:
            temp = dict()
            try:
                temp["title"] = clean_text(post.title)
            except:
                temp["title"] = "not found"
            try:
                temp["description"] = clean_text(post.description)
            except:
                temp["description"] = "not found"
            try:
                temp["link"] = post.link
            except:
                temp["link"] = "not found"
            try:
                temp["blog title"] = clean_text(blog_feed.feed.title)
            except:
                temp["blog title"] = "not found"
            try:
                temp["blog link"] = blog_feed.feed.link
            except:
                temp["blog link"] = "not found"
            try:
                temp["authors"] = [author["name"] for author in post.authors]
            except:
                temp["authors"] = ["not found"]
            try:
                temp["time_published"] = post.published
            except:
                temp["time_published"] = "not found"
            post_list.append(temp)
        # print(json.dumps(post_list, indent=1))
        return post_list
    else:
        return None

# Tạo selenium driver


def gen_driver(headless: bool = True):
    o = webdriver.ChromeOptions()
    o.add_argument("disable-features=VizDisplayCompositor")
    if headless:
        o.add_argument("headless")
    o.add_argument("window-size=1200x800")
    o.add_argument(
        "user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:64.0) Gecko/20100101 Firefox/64.0")
    driver = webdriver.Chrome(options=o)
    print("Generate driver!")
    return driver


# Crawl dữ liệu ở link cung cấp bởi rss


def crawl_detail(driver, url):
    driver.get(url)
    html = driver.page_source
    rawData = bs4.BeautifulSoup(html, "html.parser")
    for i in rawData(['style', 'script']):
        i.decompose()
    data = ' '.join(rawData.stripped_strings)
    return data

# Cắt đoạn văn thành mảng câu có nghĩa


def p2s(text: str):
    return tokenize.sent_tokenize(text)
