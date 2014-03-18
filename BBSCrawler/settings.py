# Scrapy settings for BBSCrawler project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'BBSCrawler'

SPIDER_MODULES = ['BBSCrawler.spiders']
NEWSPIDER_MODULE = 'BBSCrawler.spiders'
COMMANDS_MODULE = 'BBSCrawler.commands'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'BBSCrawler (+http://www.yourdomain.com)'
ITEM_PIPELINES = { 'BBSCrawler.pipelines.pipelines.BbsCrawlerPipeline': 300,}
DEFAULT_REQUEST_HEADERS = {'Accept':'text/heml,application/xhtml+xml;q=0.9,*/*;q=0.8','Accept-Language':'ch',}
