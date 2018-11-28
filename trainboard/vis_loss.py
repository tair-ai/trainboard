#!/usr/bin/env python
# coding=utf-8
# vim: set et sw=4 ts=4 sts=4
# Author: nasa
# Created: 2018-11-27 18:51 CST


import tornado.web
import tornado.ioloop
import tornado.httpserver
import tornado.options
import os
import datetime
import json

from tornado.web import RequestHandler
from tornado.options import define, options


define("port", default=9000, type=int)
define("lossfile", default="../examples/train.log", type=str)


class IndexHandler(RequestHandler):
    def get(self):
        self.render("index.html")


class LossHandler(RequestHandler):
    fp = options.lossfile

    def get(self):
        loss = []

        with open(self.fp) as f:
            for i in f.readlines():
                if "solver.cpp:218" in i:
                    s = i.split("=")
                    s_ =  s[-1].strip()
                    if "e" in s_:
                        z = s_.split("e")
                        s_ = float(z[0])* (10 ** int(z[-1]))
                    loss.append(float(s_))

        self.write(json.dumps(loss))


if __name__ == '__main__':
    tornado.options.parse_command_line()
    app = tornado.web.Application([
            (r"/", IndexHandler),
            (r"/loss", LossHandler),
        ],
        static_path = os.path.join(os.path.dirname(__file__), "static"),
        template_path = os.path.join(os.path.dirname(__file__), "template"),
        debug = True
        )
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.current().start()

