
import cv2
from tkinter import Tk, filedialog

# Select input image
root = Tk()
root.withdraw()

path = filedialog.askopenfilename(
    title="Select Image",
    filetypes=[("Image Files", "*.jpg *.jpeg *.png")]
)

# Read image
img = cv2.imread(path)

if img is None:
    print("Image not found")
    exit()

# Convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Load face cascade
face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades +
    "haarcascade_frontalface_default.xml"
)

# Detect faces
faces = face_cascade.detectMultiScale(
    gray, 1.1, 5
)

# Count faces
count = len(faces)

# Draw rectangles
for (x, y, w, h) in faces:
    cv2.rectangle(
        img, (x, y), (x+w, y+h),
        (0, 255, 0), 3
    )

# Display count
print("Number of faces detected:", count)

# Show output
cv2.imshow("Face Count", img)
cv2.imwrite("face_count_output.jpg", img)

cv2.waitKey(0)
cv2.destroyAllWindows()
