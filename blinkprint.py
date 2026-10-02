import cv2

# Laptop webcam-ah open pannum
camera = cv2.VideoCapture(0)

if not camera.isOpened():
    print("Webcam open aagala!")
    exit()

print("BlinkPrint started!")
print("Press Q to close.")

while True:
    success, frame = camera.read()

    if not success:
        print("Camera-la irundhu video varala.")
        break

    # Video-va mirror image-ah kaattum
    frame = cv2.flip(frame, 1)

    # Webcam video-va display pannum
    cv2.imshow("BlinkPrint", frame)

    # Q press panna stop aagum
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

camera.release()
cv2.destroyAllWindows()