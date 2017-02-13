#coding=utf-8
import re

members_json= u'49,mpq_woniu,插件,11:25:00,_GetGroupPortal_Callback({"code":0,"data":{"group":[{"auth":0,"flag":0,"groupid":105597306,"groupname":"星期八UI"},{"auth":0,"flag":0,"groupid":134283874,"groupname":"同城交友"},{"auth":0,"flag":0,"groupid":138918389,"groupname":"嘉豪健身游泳群"},{"auth":0,"flag":0,"groupid":149735832,"groupname":"单片机兴趣群"},{"auth":0,"flag":0,"groupid":151732219,"groupname":"zigbee无线产品开发群"},{"auth":0,"flag":0,"groupid":211517018,"groupname":"QQ机器人群管"},{"auth":0,"flag":0,"groupid":246806523,"groupname":"仪器仪表技术研发"},{"auth":0,"flag":0,"groupid":274567699,"groupname":"凯控产品销售"},{"auth":0,"flag":0,"groupid":293522894,"groupname":"嵌入式系统开发"},{"auth":0,"flag":0,"groupid":293529841,"groupname":"工业控制技术交流"},{"auth":0,"flag":0,"groupid":367890963,"groupname":"凯控员工"},{"auth":0,"flag":0,"groupid":421301462,"groupname":"电子产品开发群"},{"auth":0,"flag":0,"groupid":445049995,"groupname":"昌平图书馆"},{"auth":0,"flag":0,"groupid":471635379,"groupname":"90后同城交友"},{"auth":0,"flag":0,"groupid":475249295,"groupname":"LED显示屏订制开发生产"},{"auth":0,"flag":0,"groupid":478492959,"groupname":"python实习生兼职"},{"auth":0,"flag":0,"groupid":534455324,"groupname":"淘宝内部优惠券"},{"auth":0,"flag":0,"groupid":548440152,"groupname":"昌平电子创业"},{"auth":0,"flag":0,"groupid":608159724,"groupname":"爱奇艺会员分享群"}],"total":19},"default":0,"message":"","subcode":0});'

match = re.search('(\{.*\})', members_json)
members_json = match.group()
file = open('json.txt', 'wb')
file.write(members_json.encode('GBK', errors='ignore'))
file.close()
