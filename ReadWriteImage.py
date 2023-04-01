import cv2 
import sys  

img = cv2.imread(cv2.samples.findFile(r"apple.jpg"))
path = cv2.samples.findFile(r"apple.jpg")
print(path)
if img is None:
    sys.exit("Image is not present")

cv2.imshow("Window", img)
k = cv2.waitKey(0)

if k == ord("s"):
    cv2.imwrite("Apple.png",img)