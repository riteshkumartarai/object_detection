import cv2

# Set the camera index for the external camera (usually 1 or higher)
camera_index = 1

# Open the video capture with the specified camera index
cap = cv2.VideoCapture(camera_index)

if not cap.isOpened():
    print("Error: Could not open camera.")
    exit()

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    # If the frame was not captured correctly, break the loop
    if not ret:
        print("Error: Failed to capture frame.")
        break

    # Display the resulting frame
    cv2.imshow('External Camera Feed', frame)

    # Press 'q' to exit the video
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture and close the window
cap.release()
cv2.destroyAllWindows()
