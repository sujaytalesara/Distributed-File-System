import web

class MyWebApp(web.application):

    def run(self,port=8080,*middleware):
        func = self.wsgifunc(*middleware)
        return web.httpserver.runsimple(func, ('0.0.0.0',port))
