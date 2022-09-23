from re import X
import cv2
import numpy as np
import csv
print("hi")


def sol(namesorce,nametarget):
    lastinfor=[]
    with open(".\\sideinfodeci\\"+namesorce+nametarget+".txt") as f:
        for i in f.readlines():
            lastinfor.append(float(i))

    coltra_img = cv2.imread(".\\coltra\\"+namesorce+nametarget+".png")
    print(len(coltra_img))
    print(len(coltra_img[0]))
    revsct=[]
    print(lastinfor)

    for i in range(len(coltra_img)):
        revsct.append([])
        for j in range(len(coltra_img[0])):
            revsct[i].append([])
            #print(revsct[i])
            revsct[i][j].append(((coltra_img[i][j][0]-lastinfor[8])*lastinfor[5]/lastinfor[11]+lastinfor[2]))
            revsct[i][j].append(((coltra_img[i][j][1]-lastinfor[7])*lastinfor[4]/lastinfor[10])+lastinfor[1])
            revsct[i][j].append(((coltra_img[i][j][2]-lastinfor[6])*lastinfor[3]/lastinfor[9])+lastinfor[0])
    #print(revsct)
    revsct_img=np.array(revsct)
    cv2.imwrite(".\\revsct\\"+namesorce+".png",revsct_img)
    print()

if __name__ == "__main__":
    sol("01_kodim05_","kodim06")
    sol("02_kodim07_","kodim08")
    sol("03_kodim09_","kodim10")