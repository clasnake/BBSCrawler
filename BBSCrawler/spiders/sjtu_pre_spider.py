'''
Created on Mar 18, 2014

@author: cla
'''
from scrapy.spider import Spider
from scrapy.selector import Selector
from BBSCrawler.items import SjtuPreItem

class SjtuSpider(Spider):
    name = "sjtupre"
    allowed_domains = ["bbs.sjtu.edu.cn"]
    start_urls = ["https://bbs.sjtu.edu.cn/bbstdoc,board,JobInfo.html",]
 
    def parse(self, response):
        # filename = response.url.split("/")[-1]
        # open(filename, 'wb').write(response.body)
         
        sel = Selector(response)
        tr = sel.xpath('/html/body/nobr/center/table/tr[2]/td[1]/text()')
        item = SjtuPreItem()
        item['page'] = tr.extract()[0]
        return item