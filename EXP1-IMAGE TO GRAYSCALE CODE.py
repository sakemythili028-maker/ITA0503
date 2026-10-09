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

# Convert to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Display images
cv2.imshow("Original Image", image)
cv2.imshow("Grayscale Image", gray_image)

# Wait for key press
cv2.waitKey(0)

# Close windows
cv2.destroyAllWindows()
