
import cv2
import numpy as np
from tkinter import Tk, filedialog

Tk().withdraw()
path = filedialog.askopenfilename()
img = cv2.imread(path)

if img is not None:
    kernel = np.ones((5, 5), np.uint8)
    result = cv2.dilate(img, kernel, iterations=1)

    cv2.imshow("Original Image", img)
    cv2.imshow("Dilated Image", result)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Image not loaded!")
