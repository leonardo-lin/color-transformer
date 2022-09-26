#from random import gauss
from re import X
import cv2
import numpy as np
import csv
print("hi")


def sol(namesorce,nametarget):
    lastinfor=[]
    with open(".\\sideinfodeci\\"+namesorce+"_"+nametarget+".txt") as f:
        for i in f.readlines():
            lastinfor.append(float(i))

    coltra_img = cv2.imread(".\\coltra\\"+namesorce+"_"+nametarget+".png")
    #print(len(coltra_img))
    #print(len(coltra_img[0]))
    revfct=[]
    print(lastinfor)

    for i in range(len(coltra_img)):
        revfct.append([])
        for j in range(len(coltra_img[0])):
            revfct[i].append([])
            revfct[i][j].append(((coltra_img[i][j][0]-lastinfor[8])*lastinfor[5]/lastinfor[11]+lastinfor[2]))
            revfct[i][j].append(((coltra_img[i][j][1]-lastinfor[7])*lastinfor[4]/lastinfor[10])+lastinfor[1])
            revfct[i][j].append(((coltra_img[i][j][2]-lastinfor[6])*lastinfor[3]/lastinfor[9])+lastinfor[0])
    revfct_img=np.array(revfct)
    cv2.imwrite(".\\revfct\\"+namesorce+"_revfct.png",revfct_img)
    print()
    #MSE
    source_image=cv2.imread(".\\source\\"+namesorce+".png")
    rmse=0
    gmse=0
    bmse=0
    #to compute total value of rgb
    rrtot=[]
    grtot=[]
    brtot=[]
    rstot=[]
    gstot=[]
    bstot=[]
    for i in range(len(revfct)):
        for j in range(len(revfct[i])):
            rmse=rmse+((revfct[i][j][2]-source_image[i][j][2])**2)
            rrtot.append(revfct[i][j][2])
            rstot.append(source_image[i][j][2])
            gmse=gmse+((revfct[i][j][1]-source_image[i][j][1])**2)
            grtot.append(revfct[i][j][1])
            gstot.append(source_image[i][j][1])
            bmse=bmse+((revfct[i][j][0]-source_image[i][j][0])**2)
            brtot.append(revfct[i][j][0])
            bstot.append(source_image[i][j][0])
    rmse=np.around(rmse/(len(revfct)*len(revfct[i])),2)  
    gmse=np.around(gmse/(len(revfct)*len(revfct[i])),2)
    bmse=np.around(bmse/(len(revfct)*len(revfct[i])),2)
    print(rmse,gmse,bmse)
    #psnr
    if rmse==0:
        rpsnr="INF"
    else:
        rpsnr=np.around(10*np.log10(255*255/rmse),2)
    if gmse==0:
        gpsnr="INF"
    else:
        gpsnr=np.around(10*np.log10(255*255/gmse),2)
    if bmse==0:
        bpsnr="INF"
    else:
        bpsnr=np.around(10*np.log10(255*255/bmse),2)
    print(rpsnr,gpsnr,bpsnr)

    #SSIM
    rrmean=np.mean(rrtot)
    grmean=np.mean(grtot)
    brmean=np.mean(brtot)
    rsmean=lastinfor[0]
    gsmean=lastinfor[1]
    bsmean=lastinfor[2]
    rrvar=np.std(rrtot)**2
    grvar=np.std(grtot)**2
    brvar=np.std(brtot)**2
    rsvar=lastinfor[3]**2
    gsvar=lastinfor[4]**2
    bsvar=lastinfor[5]**2
    rcov=np.cov(rrtot,rstot)[0][1]
    gcov=np.cov(grtot,gstot)[0][1]
    bcov=np.cov(brtot,bstot)[0][1]
    #print(rcov,gcov,bcov)
    c1=(0.01*255)**2
    c2=(0.03*255)**2
    rssim=((2*rrmean*rsmean+c1)*(rcov+c2))/((rrmean**2+rsmean**2+c1)*(rrvar+rsvar+c2))
    gssim=((2*grmean*gsmean+c1)*(gcov+c2))/((grmean**2+gsmean**2+c1)*(grvar+gsvar+c2))
    bssim=((2*brmean*bsmean+c1)*(bcov+c2))/((brmean**2+bsmean**2+c1)*(brvar+bsvar+c2))
    rssim=np.around(rssim,6)
    gssim=np.around(gssim,6)
    bssim=np.around(bssim,6)
    print(rssim,gssim,bssim)
    print()

    #write
    f = open(".\\revfct\\"+namesorce+"_revfct.txt", 'w')
    f.write(str(rmse)+" "+str(rpsnr)+" "+str(rssim)+"\n")
    f.write(str(gmse)+" "+str(gpsnr)+" "+str(gssim)+"\n")
    f.write(str(bmse)+" "+str(bpsnr)+" "+str(bssim)+"\n")
    f.close

if __name__ == "__main__":
    sol("01_kodim05","kodim06")
    sol("02_kodim07","kodim08")
    sol("03_kodim09","kodim10")
    