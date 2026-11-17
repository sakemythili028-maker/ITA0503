import cv2
from tkinter import Tk, filedialog

# Select image from laptop
root = Tk()
root.withdraw()

file_path = filedialog.askopenfilename(
    title="Select an Image",
    filetypes=[("Image Files", "*.jpg *.jpeg *.png")]
)

# Read selected image
img = cv2.imread(file_path)

if img is None:
    print("Image not found")
    exit()

# Convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Load eye detector
eye_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_eye.xml"
)

# Detect eyes
eyes = eye_cascade.detectMultiScale(
    gray, 1.1, 8
)

# Draw blue boxes
for (x, y, w, h) in eyes:
    cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 3)

# Show output
cv2.imshow("Eye Detection", img)
cv2.imwrite("eye_output.jpg", img)

cv2.waitKey(0)
cv2.destroyAllWindows()
