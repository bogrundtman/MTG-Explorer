# !/usr/bin/env python
# -*- coding: utf-8 -*-

import tornado.web
import tornado.httpclient
import os
import requests


settings = {
    "static_path": os.getcwd()+"/static"
}

class Handler(tornado.web.RequestHandler):

    @tornado.web.asynchronous
    def get(self):
        query = self.request.uri.split("?")[1]
        self.http_client = tornado.httpclient.AsyncHTTPClient()
        searchurl = 'http://api.sl.se/api2/realtimedepartures.jason?key=281ea50514be47d585df429b180dfb0b&'+query
        r = requests.get(searchurl, verify=False)
        r.encoding = 'utf-8'
        self.set_header('Content-Type', 'application/json; charset=utf-8')
        self.set_header("Access-Control-Allow-Origin", "*")
        self.write(r.text)
        self.finish()
        return

application = tornado.web.Application([
    (r"/sl/", Handler),
    (r'/static/(.*)', tornado.web.StaticFileHandler, {'path': os.getcwd()+'/static'})

], **settings)

print 'Server started...'
application.listen(8800)
tornado.ioloop.IOLoop.instance().start()