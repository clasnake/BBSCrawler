'''
Created on Mar 10, 2014

@author: cla
'''
from scrapy.spider import Spider
from scrapy.selector import Selector
from BBSCrawler.items import BbsItem


class NewsmthSpider(Spider):
    name = "newsmth"
    allowed_domains = ["newsmth.net"]
    base_url = "http://www.newsmth.net/nForum/board/Career_Campus?ajax"
    urls = []
    for i in range(1, 3):
        urls.append(base_url + "&p=%s"%i)
    start_urls = urls
 
    def parse(self, response):
        # filename = response.url.split("/")[-1]
        # open(filename, 'wb').write(response.body)
         
        sel = Selector(response)
        td = sel.xpath('/html/body/section[@id="main"]/section[@id="body"]/div[@class="b-content"]/table[@class="board-list tiz"]/tbody/tr/td[@class="title_9"]')
        items = []
        for site in td:
            x = site.xpath('a/text()').extract()
            y = site.xpath('a/@href').extract()
            if len(x) == 1 and len(y) == 1:
                item = BbsItem()
                item['title'] = x[0]
                item['link'] = y[0]
                item['content'] = ""
                item['domain'] = self.allowed_domains[0]
                items.append(item)
        return items

# class ByrSpider(BaseSpider):
#     name = "byr"
#     allowed_domains = ["bbs.byr.cn"]
#     base_url = "http://bbs.byr.cn/board/JobInfo?"
#     urls = []
#     for i in range(1, 2):
#         urls.append(base_url + "p=%s&_uid=guest&_uid=guest"%i)
#     start_urls = urls