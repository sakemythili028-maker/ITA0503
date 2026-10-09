
import cv2
import numpy as np
from tkinter import Tk, filedialog

Tk().withdraw()
path = filedialog.askopenfilename()
img = cv2.imread(path)

if img is not None:
    h, w = img.shape[:2]
    src = np.float32([[0, 0], [w-1, 0], [0, h-1]])
    dst = np.float32([[50, 50], [w-50, 0], [50, h-50]])

    M = cv2.getAffineTransform(src, dst)
    result = cv2.warpAffine(img, M, (w, h))

    cv2.imshow("Affine Transformation", result)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Image not loaded!")

