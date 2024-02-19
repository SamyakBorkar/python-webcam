import cv2

url = 'http://192.168.137.218:8080/video'  

cap = cv2.VideoCapture(url)

if not cap.isOpened():
    print("Error: Could not open camera.")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        print("Error: Failed to receive frame.")
        break

    cv2.imshow('Mobile Camera Feed', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
