from math import ceil
from xml.sax.handler import DTDHandler
import numpy as np
ans_EMSE=100
last_b=[]
print("hi there")
import math
def EMSE(b,ans_b,num_d,k,F):
    #reB還沒用
    global ans_EMSE
    global last_b
    #print(ans_EMSE)
    
    if num_d==len(k)-1:
        k[len(k)-1]=-2
        while(k[len(k)-1]<3):
            #compute EMSE
            for i in range(len(k)):
                
                ans_b[i]=b[i]+k[i]
            #c=input()
            #print(ans_b,k,len(k)-1)
            con=0
            for i in ans_b:
                if i <2:
                    con=1
            mul=1
            for j in ans_b:
                mul=mul*j
            if mul<F or  sorted(ans_b)!=ans_b:
                #print("failed",mul,ans_b)
                con=1
            if con==1:
                k[len(k)-1]=k[len(k)-1]+1
                continue
            #permision go-on

            emse=[]
            for i in range(len(k)):
                #print((ans_b[i]**2),((-2)**(ans_b[i]%2)),((ans_b[i]**2)-((-2)**((ans_b[i]+1)%2)))/12)
                emse.append(((ans_b[i]**2)-((-2)**((ans_b[i]+1)%2)))/12)
                pass
            tmp_EMSE=np.mean(emse)
            #print(emse,tmp_EMSE)
            if tmp_EMSE<ans_EMSE:
                ans_EMSE=tmp_EMSE
                last_b=ans_b.copy()
                print("the temp answer is",ans_EMSE,last_b)
            k[len(k)-1]=k[len(k)-1]+1
        return 
    #temp_emse=0;temp_b=0;temp_m=0
    
    tmp_k=k.copy()
    while tmp_k[num_d]<3:
        EMSE(b,ans_b,num_d+1,tmp_k,F)
        tmp_k[num_d]=tmp_k[num_d]+1
    
    return
def sol():
    while(True):
        n=int(input("n= "))
        F=int(input("F= "))
        if n==0 or F==0:
            break
        #n=6
        #F=2589478
        sqF=F**(1/n)
        #print(sqF)
        #print(math.ceil(sqF))
        ans_b=[math.ceil(sqF) for i in range(n)]
        global ans_EMSE
        ans_EMSE=999
        global last_b
        M=0
        b=[math.ceil(sqF) for i in range(n)]
        #print(b)
        k=[-2 for i in range(n)]
        EMSE(b,ans_b,0,k,F)
        
        print("Optimal Base Vector OBV: ",last_b)
        M=1
        for i in last_b:
            M=M*i
        print("Derived Notation M: ",M)
        diff=M-F
        print("Difference: ",diff)
        print("EMSE OBV: ",ans_EMSE)
        psnr=np.around(10*np.log10(255*255/ans_EMSE),2)
        print("PSNR: ",psnr)

if __name__ == "__main__":
    sol()