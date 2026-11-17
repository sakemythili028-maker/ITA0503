
import cv2
import tkinter as tk
from tkinter import filedialog

# Select the video file
root = tk.Tk()
root.withdraw()

video_path = filedialog.askopenfilename(
    title="Select Traffic Video",
    filetypes=[("Video Files", "*.mp4 *.avi *.mov")]
)

# Read video
cap = cv2.VideoCapture(video_path)

if not cap.isOpened():
    print("Error: Video not found!")
    exit()

# Create background subtractor
bg_subtractor = cv2.createBackgroundSubtractorMOG2(
    history=500,
    varThreshold=50,
    detectShadows=True
)

while True:
    ret, frame = cap.read()

    if not ret:
        break

    # Resize frame
    frame = cv2.resize(frame, (800, 450))

    # Apply background subtraction
    mask = bg_subtractor.apply(frame)

    # Remove shadows
    _, mask = cv2.threshold(mask, 200, 255, cv2.THRESH_BINARY)

    # Remove noise
    kernel = cv2.getStructuringElement(
        cv2.MORPH_RECT, (5, 5)
    )
    mask = cv2.morphologyEx(
        mask, cv2.MORPH_OPEN, kernel
    )
    mask = cv2.dilate(mask, kernel, iterations=2)

    # Find vehicle contours
    contours, hierarchy = cv2.findContours(
        mask,
        cv2.RETR_EXTERNAL,
        cv2.CHAIN_APPROX_SIMPLE
    )

    count = 0

    for contour in contours:
        area = cv2.contourArea(contour)

        if area > 900:
            x, y, w, h = cv2.boundingRect(contour)

            # Draw rectangle
            cv2.rectangle(
                frame, (x, y), (x+w, y+h),
                (0, 255, 0), 2
            )

            # Display label
            cv2.putText(
                frame, "Vehicle",
                (x, y-10),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.6, (0, 0, 255), 2
            )

            count += 1

    # Display vehicle count
    cv2.putText(
        frame, "Vehicles: " + str(count),
        (20, 40),
        cv2.FONT_HERSHEY_SIMPLEX,
        1, (255, 0, 0), 2
    )

    # Display output
    cv2.imshow("Vehicle Detection", frame)
    cv2.imshow("Foreground Mask", mask)

    # Press Q to stop
    if cv2.waitKey(30) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()

print("Vehicle Detection Completed!")
