
import cv2
import numpy as np

def create_image():

    width = int(input("Enter image width: "))
    height = int(input("Enter image height: "))

    # Create white image
    image = np.full((height, width, 3), 255, dtype=np.uint8)

    # Draw rectangle
    cv2.rectangle(
        image,
        (50, 50),
        (width - 50, height - 50),
        (0, 0, 255),
        3
    )

    # Display image
    cv2.namedWindow("Output", cv2.WINDOW_NORMAL)
    cv2.imshow("Output", image)

    print("Press any key on the image window to close.")

    cv2.waitKey(0)
    cv2.destroyAllWindows()

create_image()
