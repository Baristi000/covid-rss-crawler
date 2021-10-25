from RssCrawler.CrawlerServices import crawl_detail, gen_driver

driver = gen_driver()
data = crawl_detail(
    driver, "https://time.com/6104645/malaria-vaccine/")

f = open("data.txt", "w")
f.write(data)
f.close()
print(data)
