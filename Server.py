from twisted.web import server, resource
from twisted.internet import reactor, endpoints

from LControl import LControl
import time

control = LControl()
control.serve_forever()

class Simple(resource.Resource):
    isLeaf = True

    # A simple example of using the query params as a way to get x/y coords.
    def render_GET(self, request):
        control.q.put((request.args[b'x'][0].decode('ASCII'), request.args[b'y'][0].decode('ASCII')))
        return b"Moving to x= %s y= %s" %(request.args[b'x'][0], request.args[b'y'][0])


site = server.Site(Simple())
endpoint = endpoints.TCP4ServerEndpoint(reactor, 8080)
endpoint.listen(site)
reactor.run()
