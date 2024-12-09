import cv2
import numpy as np

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

   if b_avg > g_avg and b_avg > r_avg:
       print("Blue")
   elif g_avg > b_avg and g_avg > r_avg:
       print("Green")
   else:
       print("Red")

color_detector("blue0517-4dfc85cb0200460ab717b101ac07888f.jpg")
color_detector("Solid_red.svg.png")
color_detector("Flag_of_Libya_(1977–2011).svg.png")



