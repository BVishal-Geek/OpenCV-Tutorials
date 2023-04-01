import cv2
import sys
video = cv2.VideoCapture(0)

if not video.isOpened():
    print("Cannot open camera, Must be occupied with different utility")
    exit()

while True:
    ret, frame = video.read()
    #boolean value is stored in ret 

    if not ret:
        print("Unable to capture frames")
    
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    #Coverting the RGB image to Gray Image
    cv2.imshow("Frame",frame)

    if cv2.waitKey(0) == ord('q'):
        sys.exit()

video.release()
cv2.destroyAllWindows()