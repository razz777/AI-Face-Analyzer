import cv2
from tkinter import Tk, filedialog
from detector import detect

# Hide Tkinter window
root = Tk()
root.withdraw()

# Open File Explorer
video_path = filedialog.askopenfilename(
    title="Select a Video",
    filetypes=[
        ("Video Files", "*.mp4 *.avi *.mov *.mkv"),
        ("All Files", "*.*")
    ]
)

if not video_path:
    print("❌ No video selected!")
    exit()

# Open Video
cap = cv2.VideoCapture(video_path)

if not cap.isOpened():
    print("❌ Unable to open video!")
    exit()

while True:
    ret, frame = cap.read()

    if not ret:
        break

    frame = detect(frame)

    cv2.imshow("Video Detection", frame)

    # Press Q to exit
    if cv2.waitKey(25) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()