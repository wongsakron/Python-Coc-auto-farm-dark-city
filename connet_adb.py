from ppadb.client import Client as AdbClient
from PIL import Image
import io
import os


#start adb
os.system('cmd /c "adb devices"')
# Connect to the ADB server
client = AdbClient(host="127.0.0.1", port=5037)
device = client.device("emulator-5554")
print("adb connet")

def screenshot():
        # Convert the raw screenshot to an image png to jpg
        raw_screenshot = device.screencap()
        image = Image.open(io.BytesIO(raw_screenshot))
        # Convert the image to RGB mode 
        image = image.convert('RGB')
        image.save("screenshot.jpg", "JPEG")

def touch(x,y):
    device.shell(f"input tap {x} {y}")
def swipe (start_x,start_y,end_x,end_y):
    device.shell(f"input swipe {start_x} {start_y} {end_x} {end_y} 100")

def zoomout():
    device(text="Settings").pinch.Out()
   



    
