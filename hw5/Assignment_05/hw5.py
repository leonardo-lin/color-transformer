
import random    
from re import X
import cv2
import numpy as np

def sol(n,pic_name,secret_text):
    
    img = cv2.imread(pic_name+".png")
    source_r_channel=[]
    source_b_channel=[]
    source_g_channel=[]
    for i in range(len(img)):
        for j in range(len(img[0])):
            source_b_channel.append(img[i][j][0])
            source_g_channel.append(img[i][j][1])
            source_r_channel.append(img[i][j][2])

    print((source_r_channel[0:30]))
    print((source_g_channel[0:30]))
    print((source_b_channel[0:30]))
    cnt=0
    rhead=0  
    ghead=0
    bhead=0 
    dob_n=2*n+1
    print(dob_n)
    for turn in range(len(secret_text)):
        
        if cnt%3==0:
            f_tot=0
            for i in range(n):
                f_tot+=source_r_channel[rhead+i]*i
            f_tot=f_tot%dob_n
            print("f_tot= ",f_tot)
            s=(secret_text[turn]-f_tot)%(dob_n)        
            print(secret_text[turn],f_tot,s)
            print("rhead=",rhead,n)
            if s==0:
                print("s=0")
                pass
            elif s<=n :
                source_r_channel[rhead+s-1]+=1
                print("in",rhead,s,rhead+s-1)
            elif s>n:
                source_r_channel[rhead+n+n-s]-=1           
                print("twin",rhead,s,rhead+n+n-s)
            print(source_r_channel[0:30])
            rhead+=n
        elif cnt%3==1:
            f_tot=0
            for i in range(n):
                f_tot+=source_g_channel[ghead+i]*i
            f_tot=f_tot%dob_n
            print("f_tot= ",f_tot)
            s=(secret_text[turn]-f_tot)%(dob_n)        
            print(secret_text[turn],f_tot,s)
            print("ghead=",ghead,n)
            if s==0:
                print("s=0")
                pass
            elif s<=n :
                source_g_channel[ghead+s-1]+=1
                print("in",ghead,s,ghead+s-1)
            elif s>n:
                source_g_channel[ghead+n+n-s]-=1           
                print("twin",ghead,s,ghead+n+n-s)
            print(source_g_channel[0:30])
            ghead+=n
        elif cnt%3==2:
            f_tot=0
            for i in range(n):
                f_tot+=source_b_channel[bhead+i]*i
            f_tot=f_tot%dob_n
            print("f_tot= ",f_tot)
            s=(secret_text[turn]-f_tot)%(dob_n)        
            print(secret_text[turn],f_tot,s)
            print("bhead=",bhead,n)
            if s==0:
                print("s=0")
                pass
            elif s<=n :
                source_b_channel[bhead+s-1]+=1
                print("in",bhead,s,bhead+s-1)
            elif s>n:
                source_b_channel[bhead+n+n-s]-=1           
                print("twin",bhead,s,bhead+n+n-s)
            print(source_b_channel[0:30])
            bhead+=n
            
            
        cnt+=1


    # get output image
    cnt=0
    result=[]
    for i in range(len(img)):
        result.append([])
        for j in range(len(img[0])):
            result[i].append([])
            result[i][j].append(source_b_channel[cnt])
            result[i][j].append(source_g_channel[cnt])
            result[i][j].append(source_r_channel[cnt])
            cnt+=1
    error=0        
    print(len(result),len(result[0]))
    for i in range(len(result)):
        for j in range(len(result[0])):
            result[i][j][0]=np.around(result[i][j][0])
            if result[i][j][0]>255:
                result[i][j][0]=255
            elif result[i][j][0]<0:
                result[i][j][0]=0
                print("blue error")
            result[i][j][1]=np.around(result[i][j][1])
            if result[i][j][1]>255:
                result[i][j][1]=255
            elif result[i][j][1]<0:
                result[i][j][1]=0
                print("green error")
            result[i][j][2]=np.around(result[i][j][2])  
            if result[i][j][2]>255:
                result[i][j][2]=255
                print("red error")
            elif result[i][j][2]<0:
                result[i][j][2]=0
                
    result_img=np.array(result) 
    cv2.imwrite(pic_name+"_stego_EMD_"+str(n)+".png",result_img) 
        
if __name__ == "__main__":
    
    n=0
    while(n<2 or n>10):
        n=input("Input number of pixels in a cluster (n): ")
    pic_name=input("Input cover image: ")
    seed=2022
    random.seed(seed)
    text=random.random()
    text=int(text*1000)
    print(text)
    secret_text=[]
    while text!=0:
        secret_text.append(text%n)
        text=text//n
    print(secret_text)
    secret_text=secret_text[::-1]
    print(secret_text)

    sol(n,pic_name,secret_text)




