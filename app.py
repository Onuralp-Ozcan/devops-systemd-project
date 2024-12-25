from http.server import SimpleHTTPRequestHandler, HTTPServer

host = '0.0.0.0'
port = 8080

class MyHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(b'Hello, World!')

server = HTTPServer((host, port), MyHandler)
print(f"Server running on http://{host}:{port}")
server.serve_forever()
