import cv2
from insightface.app import FaceAnalysis

# ==========================
# Load InsightFace Model
# ==========================
app = FaceAnalysis(
    name="buffalo_s",
    providers=["CPUExecutionProvider"]
)

app.prepare(
    ctx_id=0,
    det_size=(480, 480)
)


# ==========================
# Face Detection Function
# ==========================
def detect(frame):

    faces = app.get(frame)

    for face in faces:

        # Age & Gender
        age = int(face.age)
        gender = "Male" if face.gender == 1 else "Female"

        # Face Coordinates
        x1, y1, x2, y2 = face.bbox.astype(int)

        # Draw Face Rectangle
        cv2.rectangle(
            frame,
            (x1, y1),
            (x2, y2),
            (0, 255, 0),
            3
        )

        # Label
        label = f"{gender} | {age}"

        # Text Background
        (w, h), _ = cv2.getTextSize(
            label,
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7,
            2
        )

        cv2.rectangle(
            frame,
            (x1, y1 - h - 18),
            (x1 + w + 10, y1),
            (0, 255, 0),
            -1
        )

        # Show Text
        cv2.putText(
            frame,
            label,
            (x1 + 5, y1 - 7),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7,
            (0, 0, 0),
            2,
            cv2.LINE_AA
        )

    return frame