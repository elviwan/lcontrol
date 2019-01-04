from twisted.web.server import Site
from twisted.internet import reactor
from twisted.web.resource import Resource
from LControl import LControl


class Quit(Resource):
    def render_GET(self, request):
        control.q.put("quit")
        return b"Quitting..."


class Start(Resource):
    def render_GET(selfself, request):
        control.serve_forever()
        return b'Starting...'


class Move(Resource):
    isLeaf = True

    # A simple example of using the query params as a way to get x/y coords.
    def render_GET(self, request):
        if b'x' in request.args and b'y' in request.args:
            control.q.put((request.args[b'x'][0].decode('ASCII'), request.args[b'y'][0].decode('ASCII')))
            return b"Moving to x= %s y= %s" % (request.args[b'x'][0], request.args[b'y'][0])
        else:
            request.setResponseCode(500)
            return b'Not Implemented'


class LControlRoot(Resource):
    def getChild(self, name, request):
        if name == b'quit':
            return Quit()
        if name == b'start':
            return Start()
        return Move()


control = LControl()
control.serve_forever()
root = LControlRoot()
factory = Site(root)
reactor.listenTCP(8080, factory)
reactor.run()
