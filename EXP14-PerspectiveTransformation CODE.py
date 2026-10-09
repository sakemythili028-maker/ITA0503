
import cv2
import numpy as np
from tkinter import Tk, filedialog

Tk().withdraw()
path = filedialog.askopenfilename()
img = cv2.imread(path)

if img is not None:
    h, w = img.shape[:2]
    src = np.float32([[0, 0], [w-1, 0],
                      [0, h-1], [w-1, h-1]])
    dst = np.float32([[50, 50], [w-50, 0],
                      [0, h-50], [w-1, h-1]])

    M = cv2.getPerspectiveTransform(src, dst)
    result = cv2.warpPerspective(img, M, (w, h))

    cv2.imshow("Perspective Transformation", result)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Image not loaded!")
