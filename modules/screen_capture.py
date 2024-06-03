# modules/screen_capture.py

import pyautogui
from PIL import ImageGrab
from io import BytesIO
from ..encryption import encrypt_data

# Function to take screenshot
def take_screenshot():
    screenshot = pyautogui.screenshot()
    img_bytes = BytesIO()
    screenshot.save(img_bytes, format='PNG')
    img_data = img_bytes.getvalue()
    return img_data
