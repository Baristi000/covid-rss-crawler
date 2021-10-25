from config import setting
from RssCrawler import CrawlerServices
from threading import Thread
import grpc
import json
from queue import Queue

from protobuf import train_pb2, train_pb2_grpc


def create_request(datas: list):
    input_datas = []
    for data in datas:
        item = train_pb2.Block(
            title=data["title"],
            description=data["description"],
            link=data["link"],
            blog_title=data["blog title"],
            blog_link=data["blog link"],
            authors=data["authors"],
            time_published=data["time_published"]
        )
        input_datas.append(item)
    return train_pb2.InputData(block=input_datas)


def push_data(datas: list):
    try:
        chanel = grpc.insecure_channel(setting.core_url)
        stub = train_pb2_grpc.TrainStub(chanel)
        res = stub.Training(create_request(datas))
        if res.status == 200:
            print("\tPush data succeed")
    except:
        pass


def crawlerService():
    i = 0
    for url in setting.urls:
        datas = CrawlerServices.crawler(url)
        push_data(datas)
        i += 1
        if i == len(setting.urls):
            print("Crawl data is done")
