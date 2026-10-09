import cv2
from tkinter import Tk, filedialog

root = Tk()
root.withdraw()

file = filedialog.askopenfilename()
img = cv2.imread(file)

kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5,5))
eroded = cv2.erode(img, kernel)

cv2.imshow("Original", img)
cv2.imshow("Eroded", eroded)

cv2.waitKey(0)
cv2.destroyAllWindows()
