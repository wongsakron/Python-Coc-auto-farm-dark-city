import cv2
import numpy as np
import matplotlib.pyplot as plt
import connet_adb


connet_adb.screenshot()
main_image_path = 'screenshot.jpg'
template_image_path = f'imge/give_1.jpg'

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



            
          
        
# Display the positions in the console
for i, (x, y) in enumerate(positions):
    print(f"Match {i+1}: Center Position (Width, Height) = ({x}, {y})")

# Display the result
plt.figure(figsize=(10, 6))
plt.imshow(cv2.cvtColor(main_image , cv2.COLOR_BGR2RGB))
plt.title('Detected Template Matches')
plt.show()

    

