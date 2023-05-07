print("start")
import numpy as np
import cv2
import os
import random
import math
import copy
import os

def sol(enc_pic,dec_pic,output_txt):
    answer2=[]
    source_img = cv2.imread(enc_pic)
    #answer = [[0 for j in range(N)] for i in range(M)]
    M=len(source_img)
    N=len(source_img[0])

    K=24
    if len(source_img.shape) == 2:
        K=8
    print(M,N,K)
    bz=24
    rz=12
    cz=int((rz*M)/math.gcd(M,N))
    bx=25
    rx=16
    cx=int((rx*M)/math.gcd(M,K))
    by=27
    ry=18
    cy=int((ry*N)/math.gcd(K,N))
    iter_num=5
    answer2=copy.deepcopy(source_img)
    Sz_inverse_matric=[[1,-bz,0],[-cz,1,0],[0,0,1]]
    Sx_inverse_matric=[[1,0,0],[0,1,-bx],[0,-cx,1]]
    Sy_inverse_matric=[[1,0,-cy],[0,1,0],[-by,0,1]]
    print(Sz_inverse_matric)
    print(Sx_inverse_matric)
    print(Sy_inverse_matric)
    for i in range(M):
        ori=i
        for j in range(N):
            orj=j
            output=[i,j,48]
            
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
            answer2[output[1]][output[0]]=source_img[ori][orj] 
    answer2=np.array(answer2)        
    cv2.imwrite(dec_pic,answer2)

    """
    f = open(output_txt, 'w')
    f.write("N ="+str(N) +"\n")
    f.write("M ="+str(M) +"\n")
    f.write("gcd(M,N) ="+str(math.gcd(M,N)) +"\n")
    f.write("gcd(M,K) ="+str(math.gcd(M,K)) +"\n")
    f.write("gcd(K,N) ="+str(math.gcd(K,N)) +"\n")
    f.write("bx ="+str(bx) +"\n")
    f.write("by ="+str(by) +"\n")
    f.write("bz ="+str(bz) +"\n")
    f.write("rx ="+str(rx) +"\n")
    f.write("ry ="+str(ry) +"\n")
    f.write("rz ="+str(rz) +"\n")
    f.write("cx ="+str(cx) +"\n")
    f.write("cy ="+str(cy) +"\n")
    f.write("cz ="+str(cz) +"\n")"""
    print("finish decrypt")
if __name__ == "__main__":
    #sol2("./source/kodim04.png","./encryp/kodim04.png","./decryp/kodim04.png")
    #sol2("./source/Boat.png","./encryp/Boat.png","./decryp/Boat.png")
    source_path = "./source/"
    enc_path = "./encryp"
    dec_path = "./decryp"
    dirs = os.listdir( enc_path )
    for i in dirs:
        sol("./encryp/"+i,"./decryp/"+i,"./parame/"+i[:-3]+"txt")
    #source_img = cv2.imread("./source/kodim04.png")