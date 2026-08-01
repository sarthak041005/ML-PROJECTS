import cv2
import os

os.makedirs("predictions",exist_ok=True)

for file in os.listdir("images"):

    img=cv2.imread("images/"+file)

    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    blur=cv2.GaussianBlur(gray,(5,5),0)

    _,pred=cv2.threshold(
        blur,
        40,
        255,
        cv2.THRESH_BINARY
    )

    cv2.imwrite("predictions/"+file,pred)

print("Segmentation Completed")