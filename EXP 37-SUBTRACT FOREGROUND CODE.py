
import cv2
import numpy as np
from tkinter import Tk, filedialog

def subtract_foreground(image_path):
    image = cv2.imread(image_path)

    if image is None:
        print("Image not found!")
        return

    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    lower = np.array([35, 40, 40])
    upper = np.array([85, 255, 255])

    mask = cv2.inRange(hsv, lower, upper)
    result = cv2.bitwise_and(image, image, mask=mask)

    cv2.imshow("Original Image", image)
    cv2.imshow("Foreground Extracted", result)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

root = Tk()
root.withdraw()

path = filedialog.askopenfilename(
    title="Select Image",
    filetypes=[("Images", "*.png *.jpg *.jpeg *.bmp")]
)

root.destroy()

if path:
    subtract_foreground(path)
else:
    print("No image selected!")
