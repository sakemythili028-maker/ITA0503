
import cv2
from tkinter import Tk, filedialog

Tk().withdraw()
path = filedialog.askopenfilename()
img = cv2.imread(path)

if img is not None:
    result = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
    cv2.imshow("Original Image", img)
    cv2.imshow("Rotated Image", result)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Image not loaded!")
