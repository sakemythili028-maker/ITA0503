
import cv2
from tkinter import Tk, filedialog

Tk().withdraw()
path = filedialog.askopenfilename()

img = cv2.imread(path)

if img is not None:
    big = cv2.resize(img, (600, 600))
    small = cv2.resize(img, (200, 200))

    cv2.imshow("Original", img)
    cv2.imshow("Big Image", big)
    cv2.imshow("Small Image", small)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Image not loaded!")
