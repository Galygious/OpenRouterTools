# PowerShell script to start the OpenRouter Tools server with API key
Write-Host "Setting OpenRouter API key and starting server..." -ForegroundColor Green
Write-Host ""
Write-Host "Please replace 'your_actual_api_key_here' with your real OpenRouter API key" -ForegroundColor Yellow
Write-Host ""

# Set the environment variable
$env:OPENROUTER_API_KEY = "your_actual_api_key_here"

# Start the server
py -3.12 start_server.py

# Keep the window open
Read-Host "Press Enter to exit"
