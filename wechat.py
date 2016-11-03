# coding=utf-8

import itchat

@itchat.msg_register(itchat.content.TEXT)
def text_reply(msg):
    itchat.send(msg['Text']+u'this is 自动回复', msg['FromUserName'])

itchat.auto_login()
itchat.run()