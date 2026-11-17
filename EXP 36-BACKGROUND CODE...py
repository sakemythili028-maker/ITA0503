
import cv2
import numpy as np

def subtract_background(C:\Users\sakem\Downloads\image_experiments\sample.png):
    # Read image
    image = cv2.imread(image_path)

    if image is None:
        print("Image not found! Check the file name.")
        return

    # Convert to HSV
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    # Green background color range
    lower_color = np.array([35, 40, 40])
    upper_color = np.array([85, 255, 255])

    # Detect green background
    mask = cv2.inRange(hsv, lower_color, upper_color)

    # Remove background
    mask_inv = cv2.bitwise_not(mask)
    foreground = cv2.bitwise_and(
        image, image, mask=mask_inv
    )

    # Display output
    cv2.imshow("Original Image", image)
    cv2.imshow("Background Removed", foreground)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

subtract_background("image.jpg")
