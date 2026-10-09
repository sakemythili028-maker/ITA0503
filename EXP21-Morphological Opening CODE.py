import cv2
import numpy as np
from tkinter import Tk, filedialog

Tk().withdraw()
path = filedialog.askopenfilename()
img = cv2.imread(path)

if img is not None:
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    kernel = np.ones((5, 5), np.uint8)
    result = cv2.morphologyEx(gray, cv2.MORPH_OPEN, kernel)

    cv2.imshow("Original", gray)
    cv2.imshow("Opening", result)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Image not loaded!")
