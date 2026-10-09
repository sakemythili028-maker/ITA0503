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

# Detect edges using Canny
edges = cv2.Canny(gray_image, 100, 200)

# Display original image
cv2.imshow("Original Image", image)

# Display outline
cv2.imshow("Canny Edge Image", edges)

# Wait for key press
cv2.waitKey(0)

# Close windows
cv2.destroyAllWindows()
