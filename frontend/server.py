import os
from http.server import SimpleHTTPRequestHandler
from socketserver import TCPServer

PORT = int(os.environ.get("PORT", 8080))


class Handler(SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header("Cache-Control", "public, max-age=300")
        super().end_headers()

    def log_message(self, format, *args):
        print(f"[frontend] {self.address_string()} - {format % args}")


if __name__ == "__main__":
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    with TCPServer(("0.0.0.0", PORT), Handler) as httpd:
        print(f"Serving immigration.datawebify.com frontend on port {PORT}")
        httpd.serve_forever()
