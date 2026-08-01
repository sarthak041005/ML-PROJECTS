import cv2
import numpy as np
import random
import os

random.seed(42)

folders = [
    "dataset/images/train",
    "dataset/images/val",
    "dataset/images/test",
    "dataset/labels/train",
    "dataset/labels/val",
    "dataset/labels/test",
]

for f in folders:
    os.makedirs(f, exist_ok=True)

# ---------- Draw Functions ----------

def draw_nut(img, x, y, s):
    pts = np.array([
        [x-s,y],
        [x-s//2,y-s],
        [x+s//2,y-s],
        [x+s,y],
        [x+s//2,y+s],
        [x-s//2,y+s]
    ], np.int32)

    cv2.fillPoly(img,[pts],(150,150,150))
    cv2.circle(img,(x,y),s//3,(240,240,240),-1)

def draw_bolt(img,x,y,r):
    cv2.circle(img,(x,y),r,(120,120,120),-1)
    cv2.line(img,(x,y-r),(x,y+r),(90,90,90),3)
    cv2.circle(img,(x,y),r//3,(240,240,240),-1)

def draw_washer(img,x,y,r):
    cv2.circle(img,(x,y),r,(170,170,170),-1)
    cv2.circle(img,(x,y),r//2,(255,255,255),-1)

def draw_screw(img,x,y,l):
    cv2.rectangle(img,(x-5,y),(x+5,y+l),(120,120,120),-1)
    cv2.circle(img,(x,y),12,(150,150,150),-1)

# ---------- Generator ----------

def create(split,count):

    for i in range(count):

        img=np.full((640,640,3),240,dtype=np.uint8)

        labels=[]

        n=random.randint(8,15)

        for j in range(n):

            cls=random.randint(0,3)

            x=random.randint(60,580)
            y=random.randint(60,580)

            size=random.randint(20,40)

            if cls==0:
                draw_nut(img,x,y,size)

            elif cls==1:
                draw_bolt(img,x,y,size)

            elif cls==2:
                draw_washer(img,x,y,size)

            else:
                draw_screw(img,x,y,size)

            xmin=max(0,x-size)
            ymin=max(0,y-size)
            xmax=min(639,x+size)
            ymax=min(639,y+size)

            xc=((xmin+xmax)/2)/640
            yc=((ymin+ymax)/2)/640
            w=(xmax-xmin)/640
            h=(ymax-ymin)/640

            labels.append(f"{cls} {xc:.6f} {yc:.6f} {w:.6f} {h:.6f}")

        name=f"img_{i:04d}"

        cv2.imwrite(f"dataset/images/{split}/{name}.png",img)

        with open(f"dataset/labels/{split}/{name}.txt","w") as f:
            f.write("\n".join(labels))

create("train",120)
create("val",20)
create("test",20)

print("Dataset Generated Successfully")