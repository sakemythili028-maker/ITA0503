
import cv2
from tkinter import Tk, filedialog

# Open a window to select your image
root = Tk()
root.withdraw()

image_path = filedialog.askopenfilename(
    title="Select your sample image",
    filetypes=[("Image files", "*.png *.jpg *.jpeg")]
)

root.destroy()

if not image_path:
    print("No image selected.")
else:
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    if image is None:
        print("Unable to read the image.")
    else:
        threshold_value = 127

        _, segmented_image = cv2.threshold(
            image, threshold_value, 255, cv2.THRESH_BINARY
        )

        cv2.imshow("Original Image", image)
        cv2.imshow("Segmented Image", segmented_image)

        cv2.waitKey(0)
        cv2.destroyAllWindows()
