
import cv2

def reverse_video(input_video_path, output_video_path):

    # Open the input video
    cap = cv2.VideoCapture(input_video_path)

    if not cap.isOpened():
        print("Cannot open video. Check the file name.")
        return

    # Get video properties
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = cap.get(cv2.CAP_PROP_FPS)

    if fps <= 0:
        fps = 25

    # Read all frames
    frames = []

    while True:
        ret, frame = cap.read()

        if not ret:
            break

        frames.append(frame)

    cap.release()

    # Check whether frames were read
    if len(frames) == 0:
        print("No frames found in the video.")
        return

    # Reverse the frames
    frames.reverse()

    # Create output video
    fourcc = cv2.VideoWriter_fourcc(*"mp4v")

    out = cv2.VideoWriter(
        output_video_path,
        fourcc,
        fps,
        (width, height)
    )

    # Write reversed frames
    for frame in frames:
        out.write(frame)

    out.release()

    print("Reversed video saved successfully!")
    print("Output file:", output_video_path)


# Example usage: use your actual input filename
reverse_video(
    "input_video.mp4.mp4",
    "output_reversed.mp4"
)
