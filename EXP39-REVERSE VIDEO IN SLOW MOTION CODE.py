
import cv2
from tkinter import Tk, filedialog

def reverse_slow_motion(video_path):
    cap = cv2.VideoCapture(video_path)

    if not cap.isOpened():
        print("Cannot open video!")
        return

    frames = []

    while True:
        ret, frame = cap.read()
        if not ret:
            break
        frames.append(frame)

    cap.release()

    if not frames:
        print("No frames found!")
        return

    for frame in reversed(frames):
        cv2.imshow("Reverse Slow Motion", frame)

        if cv2.waitKey(100) & 0xFF == ord('q'):
            break

    cv2.destroyAllWindows()

root = Tk()
root.withdraw()

video_path = filedialog.askopenfilename(
    title="Select your video",
    filetypes=[("Video files", "*.mp4 *.avi *.mov *.mkv")]
)

root.destroy()

if video_path:
    reverse_slow_motion(video_path)
else:
    print("No video selected!")
