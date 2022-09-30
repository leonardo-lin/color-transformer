
from unicodedata import decimal
import cv2
import numpy as np
import csv
print("hi")
#123
def sol(ques):
    print(ques)
    img = cv2.imread(ques+".png")
    #print(len(img[0]))
    #print(img[0][0])
    #question1
    r_channel=[]
    b_channel=[]
    g_channel=[]
    for i in range(512):
        for j in range(512):
            b_channel.append(img[i][j][0])
            g_channel.append(img[i][j][1])
            r_channel.append(img[i][j][2])
    
    bmean=np.around(np.mean(b_channel),2)
    gmean=np.around(np.mean(g_channel),2)
    rmean=np.around(np.mean(r_channel),2)
    bstd=np.around(np.std(b_channel),2)
    gstd=np.around(np.std(g_channel),2)
    rstd=np.around(np.std(r_channel),2)
    print(bmean,gmean,rmean,bstd,gstd,rstd)

    with open(ques+"-mean-std.csv",'w',newline='',encoding='utf-8_sig') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([rmean, gmean, bmean])
        writer.writerow([rstd, gstd,bstd])


    #question2
    bnp=np.array(b_channel)
    gnp=np.array(g_channel)
    rnp=np.array(r_channel)
    bhis=[[]for x in range(256)]
    ghis=[[]for x in range(256)]
    rhis=[[]for x in range(256)]
    #numpy.count_nonzero(aCountZero == 100.1)
    for i in range(256):
        bhis[i].append(np.count_nonzero(bnp==i))
        ghis[i].append(np.count_nonzero(gnp==i))
        rhis[i].append(np.count_nonzero(rnp==i))
    with open(ques+"-his.csv",'w',newline='',encoding='utf-8_sig') as csvfile:
        writer = csv.writer(csvfile)
        for i in range(256):
            writer.writerow([rhis[i][0], ghis[i][0], bhis[i][0]])
    #print(bhis)
if __name__ == "__main__":
    
    q1='baboon'
    q2='kodim07'
    q3='kodim17'
    q4='peppers'
    sol(q1)
    sol(q2)
    sol(q3)
    sol(q4)
