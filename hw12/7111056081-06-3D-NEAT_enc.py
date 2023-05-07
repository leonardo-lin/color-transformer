print("start")
import numpy as np
import cv2
import os
import random
import math
import copy
import os




def sol(source_pic,enc_pic,dec_pic,output_txt):
    #answer=[]
    source_img = cv2.imread(source_pic)
    
    #cv2.imwrite("./encryp/kodim044.png",source_img)
    M=len(source_img)
    N=len(source_img[0])

    #answer = [[0 for j in range(N)] for i in range(M)]
    answer=copy.deepcopy(source_img)
    #print(type(source_img[0]))
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
    #print(cz,cx,cy)
    Sz_matric=[[1,bz,0],[cz,1+bz*cz,0],[0,0,1]]
    Sx_matric=[[1,0,0],[0,1,bx],[0,cx,1+bz*cx]]
    Sy_matric=[[1+by*cy,0,cy],[0,1,0],[by,0,1]]
    print(Sz_matric)
    print(Sx_matric)
    print(Sy_matric)
    print(type(source_img[75][56][0]))
    for i in range(M):
        ori=i
        for j in range(N):
            orj=j
            output=[i,j,48]
            
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
                #print(output)
            answer[output[1]][output[0]]=source_img[ori][orj] 
    answer=np.array(answer)
    #print(answer)
    
    cv2.imwrite(enc_pic,answer)
    print("finish encrypt")



    
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
    f.write("cz ="+str(cz) +"\n")
    print("finish decrypt")
if __name__ == "__main__":
    #sol2("./source/kodim04.png","./encryp/kodim04.png","./decryp/kodim04.png")
    #sol2("./source/Boat.png","./encryp/Boat.png","./decryp/Boat.png")
    source_path = "./source/"
    enc_path = "./encryp"
    dec_path = "./decryp"
    dirs = os.listdir( source_path )
    for i in dirs:
        sol("./source/"+i,"./encryp/"+i,"./decryp/"+i,"./parame/"+i[:-3]+"txt")
    #source_img = cv2.imread("./source/kodim04.png")
    