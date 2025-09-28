#!/usr/bin/env python3
"""
Startup script for the OpenRouter Tools proxy server.
"""

import sys
import os
from proxy_server import run_server

def main():
    """Main function to start the server."""
    port = 8080
    
    # Check if port is specified as command line argument
    if len(sys.argv) > 1:
        try:
            port = int(sys.argv[1])
        except ValueError:
            print("Invalid port number. Using default port 8080.")
    
    print("Starting OpenRouter Tools Proxy Server...")
    print(f"Server will be available at: http://localhost:{port}")
    print("Make sure to use this URL instead of the GitHub Pages URL to avoid CORS issues.")
    print()
    
    run_server(port)

if __name__ == '__main__':
    main()
