import cv2
from tkinter import Tk, filedialog
import matplotlib.pyplot as plt

def histogram(img):
    for i, color in enumerate(['b', 'g', 'r']):
        hist = cv2.calcHist([img], [i], None, [256], [0, 256])
        plt.plot(hist)

root = Tk()
root.withdraw()

file = filedialog.askopenfilename()
img = cv2.imread(file)

histogram(img)

plt.title("Color Histogram")
plt.xlabel("Color Levels")
plt.ylabel("Frequency")
plt.show()
