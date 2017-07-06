# -*- coding:utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json
import codecs
import string


class W3SchoolPipeline(object):
    def __init__(self):
        self.file = codecs.open('w3school_data_utf8.json','wb', encoding='utf-8')

        # 参数需要加上, encoding='utf-8'，因为写入需要二进制码，encoding可以生成二进制码
        '''
        global f
        f = open('w3school_data_utf8_2.txt','wb')
        '''
        #还没实现将所得数据放到txt里面

    def process_item(self, item, spider):
        line = json.dumps(dict(item),ensure_ascii=False)+ '\n'   #加上参数ensure_ascii=False,生成的json里面就可以显示中文啦~！
        #print (line)
        self.file.write(line)
        #print(dict(item))
        '''
        for i in dict:
            print (i, dict[i])
            write_str = str(i) + ' ' + dict[i] + '\n'
            f.write(write_str)
        '''
        #想把字典放到txt里面，会出现 TypeError: 'type' object is not iterable
        '''
        item = item['title']
        f.write(item.encode())
        f.close()                     #list object has no attribute encode() 主要是list不能转bytes
        '''
        return item
