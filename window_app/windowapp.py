import pygetwindow as gw
# import pyautogui
# import time

def list_open_windows():
    windows = gw.getAllTitles()
    print("Open windows:")
    for window in windows:
        print(f'"{window}"')

# list_open_windows()

# def window_detecd(x_p,y_p):
def window_detecd():
# Define the window title you want to target
    window_title = "test1"

    # Find the window by its title
    window = None
    for w in gw.getWindowsWithTitle(window_title):
        if w.title == window_title:
            window = w
            break

    if window is None:
        print(f"Window titled '{window_title}' not found!")
    else:
        # Bring the window to the front
        # window.activate() #get position app window mode .exe
        left , top , right , bottom= window.left,window.top,window.right,window.bottom
        print(left , top , right , bottom)
        display_x=1920;display_y=1080 #my pc display  screen
        x_p,y_p = 100,200 # position target

        # *if app window_mode full screen = 1920x1080 
        x = (display_x - (left + (display_x - right ))) / display_x 
        y = (display_y - (top + (display_y - bottom))) / display_y 
         
         #result position target in window app
        result_x = (x_p * x) + left 
        result_y = (y_p * y) + top 

       
       
        return result_x,result_y
    
window_detecd()
