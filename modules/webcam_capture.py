# modules/webcam_capture.py

import cv2
from io import BytesIO
import numpy as np
from ..encryption import encrypt_data

# Function to capture image from webcam
def capture():
    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()
    cap.release()
    cv2.destroyAllWindows()

    img_bytes = BytesIO()
    np.savez_compressed(img_bytes, frame)
    img_data = img_bytes.getvalue()
    return img_data
