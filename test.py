from transformers import pipeline
from RssCrawler.CrawlerServices import crawl_detail, gen_driver
from time import time


driver = gen_driver(False)
start = time()
data = crawl_detail(
    driver, "https://time.com/6104645/malaria-vaccine/")

''' f = open("data.txt", "r", encoding="utf8")
data = f.read() '''

# Initialize the HuggingFace summarization pipeline
summarizer = pipeline("summarization")
summarized = summarizer(data, min_length=75, max_length=300)

#end = time()-start
# Print summarized text
#print("\tduration:", end)
print(summarized)
