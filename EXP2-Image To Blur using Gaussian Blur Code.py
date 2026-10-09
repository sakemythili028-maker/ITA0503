import cv2
from tkinter import Tk, filedialog

# Select the image
root = Tk()
root.withdraw()

file_path = filedialog.askopenfilename(
    title="Select Image",
    filetypes=[("Image Files", "*.jpg *.jpeg *.png")]
)

# Read the image
image = cv2.imread(file_path)

# Apply Gaussian Blur
blur_image = cv2.GaussianBlur(image, (15, 15), 0)

# Display original image
cv2.imshow("Original Image", image)

# Display blurred image
cv2.imshow("Gaussian Blur Image", blur_image)

# Wait for key press
cv2.waitKey(0)

# Close windows
cv2.destroyAllWindows()
