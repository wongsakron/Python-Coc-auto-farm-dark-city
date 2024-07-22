import cv2
import numpy as np
import matplotlib.pyplot as plt
import time
import connet_adb


def detect(img_coc:str) :
    connet_adb.screenshot()
    main_image_path = 'screenshot.jpg'
    template_image_path = f'imge/{img_coc}.jpg'

    main_image = cv2.imread(main_image_path, cv2.IMREAD_COLOR)
    template = cv2.imread(template_image_path, cv2.IMREAD_COLOR)

    # Convert images to grayscale
    main_gray = cv2.cvtColor(main_image, cv2.COLOR_BGR2GRAY)
    template_gray = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)

    # Get the width and height of the template
    w, h = template_gray.shape[::-1]
    # Perform template matching
    res = cv2.matchTemplate(main_gray, template_gray, cv2.TM_CCOEFF_NORMED)

    # Set a threshold for matching
    threshold = 0.8
    loc = np.where(res >= threshold)
    # Initialize list to store the center positions
    positions = []
    # Draw rectangles around matched regions and store the center positions
    for pt in zip(*loc[::-1]):
        # Calculate the center of the rectangle
        center_x = pt[0] + w // 2
        center_y = pt[1] + h // 2
        positions.append((center_x, center_y))
        # Draw the rectangle on the main image
        cv2.rectangle(main_image, pt, (pt[0] + w, pt[1] + h), (0, 255, 0), 2)
    return positions
        
def coc_funtion(count:int,step:int):
    for round in range(1,count+1):
        print("round : ",round)
        img_coc = ["attack","search","hero","give_up","accept","to_home"]
        error = 0
        index = 0
      
        while error <= 5:
            img = img_coc[index]
            print(img)
            try:
                x,y  = detect(img)[0]
                connet_adb.touch(x=x,y=y)
                if img == "to_home":
                    break
                if img == "hero":
                    connet_adb.swipe(877,526,1713,526)
                    connet_adb.swipe(1713,526,1713,1200)
                    time.sleep(0.5)
                    x,y = 1428,421
                    connet_adb.touch(x=x,y=y)
                error = 0
                index += 1
                time.sleep(0.5)
            except:
                error += 1
                time.sleep(2)
                print("wait"+"."*error)
        if round % step == 0:
            time.sleep(5)
            connet_adb.swipe(1228,383,881,609)
            time.sleep(1)
            for i in ["give_1","give_2","give_3"]:
                try:
                    x,y=detect(i)[0]
                    connet_adb.touch(x=x,y=y)
                    time.sleep(1)
                    for get in ["get","coles"]:
                        x,y=detect(get)[0]
                        connet_adb.touch(x=x,y=y)
                        time.sleep(1)
                    break
                except:
                    pass
       
            

coc_funtion(90,5)