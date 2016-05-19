import scrapy
from jianshu2.items import Jianshu2Item
from scrapy.http import Request
from scrapy.selector import Selector


class postSpider(scrapy.spiders.Spider):
    
    name = 'post'
    start_urls = ['http://www.jianshu.com']
    url = 'http://www.jianshu.com'

    def parse(self, response):
        selector = Selector(response)
        articles = selector.xpath('//ul[@class="article-list thumbnails"]/li')
        
        for article in articles:
            item = Jianshu2Item()
            url = article.xpath('div/h4/a/@href').extract()
            likeNum = article.xpath('div/div/span[2]/text()').extract()
            posturl = 'http://www.jianshu.com'+url[0]
            
            if len(likeNum) == 0:
                item['likeNum'] = 0
            else:
                item['likeNum'] = int(likeNum[0].split(' ')[-1])

            request = Request(posturl,callback=self.parse_donate)
            request.meta['item'] = item
            yield request
            
        next_link = selector.xpath('//*[@id="list-container"]/div[@class="load-more"]/button/@data-url').extract()[0]
        if next_link:
            next_link = self.url + str(next_link)
            yield Request(next_link,callback=self.parse)


    def parse_donate(self, response):
        donate = response.xpath('//div[@class="support-author"]/p/text()').extract()
        item = response.meta['item']
        if len(str(donate)) == 0:
            item['quote'] = ""
        else:
            item['quote'] = str(donate[0].encode('utf-8'))
            
        return item
















