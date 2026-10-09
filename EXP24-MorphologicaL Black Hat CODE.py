
import cv2
from tkinter import Tk, filedialog

Tk().withdraw()
path = filedialog.askopenfilename()
img = cv2.imread(path)

if img is not None:
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    circles = cv2.HoughCircles(
        gray, cv2.HOUGH_GRADIENT, 1.2, 50,
        param1=100, param2=40,
        minRadius=20, maxRadius=200)

    if circles is not None:
        for c in circles[0]:
            x, y, r = map(int, c)
            cv2.circle(img, (x, y), r, (0, 255, 0), 2)
            cv2.putText(img, "Possible Watch", (x-r, y-r),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.6,
                        (0, 0, 255), 2)

    cv2.imshow("Watch Detection", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Image not loaded!")

