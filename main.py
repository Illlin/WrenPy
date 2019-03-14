#!/usr/bin/env python3

from http.server import BaseHTTPRequestHandler, HTTPServer
import ssl
import json
import pages

posts = {}
gets = {}

print("--------")
print("Setting up pages:")
for page in pages.pages:
    if page[1].is_page:
        if page[1].POST:
            posts[page[0]] = page[1]
        if page[1].GET:
            gets[page[0]] = page[1]

print("Post Pages:")
for i in posts:
    print(i)
print("Get Pages:")
for i in gets:
    print(i)
print("--------")

class HTTPServerRequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        print(self.path)
        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps({"sucess":True}).encode("utf-8"))

    def do_POST(self):
        # Get location that post request was made
        print(self.path)
        path = self.path.split("/")[1:]

        # If valid address call
        if path[0] in posts:
            content_length = int(self.headers["Content-Length"])
            body = self.rfile.read(content_length)
            # See if Valid JSON
            try:
                data = json.loads(body)
                response, return_json = posts[path[0]].main(path[1:],data)
                self.send_response(response)
                self.send_header("Content-type", "application/json")
                self.end_headers()
                print(data)
                self.wfile.write(json.dumps(return_json).encode("utf-8"))

            except json.decoder.JSONDecodeError:
                print(body)
                self.send_response(400)
                self.send_header("Content-type", "application/json")
                self.end_headers()
                self.wfile.write(json.dumps({"sucess":False}).encode("utf-8"))

        # Page not found as valid for POST request
        else:
            self.send_response(404)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps({"sucess":False}).encode("utf-8"))


def main():
    print('starting server... ',end="",flush=True)
    # Server settings
    server_address = ('localhost', 443)
    httpd = HTTPServer(server_address, HTTPServerRequestHandler)
    print("Done")
    print("Adding SSL...      ",end="",flush=True)
    httpd.socket = ssl.wrap_socket (
        httpd.socket,
        keyfile="ssl/host.key",
        certfile="ssl/host.cert",
        server_side=True,
    )
    print("Done")
    print('running server...  Done')
    httpd.serve_forever()

main()