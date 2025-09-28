@echo off
echo Setting OpenRouter API key and starting server...
echo.
echo Please replace 'your_actual_api_key_here' with your real OpenRouter API key
echo.
set OPENROUTER_API_KEY=your_actual_api_key_here
py -3.12 start_server.py
pause
