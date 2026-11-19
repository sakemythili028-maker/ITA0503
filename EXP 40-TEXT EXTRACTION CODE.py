
import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

video = cv2.VideoCapture("input.mp4")

while True:
    ret, frame = video.read()

    if not ret:
        break

    text = pytesseract.image_to_string(frame)

    if text.strip():
        print("Extracted Text:")
        print(text)

    cv2.imshow("Video", frame)

    if cv2.waitKey(100) & 0xFF == ord('q'):
        break

video.release()
cv2.destroyAllWindows()
