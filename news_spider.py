"""
爬网页
"""
import time
import requests
from lxml import etree
import json
import pymysql
class SinaSpider(object):
    def __init__(self):
        self.item={}
        self.url='https://www.hao123.com/feedData/data?type={}&app_from=pc_tuijian&rn={}&pn={}&_={}'
        self.item['category']="{}"
    def get_html(self):
        html=requests.get(
            url=self.url,
            headers={'User-Agent':"Mozilla/5.0"}
        ).text
        html=json.loads(html)
        self.parse_html(html)
    def parse_html(self,html):
        for dict in html['data']:
            self.item["source"]=dict['source']
            self.item["content"]=dict['desc']
            self.item['title']=dict['title']
            self.item['url']=dict['url']
            self.item['time']=dict['time']
            print(self.item)
    def run(self):
        category=input("请输入项目(国际|体育|国内|娱乐|时政):")
        self.item["category"]="{}".format(category)
        # 国际 intl 体育 sports  国内 domestic  娱乐 ent 时政 rec
        type=input('请输入查询项目(intl|sports|demestic|ent|tec):')
        rn = 10
        for page in range(1,30):
            t=int(time.time()*1000)
            self.url.format(type,page,rn,t)
            self.get_html()
            rn+=10
if __name__=="__main__":
    spidrer=SinaSpider()
    spidrer.run()
