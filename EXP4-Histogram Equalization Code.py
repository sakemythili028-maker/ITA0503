import cv2
from tkinter import Tk, filedialog

root = Tk()
root.withdraw()

file = filedialog.askopenfilename()

img = cv2.imread(file)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

equalized = cv2.equalizeHist(gray)

cv2.imshow("Original", gray)
cv2.imshow("Equalized", equalized)

cv2.waitKey(0)
cv2.destroyAllWindows()
