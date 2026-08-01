import cv2
import numpy as np
import os
import random

os.makedirs("images", exist_ok=True)

for i in range(20):

    img = np.ones((700,900,3), dtype=np.uint8)*255

    # Draw bolts (circles)
    for j in range(random.randint(10,20)):
        x = random.randint(40,850)
        y = random.randint(40,650)
        r = random.randint(15,25)

        cv2.circle(img,(x,y),r,(80,80,80),-1)
        cv2.circle(img,(x,y),r//2,(255,255,255),-1)

    # Draw nuts (hexagons)
    for j in range(random.randint(8,15)):

        x = random.randint(40,850)
        y = random.randint(40,650)
        s = random.randint(15,25)

        pts=np.array([
            [x-s,y],
            [x-s//2,y-s],
            [x+s//2,y-s],
            [x+s,y],
            [x+s//2,y+s],
            [x-s//2,y+s]
        ])

        cv2.fillPoly(img,[pts],(120,120,120))

    cv2.imwrite(f"images/img_{i+1}.png",img)

print("Dataset Generated")