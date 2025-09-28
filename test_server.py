#!/usr/bin/env python3
"""
Test script to check if the proxy server is working correctly.
"""

import urllib.request
import json
import time

def test_server():
    """Test the proxy server endpoints."""
    base_url = "http://localhost:8080"
    
    print("Testing proxy server...")
    
    # Test 1: Check if server is running
    try:
        response = urllib.request.urlopen(f"{base_url}/")
        print("[OK] Server is running")
    except Exception as e:
        print(f"[ERROR] Server not running: {e}")
        return
    
    # Test 2: Test API endpoint
    try:
        print("Testing /api/frontend/models endpoint...")
        response = urllib.request.urlopen(f"{base_url}/api/frontend/models")
        data = response.read()
        
        # Try to parse as JSON
        try:
            json_data = json.loads(data.decode('utf-8'))
            print(f"[OK] API endpoint working - got {len(json_data.get('data', []))} models")
            print(f"First model: {json_data.get('data', [{}])[0].get('name', 'Unknown')}")
        except json.JSONDecodeError as e:
            print(f"[ERROR] Invalid JSON response: {e}")
            print(f"Response preview: {data[:200]}...")
        except Exception as e:
            print(f"[ERROR] Error parsing response: {e}")
            
    except Exception as e:
        print(f"[ERROR] API endpoint failed: {e}")

if __name__ == '__main__':
    test_server()
