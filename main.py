import cv2
import time
from detector import detect

# ==========================
# Open Camera
# ==========================
cap = cv2.VideoCapture(0)

# Camera Resolution
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 320)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 240)

if not cap.isOpened():
    print("❌ Camera not found!")
    exit()

# FPS Counter
prev_time = time.time()

# ==========================
# Main Loop
# ==========================
while True:

    ret, frame = cap.read()

    if not ret:
        break

    # Mirror View
    frame = cv2.flip(frame, 1)

    # Face Detection
    frame = detect(frame)

    # FPS Calculation
    current_time = time.time()
    time_diff = current_time - prev_time
    fps = int(1 / time_diff) if time_diff > 0 else 0
    prev_time = current_time

    # Show FPS
    cv2.putText(
        frame,
        f"FPS: {fps}",
        (20, 35),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.8,
        (0, 255, 0),
        2,
        cv2.LINE_AA
    )

    # Show Window
    cv2.imshow("Age Gender Emotion Detection", frame)

    # Exit
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# ==========================
# Release Resources
# ==========================
cap.release()
cv2.destroyAllWindows()