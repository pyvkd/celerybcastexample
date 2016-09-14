from .tasks import sampletask
import json
import falcon


class TestIssue:
    def on_get(self, req, resp):
        l = json.dumps({'hello': 'world'})
        sampletask.apply_async([l], serializer="json", queue='q1')
        resp.body = "Hello World!"
        resp.content_type = "text/plain"
        resp.status = falcon.HTTP_200

test = TestIssue()
