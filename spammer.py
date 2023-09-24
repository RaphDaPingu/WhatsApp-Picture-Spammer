from PIL import Image
import numpy
from io import BytesIO
import win32clipboard
import pyautogui
import time

WHATSAPP_MESSAGE_BOX_COORDINATES = (1200, 980)
IMAGE_SIZE_X = 2000
IMAGE_SIZE_Y = 2000
SPAM_COUNT = 10
SPAM_RATE = 2

pyautogui.click(WHATSAPP_MESSAGE_BOX_COORDINATES)

for i in range(SPAM_COUNT):
    imarray = numpy.random.rand(IMAGE_SIZE_X, IMAGE_SIZE_Y, 3) * 255
    image = Image.fromarray(imarray.astype("uint8")).convert("RGBA")
    
    output = BytesIO()
    image.convert("RGB").save(output, "BMP")
    data = output.getvalue()[14:]
    output.close()
    
    win32clipboard.OpenClipboard()
    win32clipboard.EmptyClipboard()
    win32clipboard.SetClipboardData(win32clipboard.CF_DIB, data)
    win32clipboard.CloseClipboard()
    
    pyautogui.hotkey("ctrlleft", "v")
    time.sleep(SPAM_RATE)
    pyautogui.hotkey("enter")
