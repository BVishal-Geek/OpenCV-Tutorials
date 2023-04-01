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
        sys.exit() #It waits until the q is pressed to shutdown the camera


video.release() #release the camera to set it free, so all other applications can use it
cv2.destroyAllWindows() #Destroying all teh windows created by CV, so that there is no obstruction for other applications to use it 
