
import cv2
import numpy as np

# Function to create white image
def create_image():

    # Get image size from user
    width = int(input("Enter image width: "))
    height = int(input("Enter image height: "))

    # Create white image
    image = np.ones((height, width, 3), dtype=np.uint8) * 255

    # Calculate circle center
    center = (width // 2, height // 2)

    # Calculate radius
    radius = min(width, height) // 4

    # Draw circle
    cv2.circle(
        image,
        center,
        radius,
        (0, 0, 255),
        3
    )

    # Display output
    cv2.imshow("White Image with Circle", image)

    print("Press any key on image window to close.")

    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Call function
create_image()
