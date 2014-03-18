# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field

class BbsItem(Item):
    title = Field()
    link = Field()
    content = Field()
    domain = Field()

class SjtuPreItem(Item):
    page = Field()
    
# 
# class NewsmthItem(Item):
#     title = Field()
#     link = Field()
# 
# class SjtuItem(Item):
#     title = Field()
#     link = Field()