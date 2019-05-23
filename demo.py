from align import *
import os
import cv2

for parent,dirnames,filenames in os.walk("./data"):
    for filename in filenames:
        if filename.endswith(".png") or filename.endswith(".jpg"):
            path = os.path.join(parent,filename);
            img = cv2.imread(path)
            
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            skew_h, skew_v = skew_detect(gray)
            corr_img = v_rot(img, (90 - skew_v + skew_h), img.shape, 60);
            corr_img = h_rot(corr_img, skew_h)
            
            cv2.imwrite(os.path.join("./result",filename), corr_img)
            cv2.imshow("origin",img)
            cv2.imshow("corr",corr_img)
            cv2.waitKey(0)
