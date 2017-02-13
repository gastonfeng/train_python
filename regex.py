# coding=utf-8
import json
import re

import time


pattern = re.compile(u'优惠券(.*)')
match = pattern.match(u'ggggg优惠券 大衣')
if match:
    print match.group()
    print match.group(1)


pattern = re.compile(u'优惠券(.*)')
match = pattern.search(u'ggggg优惠券 大衣')
if match:
    print match.group()
    print match.group(1)

a = re.match(u'加群 (.*)', u'加群 12345')
if a:
    print a.group()
    print a.group(1)

f=open('json.txt')
x=f.read().decode('GBK')
print x[140240:140260]
f.close()
m = re.search('(\{.*\})', x)
if m:
    print m.group()
    clusters_json = m.group()
    j = json.loads(clusters_json)
    print j['code']
    if j['code'] == 0:
        clusters = j['data']['group']
        for cluster in clusters:
            print cluster['groupname']

aa = re.compile('[\\x00-\\x08\\x0b-\\x0c\\x0e-\\x1f]').sub(' ', x)


def remove_invalid_utf8(data):
    #    new_data,count = re.subn('[x00-x08x10x0Bx0Cx0E-x19x7F]'
    #        + '|[x00-x7F][x80-xBF]+'
    #        + '|([xC0xC1]|[xF0-xFF])[x80-xBF]*'
    #        + '|[xC2-xDF]((?![x80-xBF])|[x80-xBF]{2,})'
    #        + '|[xE0-xEF](([x80-xBF](?![x80-xBF]))|(?![x80-xBF]{2})|[x80-xBF]{3,})', '!', data)
    new_data, count = re.subn('xE0[x80-x9F][x80-xBF]' + '|xED[xA0-xBF][x80-xBF]', '?', data)
    new_data = re.sub('xEDxA6x88', '?', new_data)
    return new_data


aa = remove_invalid_utf8(aa).decode('utf-8')
mmm = json.loads(aa)
print mmm['count']
print len(mmm['mems'])
for i in mmm['mems']:
    join_time = time.localtime(i['join_time'])
    join_time = time.strftime('%Y-%m-%d %H:%M:%S', join_time)
    print i['nick']
