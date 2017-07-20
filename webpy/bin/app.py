# ex51-2

import web

urls = (
  '/main', 'Main',
  '/tricktips', 'Tricktips',
   # You can use /tricktips/? which was never taught...

  '/channels', 'Channels',
   # This doesn't work, while tricktips with the same url does...
   # idk y...
   # I think it was b/c the "C" in "Channels" was not capitalized


)

app = web.application(urls, globals())

render = web.template.render('templates/', base="layout")
# That tells lpthw.web to use the templates/layout.html file
# as the base template for all the other templates.
# Restart your application and then try to
# change the layout in interesting ways but without
# changing the other templates.

class Main(object):
    def GET(self):
        return render.main()

class Tricktips(object):
    def GET(self):
        return render.tricktips()

class Channels(object):
    def GET(self):
        return render.channels()


if __name__ == "__main__":
    app.run()
