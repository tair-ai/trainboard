#!/usr/bin/env python
# coding: utf-8

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import tornado.ioloop
import tornado.web
import tornado
import logging
from tornado.options import options, parse_command_line, define
from tornado.httpserver import HTTPServer


class MainHandler(tornado.web.RequestHandler):

    @tornado.web.asynchronous
    @tornado.gen.engine
    def get(self):
        self.render("index.html")


class Application(tornado.web.Application):

    def __init__(self):
        settings = dict(
            static_path="static",
            template_path="templates",
            debug=True
        )
        urls = [
            (r"/?", MainHandler),
        ]
        super(Application, self).__init__(urls, **settings)


def main():
    http_server = HTTPServer(Application())
    http_server.listen(8666)
    http_server.start()
    tornado.ioloop.IOLoop.instance().start()


if __name__ == "__main__":
    main()
