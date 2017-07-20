import web

urls = (
  '/upload', 'Upload'
 )


app = web.application(urls, globals())

render = web.template.render('templates/')

class Upload(object):
    def GET(self):
        return render.Upload()

    def POST(self):
        x = web.input(myfile={})
        web.debug(x['myfile'].filename) # This is the filename
        web.debug(x['myfile'].value) # This is the file contents
        web.debug(x['myfile'].file.read()) # Or use a file(-like) object
        raise web.seeother('/upload')


if __name__ == "__main__":

   app.run()
