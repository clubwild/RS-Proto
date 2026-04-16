import http.server
import os

PORT = 3456
DIR  = "/Users/chloe.cardona/Documents/Claude/RS-Proto"

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIR, **kwargs)

with http.server.HTTPServer(("", PORT), Handler) as httpd:
    httpd.serve_forever()
