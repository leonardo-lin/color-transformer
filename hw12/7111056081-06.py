print("start")
import numpy as np
import cv2
import os
import random
import math



def sol(source_pic,enc_pic,dec_pic):
    answer=[]
    source_img = cv2.imread(source_pic)
    M=len(source_img)
    N=len(source_img[0])
    print(type(source_img[0]))
    K=24
    print(M,N,K)
    bz=2
    rz=14
    cz=int((rz*M)/math.gcd(M,N))
    bx=6
    rx=18
    cx=int((rx*M)/math.gcd(M,N))
    by=10
    ry=12
    cy=int((ry*M)/math.gcd(M,N))
    iter_num=5
    print(cz,cx,cy)
    Sz_matric=[[1,bz,0],[cz,1+bz*cz,0],[0,0,1]]
    Sx_matric=[[1,0,0],[0,1,bx],[0,cx,1+bz*cx]]
    Sy_matric=[[1+by*cy,0,cy],[0,1,0],[by,0,1]]
    print(Sz_matric)
    print(Sx_matric)
    print(Sy_matric)
    print(type(source_img[75][56][0]))
    for height in source_img:
        wid_ans=[]
        for  width in height:
            output=width.astype(int)
            
            for i in range(iter_num):
                #print(width)
                output = np.dot(Sz_matric, output)
                
                output[0]=output[0]%N
                output[1]=output[1]%M
                output[2]=output[2]%K
                
                output = np.dot(Sx_matric, output)
                output[0]=output[0]%N 
                output[1]=output[1]%M
                output[2]=output[2]%K

                output = np.dot(Sy_matric, output)
                output[0]=output[0]%N
                output[1]=output[1]%M
                output[2]=output[2]%K
                #k=input()
            #output[0]=output[0].astype(np.uint8)
            #output[1]=output[1].astype(np.uint8)
            #output[2]=output[2].astype(np.uint8)
            #output=output[::-1]
            wid_ans.append(output)
        answer.append(wid_ans)
    answer=np.array(answer)    
    cv2.imwrite(enc_pic,answer)
    print("finish encrypt")



    answer=[]
    source_img = cv2.imread(enc_pic)
    Sz_inverse_matric=[[1,-bz,0],[-cz,1,0],[0,0,1]]
    Sx_inverse_matric=[[1,0,0],[0,1,-bx],[0,-cx,1]]
    Sy_inverse_matric=[[1,0,-cy],[0,1,0],[-by,0,1]]
    print(Sz_inverse_matric)
    print(Sx_inverse_matric)
    print(Sy_inverse_matric)
    for height in source_img:
        wid_ans=[]
        for  width in height:
            output=width.astype(int)
            
            for i in range(iter_num):
                #print(width)
                output = np.dot(Sy_inverse_matric, output)
                
                output[0]=output[0]%N
                output[1]=output[1]
                output[2]=output[2]%K
                
                output = np.dot(Sx_inverse_matric, output)
                output[0]=output[0] 
                output[1]=output[1]%M
                output[2]=output[2]%K

                output = np.dot(Sz_inverse_matric, output)
                output[0]=output[0]%N
                output[1]=output[1]%M
                output[2]=output[2]
                #k=input()
            #output[0]=output[0].astype(np.uint8)
            #output[1]=output[1].astype(np.uint8)
            #output[2]=output[2].astype(np.uint8)
            #output=output[::-1]
            wid_ans.append(output)
        answer.append(wid_ans)
    answer=np.array(answer)    
    cv2.imwrite(dec_pic,answer)
    print("finish decrypt")

if __name__ == "__main__":
    sol("./source/kodim04.png","./encryp/kodim04.png","./decryp/kodim04.png")
    source_img = cv2.imread("./source/kodim04.png")
    #print(len(source_img))
    #print(len(source_img[0]))
    #source=os.listdir("./source")
    #for i in source:
    #    print(i)