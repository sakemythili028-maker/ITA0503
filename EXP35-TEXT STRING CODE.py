
import cv2
from tkinter import Tk, filedialog

def add_text(image_path):
    image = cv2.imread(image_path)

    if image is None:
        print("Image not found!")
        return

    text = input("Enter text: ")

    cv2.putText(
        image, text, (50, 50),
        cv2.FONT_HERSHEY_SIMPLEX,
        1, (0, 255, 0), 2
    )

    cv2.imshow("Text on Image", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

root = Tk()
root.withdraw()

path = filedialog.askopenfilename(
    title="Select Image",
    filetypes=[("Images", "*.jpg *.png *.jpeg")]
)

root.destroy()

if path:
    add_text(path)
else:
    print("No image selected!")
