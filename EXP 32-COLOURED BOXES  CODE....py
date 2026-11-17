import cv2
import numpy as np
def colored_boxes():
    w = int(input("Enter image width: "))
    h = int(input("Enter image height: "))
    img = np.ones((h, w, 3), dtype=np.uint8) * 255
    bw = w // 10
    bh = h // 10
    img[0:bh, 0:bw] = (0, 0, 0)
    img[0:bh, w-bw:w] = (255, 0, 0)
    img[h-bh:h, 0:bw] = (0, 255, 0)
    img[h-bh:h, w-bw:w] = (0, 0, 255)
    print("Image created successfully")
    cv2.imshow("Colored Boxes", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
colored_boxes()
