# OpenRouter Tools

A web dashboard for exploring OpenRouter models and their performance statistics.

## Features

- Browse available models from OpenRouter
- View performance statistics (latency, throughput) for each model
- Automatically selects the fastest provider based on combined latency and throughput rankings
- Chat interface with model selection
- Real-time pricing information

## Setup

### Option 1: Using the Proxy Server (Recommended)

The proxy server bypasses CORS restrictions and allows the dashboard to work properly.

#### Method A: Set API Key as Environment Variable (Recommended)

1. **Set your OpenRouter API key as an environment variable:**
   ```bash
   # Windows (PowerShell)
   $env:OPENROUTER_API_KEY="your_api_key_here"
   
   # Windows (Command Prompt)
   set OPENROUTER_API_KEY=your_api_key_here
   
   # Linux/Mac
   export OPENROUTER_API_KEY="your_api_key_here"
   ```

2. **Start the proxy server:**
   ```bash
   py -3.12 start_server.py
   ```
   Or specify a custom port:
   ```bash
   py -3.12 start_server.py 3000
   ```

3. **Open your browser and go to:**
   ```
   http://localhost:8080
   ```

#### Method B: Enter API Key in Browser

1. **Start the proxy server:**
   ```bash
   py -3.12 start_server.py
   ```

2. **Open your browser and go to:**
   ```
   http://localhost:8080
   ```

3. **Enter your OpenRouter API key** in the input field and click "Save Key"

### Option 2: Direct File Access (Limited)

You can also open `index.html` directly in your browser, but this will have CORS limitations when trying to fetch data from OpenRouter APIs.

## How It Works

1. **Models Endpoint**: Fetches all available models from OpenRouter's `/frontend/models` API
2. **Stats Endpoint**: For each model, fetches provider statistics from `/frontend/stats/endpoint`
3. **Fastest Provider Selection**: Calculates average ranking of latency and throughput performance
4. **Display**: Shows the fastest provider's statistics in the dashboard

## API Key

You'll need an OpenRouter API key to use this tool. Get one from [OpenRouter](https://openrouter.ai/).

## Troubleshooting

- **CORS Errors**: Make sure you're using the proxy server (localhost:8080) instead of opening the HTML file directly
- **API Key Issues**: Ensure your OpenRouter API key is valid and has sufficient credits
- **No Data**: Some models may not have statistics available

## Files

- `index.html` - Main dashboard interface
- `app.min.js` - JavaScript functionality
- `proxy_server.py` - Python proxy server to handle API requests
- `start_server.py` - Startup script for the proxy server
