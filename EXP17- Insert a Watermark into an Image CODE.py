
import cv2
from tkinter import Tk, filedialog

Tk().withdraw()
path = filedialog.askopenfilename()
img = cv2.imread(path)

if img is not None:
    result = img.copy()
    cv2.putText(result, "MY WATERMARK", (20, 50),
                cv2.FONT_HERSHEY_SIMPLEX, 1,
                (0, 0, 255), 2)

    cv2.imshow("Watermarked Image", result)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Image not loaded")
