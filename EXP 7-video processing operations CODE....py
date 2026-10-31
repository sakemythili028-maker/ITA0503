
import cv2
import os

video_path = r"C:\Users\sakem\Downloads\OPENCV_LAB\EXP7\video.mp4..mp4"

print("Checking video path...")
print("File exists:", os.path.exists(video_path))

cap = cv2.VideoCapture(video_path)

if not cap.isOpened():
    print("Video not found!")
else:
    print("Video opened successfully!")

    fps = cap.get(cv2.CAP_PROP_FPS)
    print("Video FPS:", fps)

    for delay, title in [
        (30, "Normal Speed"),
        (100, "Slow Motion"),
        (1, "Fast Motion")
    ]:
        cap.set(cv2.CAP_PROP_POS_FRAMES, 0)

        while True:
            ret, frame = cap.read()
            if not ret:
                break

            cv2.imshow(title, frame)

            if cv2.waitKey(delay) & 0xFF == ord('q'):
                break

        cv2.destroyAllWindows()

    cap.release()

print("Finished")
