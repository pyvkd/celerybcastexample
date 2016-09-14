import falcon
from .views import test

app = falcon.API()
app.add_route('/test', test)
