#!/usr/bin/env python3
"""
Simple proxy server to handle OpenRouter API requests and bypass CORS restrictions.
"""

import json
import urllib.parse
from http.server import HTTPServer, BaseHTTPRequestHandler
import urllib.request
import urllib.error

class ProxyHandler(BaseHTTPRequestHandler):
    def do_OPTIONS(self):
        """Handle preflight CORS requests."""
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type, Authorization, HTTP-Referer, Origin')
        self.send_header('Access-Control-Max-Age', '86400')
        self.end_headers()

    def do_GET(self):
        """Handle GET requests to proxy OpenRouter API calls."""
        try:
            # Parse the request path
            if self.path.startswith('/api/'):
                # Extract the API path and query parameters
                api_path = self.path[4:]  # Remove '/api/' prefix
                
                # Build the target URL
                target_url = f"https://openrouter.ai/api{api_path}"
                
                # Forward the request to OpenRouter
                req = urllib.request.Request(target_url)
                
                # Copy headers from the original request
                for header, value in self.headers.items():
                    if header.lower() not in ['host', 'content-length']:
                        req.add_header(header, value)
                
                # Make the request
                try:
                    with urllib.request.urlopen(req) as response:
                        data = response.read()
                        
                        # Send response back to client
                        self.send_response(200)
                        self.send_header('Access-Control-Allow-Origin', '*')
                        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
                        self.send_header('Access-Control-Allow-Headers', 'Content-Type, Authorization, HTTP-Referer, Origin')
                        self.send_header('Content-Type', 'application/json')
                        self.send_header('Content-Length', str(len(data)))
                        self.end_headers()
                        self.wfile.write(data)
                        
                except urllib.error.HTTPError as e:
                    # Forward the error response
                    error_data = e.read()
                    self.send_response(e.code)
                    self.send_header('Access-Control-Allow-Origin', '*')
                    self.send_header('Content-Type', 'application/json')
                    self.send_header('Content-Length', str(len(error_data)))
                    self.end_headers()
                    self.wfile.write(error_data)
                    
            else:
                # Serve static files
                self.serve_static_file()
                
        except Exception as e:
            self.send_error(500, f"Proxy error: {str(e)}")

    def serve_static_file(self):
        """Serve static files from the current directory."""
        import os
        
        # Default to index.html for root path
        if self.path == '/':
            self.path = '/index.html'
        
        # Remove leading slash and serve file
        file_path = self.path[1:]
        
        if os.path.exists(file_path) and os.path.isfile(file_path):
            try:
                with open(file_path, 'rb') as f:
                    content = f.read()
                
                # Determine content type
                if file_path.endswith('.html'):
                    content_type = 'text/html'
                elif file_path.endswith('.js'):
                    content_type = 'application/javascript'
                elif file_path.endswith('.css'):
                    content_type = 'text/css'
                elif file_path.endswith('.json'):
                    content_type = 'application/json'
                else:
                    content_type = 'application/octet-stream'
                
                self.send_response(200)
                self.send_header('Content-Type', content_type)
                self.send_header('Content-Length', str(len(content)))
                self.end_headers()
                self.wfile.write(content)
                
            except Exception as e:
                self.send_error(500, f"Error serving file: {str(e)}")
        else:
            self.send_error(404, "File not found")

    def log_message(self, format, *args):
        """Override to reduce log noise."""
        pass

def run_server(port=8080):
    """Run the proxy server."""
    server_address = ('', port)
    httpd = HTTPServer(server_address, ProxyHandler)
    print(f"Proxy server running on http://localhost:{port}")
    print("Press Ctrl+C to stop the server")
    
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nShutting down server...")
        httpd.shutdown()

if __name__ == '__main__':
    run_server()
