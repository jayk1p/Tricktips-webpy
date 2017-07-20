import web

urls = (
    '/','index'
)


app = web.application(urls, globals())

render = web.template.render('templates/')

class index:
    def GET(self):
        # return "Hello, world!"
        name = 'Bob'
        return render.index(name)

# This GET function will now get called by web.py
# anytime someone makes a GET request for /.



# Now we need to create an application specifying the urls and
# a way to tell web.py to start serving web pages:

if __name__ == "__main__":

    # First we tell web.py to create an application with the URLs
    # we listed above, looking up the classes in the global
    # namespace of this file.

    app.run()
    # And finally we make sure that
    # web.py serves the application we created above.
