import cv2
from tkinter import Tk, filedialog
from detector import detect

# Hide Tkinter window
root = Tk()
root.withdraw()

# Open File Explorer
image_path = filedialog.askopenfilename(
    title="Select an Image",
    filetypes=[
        ("Image Files", "*.jpg *.jpeg *.png *.bmp"),
        ("All Files", "*.*")
    ]
)

if not image_path:
    print("❌ No image selected!")
    exit()

# Read Image
frame = cv2.imread(image_path)

if frame is None:
    print("❌ Unable to open image!")
    exit()

# Detect
frame = detect(frame)

# Show Result
cv2.imshow("Age Gender Detection", frame)

cv2.waitKey(0)
cv2.destroyAllWindows()