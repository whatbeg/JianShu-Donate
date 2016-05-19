# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
import json
import codecs
from operator import itemgetter

class Jianshu2Pipeline(object):

    def __init__(self):
	    self.file = codecs.open('items.json','wb','utf-8')
	    self.quote = {}
	    self.filecsv = codecs.open('items.csv','w','utf-8')

    def process_item(self, item, spider):
        
        line = json.dumps(dict(item)) + "\n"
        self.file.write(line.decode("unicode_escape"))

        if item['quote'] in self.quote.keys():
            self.quote[item['quote']] += item['likeNum']
        else:
            self.quote[item['quote']] = item['likeNum']

        self.filecsv.seek(0)
        lis = sorted(self.quote.items(),key=itemgetter(1),reverse=True)
        for i in range(len(lis)):
            line2 = lis[i][0] + '\t' + str(lis[i][1]) + '\r\n'
            self.filecsv.write(line2.decode("utf-8"))

        return item
