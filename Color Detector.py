import cv2
import numpy as np

image = 'white.jpg'

def get_avg_brightness(image):
    brightness = []
    # Scan through rows and columns
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            # Append the brightness value to the list
            brightness.append(image[i, j])
    # Return the average brightness value
    return np.mean(brightness)

# Color Detector comparing the average brightness of the three channels
def color_detector(image):
   frame = cv2.imread(image)
   b, g, r = cv2.split(frame)
   b_avg = get_avg_brightness(b)
   g_avg = get_avg_brightness(g)
   r_avg = get_avg_brightness(r)
   if b_avg > 200 and g_avg > 200 and r_avg > 200:
       return "W"
   elif b_avg > g_avg and b_avg > r_avg:
       return "B"
   elif g_avg > b_avg and g_avg > r_avg:
       return "G"
   elif r_avg > b_avg and r_avg > g_avg:
       return "R"
   else:
       return "W"


color = []
while True:
    color.append(color_detector(image))

    cv2.imshow("Image", cv2.imread(image))
    key = cv2.waitKey(100)

    # Change the image color
    if key == ord("b"):
        image = "blue.jpg"
    elif key == ord("g"):
        image = "green.png"
    elif key == ord("r"):
        image = "red.png"
    elif key == ord("w"):
        image = "white.jpg"

    if key == ord("q"):
        break
print(color)
color_list = []

# If 2 consecutive colors are the same, remove the second one
for item in color:
    if not color_list or color_list[-1] != item:
        color_list.append(item)

if color_list == ['W', 'R', 'W', 'G', 'W', 'B', 'W']:
    print("RGB")



