# -*- coding: utf-8 -*-

# Scrapy settings for jianshu2 project


BOT_NAME = 'jianshu2'

SPIDER_MODULES = ['jianshu2.spiders']
NEWSPIDER_MODULE = 'jianshu2.spiders'

ITEM_PIPELINES = {
    'jianshu2.pipelines.Jianshu2Pipeline': 300,
}


FEED_URI=u'D:\Python27\jianshu2\jianshu2\spiders\data.csv'
FEED_FORMAT='CSV'

#LOG_FILE = u'D:\Python27\jianshu2\jianshu2\spiders\log.txt'
LOG_STDOUT = False
