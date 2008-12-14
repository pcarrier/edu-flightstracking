#!/usr/bin/env python
import sys
sys.path.append("webpy/")
import web

urls = (
    '/', 'main',
    '/flights.xml', 'flights',
    '/flights.html', 'html',
    '/doc.kml', 'kml',
    )
app = web.application(urls, globals())

class hello:
    def GET(self, name):
        if not name: 
            name = 'world'
        return 'Hello, ' + name + '!'
    def POST(self, name):
        pass

class main:
    def GET(self):
        web.redirect('/static/main.html')

class flights:
    def GET(self):
        pass
    def POST(self):
        pass
        
class html:
    def GET(self):
        pass
    
class kml:
    def GET(self):
        pass

if __name__ == "__main__":
    app.run()
