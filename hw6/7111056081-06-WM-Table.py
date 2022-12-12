
import math
import copy
import numpy as np
table=[]
def bol(w_corrus,pnt,v,n,w,m):
    i=-v
    #print(table)
    if pnt!=n:
        w_c=copy.deepcopy(w_corrus)
        while w_c[pnt]<=v:
            #print(i,w_c)            
            #w_c[pnt]+=1
            bol(w_c,pnt+1,v,n,w,m)
            w_c[pnt]+=1
            i+=1
    else:
        w_c=copy.deepcopy(w_corrus)
        r=0
        for i in range(len(w_c)):
            r+=w_c[i]*w[i]
        r=r%m
        se=0
        for i in range(len(w_c)):
            se+=w_c[i]**2
        #print(r,se)
        table.append([r,se,w_c])   
        return 0

n=4
m=79
w=[1,3,9,26]
q=m**(1/2) -1
v=math.ceil((q**2 *n)**(1/2))
print(n,m,q,v)
#R=[ [] for i in range(2*v+1)]#+1?
#SE=[ [] for i in range(2*v+1)]
table=[]
w_corrus=[]
for i in range(n):
    w_corrus.append(-v)
print(w_corrus)
pnt=0
bol(w_corrus,pnt,v,n,w,m)




table=sorted(table)   
#print(table)
PAtable=[]
cntP=0
HAtable=[]
cntH=0
best_r=0
for i in table:
    if i[0]==best_r:
        best_r+=1
        PAtable.append([cntP,i[0],i[1],i[2]])
        cntP+=1
    else:
        HAtable.append([cntH,i[0],i[1],i[2]])
        cntH+=1
        
print()
#print(PAtable)
#print(HAtable)
#計算TSE MSE PSNR
sqr=n*m
TSE=0
for i in PAtable:
    TSE+=i[2]**2
MSE=TSE/sqr
PSNR=np.around(10*np.log10(255*255/MSE),2)
print(TSE,MSE,PSNR)
import csv

for i in range(len(PAtable)):
    p=PAtable[i].pop()
    for j in p:
        PAtable[i].append(j)
for i in range(len(HAtable)):
    p=HAtable[i].pop()
    for j in p:
        HAtable[i].append(j)
        
        
# 開啟輸出的 CSV 檔案 要改
with open('PA_4_79_(1_3_9_26).csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)

    # 寫入一列資料
    writer.writerow(['PA',str(n),str(m),'w1','w2','w3','w4'])
    writer.writerow(['IX','d','SE',w[0],w[1],w[2],w[3]])
    writer.writerows(PAtable)
    
with open('HA_4_79_(1_3_9_26).csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)

    # 寫入一列資料
    writer.writerow(['HA',str(n),str(m),'w1','w2','w3','w4'])
    writer.writerow(['IX','d','SE',w[0],w[1],w[2],w[3]])
    writer.writerows(PAtable)    