# coding=utf-8

import BaseHTTPServer
import io
import shutil
import urllib


class MyRequestHandler(BaseHTTPServer.BaseHTTPRequestHandler):
    def do_GET(self):
        print 'GET:'
        self.process(2)

    def do_POST(self):
        print 'POST:'
        self.process(1)

    def process(self, type):

        content = ""
        if type == 1:  # post方法，接收post参数
            datas = self.rfile.read(int(self.headers['content-length']))
            print datas
            datas = urllib.unquote(datas).decode("utf-8", 'ignore')  # 指定编码方式
            #datas = transDicts(datas)  # 将参数转换为字典
            #if datas.has_key('data'):
            #    content = "data:" + datas['data'] + "\r\n"

        if '?' in self.path:
            query = urllib.splitquery(self.path)
            action = query[0]

            if query[1]:  # 接收get参数
                queryParams = {}
                for qp in query[1].split('&'):
                    kv = qp.split('=')
                    queryParams[kv[0]] = urllib.unquote(kv[1]).decode("utf-8", 'ignore')
                    content += kv[0] + ':' + queryParams[kv[0]] + "\r\n"

            # 指定返回编码
            enc = "UTF-8"
            content = content.encode(enc)
            f = io.BytesIO()
            f.write(content)
            f.seek(0)
            self.send_response(200)
            self.send_header("Content-type", "text/html; charset=%s" % enc)
            self.send_header("Content-Length", str(len(content)))
            self.end_headers()
            shutil.copyfileobj(f, self.wfile)

server = BaseHTTPServer.HTTPServer(('', 8000), MyRequestHandler)
print 'started httpserver...'
server.serve_forever()

