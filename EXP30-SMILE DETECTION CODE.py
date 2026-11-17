import cv2
from tkinter import Tk, filedialog

# Select image from laptop
root = Tk()
root.withdraw()

file_path = filedialog.askopenfilename(
    title="Select an Image",
    filetypes=[("Image Files", "*.jpg *.jpeg *.png")]
)

# Read image
img = cv2.imread(file_path)

if img is None:
    print("Image not found")
    exit()

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Load cascades
face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)

smile_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_smile.xml"
)

# Detect face
faces = face_cascade.detectMultiScale(gray, 1.3, 5)

for (x, y, w, h) in faces:

    roi_gray = gray[y:y+h, x:x+w]

    smiles = smile_cascade.detectMultiScale(
        roi_gray, 1.7, 20, minSize=(25, 25)
    )

    for (sx, sy, sw, sh) in smiles:
        cv2.rectangle(
            img,
            (x+sx, y+sy),
            (x+sx+sw, y+sy+sh),
            (0, 255, 0), 3
        )

# Display output
cv2.imshow("Smile Detection", img)
cv2.imwrite("smile_output.jpg", img)

cv2.waitKey(0)
cv2.destroyAllWindows()
