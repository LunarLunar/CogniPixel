@echo off
echo Starting CogniPixel Image Classifier...

echo.
echo [Step 1/2] Installing required Python libraries...

pip install -r requirements.txt

echo.
echo [Step 2/2] Launching the application...
echo Please wait for the browser tab to open automatically.

python app.py

pause
