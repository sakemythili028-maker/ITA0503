
import cv2
from tkinter import Tk, filedialog

Tk().withdraw()
path = filedialog.askopenfilename()
img = cv2.imread(path)

if img is not None:
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    x = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=3)
    y = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=3)

    result = cv2.convertScaleAbs(cv2.addWeighted(
        cv2.convertScaleAbs(x), 0.5,
        cv2.convertScaleAbs(y), 0.5, 0))

    cv2.imshow("Original Image", img)
    cv2.imshow("Sobel Image", result)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Image not loaded!")

