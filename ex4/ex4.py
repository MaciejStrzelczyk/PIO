import numpy as np
import cv2
import os

pictures = os.listdir("furnitures/table")


for i in range(0, len(pictures)):

    img = cv2.imread("furnitures/table/" + pictures[i],1)

    img_inter = cv2.resize(img, (256, 256), interpolation=cv2.INTER_NEAREST)

    cv2.imwrite("furnitures2/table2/table" + str(i+1) +'.jpg', img_inter)

if __name__ == '__main__':
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
    cv2.imshow('Nearest Interpolated Image', img_inter)