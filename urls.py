import os
import tornado.ioloop
import tornado.web
import view
import settings as config

application = tornado.web.Application([
    (r"/", view.MainHandler),
    (r"/home", view.MainHandler),
], **config.settings)

if __name__ == "__main__":
    application.listen(8012)
    tornado.ioloop.IOLoop.instance().start()
