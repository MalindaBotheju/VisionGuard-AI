import cv2
from ultralytics import YOLO

# 1. Load the AI Model
# 'yolov8n.pt' is the "Nano" version. It is super fast and lightweight.
# It will download automatically the first time you run this.
model = YOLO('yolov8n.pt')

# 2. Open the Webcam (0 is usually the default camera)
cap = cv2.VideoCapture(0)

# Check if camera opened successfully
if not cap.isOpened():
    print("Error: Could not open webcam.")
    exit()

print("press 'q' to quit the video feed")

while True:
    # 3. Read a frame from the camera
    ret, frame = cap.read()
    if not ret:
        print("Error: Failed to capture image.")
        break

    # 4. Run AI Inference on the frame
    # This detects objects and draws the boxes automatically
    results = model(frame)
    
    # 5. Visualize the results
    # 'plot()' draws the bounding boxes and labels on the image
    annotated_frame = results[0].plot()

    # 6. Show the video on screen
    cv2.imshow("VisionGuard AI - Real-Time Detection", annotated_frame)

    # 7. Press 'q' to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Cleanup
cap.release()
cv2.destroyAllWindows()
