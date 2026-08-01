import cv2
import numpy as np
import random
import os

os.makedirs("images", exist_ok=True)
os.makedirs("masks", exist_ok=True)

for i in range(20):

    img = np.zeros((512,512,3),dtype=np.uint8)
    mask = np.zeros((512,512),dtype=np.uint8)

    for j in range(random.randint(3,6)):

        x = random.randint(60,450)
        y = random.randint(60,450)
        r = random.randint(30,70)

        color = (
            random.randint(80,255),
            random.randint(80,255),
            random.randint(80,255)
        )

        cv2.circle(img,(x,y),r,color,-1)
        cv2.circle(mask,(x,y),r,255,-1)

    cv2.imwrite(f"images/image{i}.png",img)
    cv2.imwrite(f"masks/image{i}_mask.png",mask)

print("Dataset Created")