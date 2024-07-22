import win32gui
import win32api
import win32con

# def encode_float_to_int(value):
#     return struct.unpack('I', struct.pack('f', value))[0]

def click_left(x,y):
    hWnd = win32gui.FindWindow(None,"test1")
    hWnd1= win32gui.FindWindowEx(hWnd, None, None, None)
    lParam = win32api.MAKELONG(1228, 266)

    win32gui.SendMessage(hWnd1, win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, lParam)
    win32gui.SendMessage(hWnd1, win32con.WM_LBUTTONUP, None, lParam)

hWnd = win32gui.FindWindow(None,"test1")
lParam = win32api.MAKELONG(1228, 286)
hWnd1= win32gui.FindWindowEx(hWnd, None, None, None)


win32gui.SendMessage(hWnd1, win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, lParam)
win32gui.SendMessage(hWnd1, win32con.WM_LBUTTONUP, None, lParam)



