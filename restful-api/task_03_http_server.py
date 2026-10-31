#!/usr/bin/python3
"""A simple HTTP API using Python's http.server module."""

import json
from http.server import BaseHTTPRequestHandler, HTTPServer


class SimpleAPIHandler(BaseHTTPRequestHandler):
    """Handle incoming HTTP GET requests."""

    def do_GET(self):
        """Return a response based on the requested endpoint."""
        if self.path == "/":
            status = 200
            content_type = "text/plain"
            content = b"Hello, this is a simple API!"

        elif self.path == "/data":
            status = 200
            content_type = "application/json"
            data = {
                "name": "John",
                "age": 30,
                "city": "New York"
            }
            content = json.dumps(data).encode("utf-8")

        elif self.path == "/status":
            status = 200
            content_type = "text/plain"
            content = b"OK"

        elif self.path == "/info":
            status = 200
            content_type = "application/json"
            info = {
                "version": "1.0",
                "description": "A simple API built with http.server"
            }
            content = json.dumps(info).encode("utf-8")

        else:
            status = 404
            content_type = "text/plain"
            content = b"Endpoint not found"

        self.send_response(status)
        self.send_header("Content-Type", content_type)
        self.send_header("Content-Length", str(len(content)))
        self.end_headers()
        self.wfile.write(content)


if __name__ == "__main__":
    server = HTTPServer(("localhost", 8000), SimpleAPIHandler)
    print("Server running on http://localhost:8000")

    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nServer stopped.")
    finally:
        server.server_close()
