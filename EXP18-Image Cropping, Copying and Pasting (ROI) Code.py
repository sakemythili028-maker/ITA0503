
import cv2
from tkinter import Tk, filedialog

Tk().withdraw()
path = filedialog.askopenfilename()
img = cv2.imread(path)

if img is not None:
    h, w = img.shape[:2]
    roi = img[h//4:3*h//4, w//4:3*w//4]
    result = img.copy()

    result[0:roi.shape[0], 0:roi.shape[1]] = roi

    cv2.imshow("Original Image", img)
    cv2.imshow("Cropped and Pasted ROI", result)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Image not loaded!")
