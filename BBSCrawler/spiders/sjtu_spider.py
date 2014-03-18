'''
Created on Mar 10, 2014

@author: cla
'''
from scrapy.spider import Spider
from scrapy.selector import Selector
from BBSCrawler.items import BbsItem
import json
import string

class SjtuSpider(Spider):
    name = "sjtu"
    allowed_domains = ["bbs.sjtu.edu.cn"]

    page = 0
    with open("sjtupre.json") as json_file:
        json_data = json.load(json_file)
        num = json_data['page']
        page = string.atoi(num)
    home = (page - 78561) / 20 + 3928
    base_url = "https://bbs.sjtu.edu.cn/bbstdoc,board,JobInfo,page,"
    urls = []
    for i in range(1, 5):
        urls.append(base_url + "%s.html"%(home - i + 1))
    print urls
    start_urls = urls
#     start_urls = ["https://bbs.sjtu.edu.cn/bbstdoc,board,JobInfo,page,3911.html",] 
    def parse(self, response):
        # filename = response.url.split("/")[-1]
        # open(filename, 'wb').write(response.body)
        sel = Selector(response)
        tr = sel.xpath('/html/body/nobr/center/table/tr/td[5]')
        items = []
        for i in tr:   
            x = i.xpath('a/text()').extract()
            y = i.xpath('a/@href').extract()
            if len(x) == 1 and len(y) == 1:
                item = BbsItem()
                item['title'] = x[0]
                item['link'] = y[0]
                item['content'] = ""
                item['domain'] = self.allowed_domains[0]
                items.append(item)
        return items
     