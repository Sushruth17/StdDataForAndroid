import json
from BaseHTTPServer import httpserver, BaseHTTPRequestHandler
from optparse import OptionParser

class RequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        request_path = self.path

        print("\n----- Request Start ----->\n")
        print("request_path :", request_path)
        print("self.headers :", self.headers)
        print("<----- Request End -----\n")

        self.send_response(200)
        self.send_header("Set-Cookie", "foo=bar")
        self.end_headers()
        self.wfile.write(json.dumps({'hello': 'world', 'received': 'ok'}))

    def do_POST(self):
        request_path = self.path

        # print("\n----- Request Start ----->\n")
        print("request_path : %s", request_path)

        request_headers = self.headers
        content_length = request_headers.getheaders('content-length')
        length = int(content_length[0]) if content_length else 0

        # print("length :", length)

        print("request_headers : %s" % request_headers)
        print("content : %s" % self.rfile.read(length))
        # print("<----- Request End -----\n")

        self.send_response(200)
        self.send_header("Set-Cookie", "foo=bar")
        self.end_headers()
        self.wfile.write(json.dumps({'hello': 'world', 'received': 'ok'}))

    do_PUT = do_POST
    do_DELETE = do_GET


def main():
    port = 8082
    print('Listening on localhost:%s' % port)
    server = HTTPServer(('', port), RequestHandler)
    server.serve_forever()


if __name__ == "__main__":
    parser = OptionParser()
    parser.usage = ("Creates an http-server that will echo out any GET or POST parameters, and respond with dummy data\n"
                    "Run:\n\n")
    (options, args) = parser.parse_args()

    main()