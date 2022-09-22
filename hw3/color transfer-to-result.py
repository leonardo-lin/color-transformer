from re import X
import cv2
import numpy as np
import csv
print("hi")


def sol(source,target,textnum):
    print(source,target)
    sortar=[source,target]
    source_img = cv2.imread(".\\source\\"+textnum+source+".png")
    print(len(source_img))
    print(len(source_img[0])) 
    #question1
    sr_channel=[]
    sb_channel=[]
    sg_channel=[]
    for i in range(len(source_img)):
        for j in range(len(source_img[0])):
            sb_channel.append(source_img[i][j][0])
            sg_channel.append(source_img[i][j][1])
            sr_channel.append(source_img[i][j][2])
    
    sbmean=np.around(np.mean(sb_channel),2)
    sgmean=np.around(np.mean(sg_channel),2)
    srmean=np.around(np.mean(sr_channel),2)
    sbstd=np.around(np.std(sb_channel),2)
    sgstd=np.around(np.std(sg_channel),2)
    srstd=np.around(np.std(sr_channel),2)
    print(sbmean,sgmean,srmean,sbstd,sgstd,srstd)
    #source finish

    #target
    target_img = cv2.imread(".\\target\\"+textnum+target+".png")
    print(len(target_img))
    print(len(target_img[0]))    
    tr_channel=[]
    tb_channel=[]
    tg_channel=[]
    for i in range(len(target_img)):
        for j in range(len(target_img[0])):
            tb_channel.append(target_img[i][j][0])
            tg_channel.append(target_img[i][j][1])
            tr_channel.append(target_img[i][j][2])
    
    tbmean=np.around(np.mean(tb_channel),2)
    tgmean=np.around(np.mean(tg_channel),2)
    trmean=np.around(np.mean(tr_channel),2)
    tbstd=np.around(np.std(tb_channel),2)
    tgstd=np.around(np.std(tg_channel),2)
    trstd=np.around(np.std(tr_channel),2)
    print(tbmean,tgmean,trmean,tbstd,tgstd,trstd)  
    f = open(".\\sideinfodeci\\"+textnum+source+target+".txt", 'w')
    f.write(str(srmean)+"\n")
    f.write(str(sgmean)+"\n")
    f.write(str(sbmean)+"\n")
    f.write(str(srstd)+"\n")
    f.write(str(sgstd)+"\n")
    f.write(str(sbstd)+"\n")
    f.write(str(trmean)+"\n")
    f.write(str(tgmean)+"\n")
    f.write(str(tbmean)+"\n")
    f.write(str(trstd)+"\n")
    f.write(str(tgstd)+"\n")
    f.write(str(tbstd)+"\n")
    f.close

    #step two
    result=[]
    for i in range(len(source_img)):
        result.append([])
        for j in range(len(source_img[0])):
            result[i].append([])
            result[i][j].append(((tbstd/sbstd)*(source_img[i][j][0]-sbmean))+tbmean)
            result[i][j].append(((tgstd/sgstd)*(source_img[i][j][1]-sgmean))+tgmean)
            result[i][j].append(((trstd/srstd)*(source_img[i][j][2]-srmean))+trmean)
            
    #print(len(result)) 
    for i in range(len(result)):
        for j in range(len(result[0])):
            result[i][j][0]=np.around(result[i][j][0])
            if result[i][j][0]>255:
                result[i][j][0]=255
            elif result[i][j][0]<0:
                result[i][j][0]=0
                #print("blue error")
            result[i][j][1]=np.around(result[i][j][1])
            if result[i][j][1]>255:
                result[i][j][1]=255
            elif result[i][j][1]<0:
                result[i][j][1]=0
                #print("green error")
            result[i][j][2]=np.around(result[i][j][2])  
            if result[i][j][2]>255:
                result[i][j][2]=255
            elif result[i][j][2]<0:
                result[i][j][2]=0
                #print("red error")
    result_img=np.array(result)  
    cv2.imwrite(".\\coltra\\"+textnum+source+target+".png",result_img)
    print(len(result_img))
    print(len(result_img[0]))    
    rr_channel=[]
    rb_channel=[]
    rg_channel=[]
    for i in range(len(result_img)):
        for j in range(len(result_img[0])):
            rb_channel.append(result_img[i][j][0])
            rg_channel.append(result_img[i][j][1])
            rr_channel.append(result_img[i][j][2])
    
    rbmean=np.around(np.mean(rb_channel),2)
    rgmean=np.around(np.mean(rg_channel),2)
    rrmean=np.around(np.mean(rr_channel),2)
    rbstd=np.around(np.std(rb_channel),2)
    rgstd=np.around(np.std(rg_channel),2)
    rrstd=np.around(np.std(rr_channel),2)
    print(rbmean,rgmean,rrmean,rbstd,rgstd,rrstd) 


    #step3 print mean&standard
    """with open(textnum+source+"-mean-std.csv",'w',newline='',encoding='utf-8_sig') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([srmean, sgmean, sbmean])
        writer.writerow([srstd, sgstd,sbstd])
    with open(textnum+target+"-mean-std.csv",'w',newline='',encoding='utf-8_sig') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([trmean, tgmean, tbmean])
        writer.writerow([trstd, tgstd,tbstd])
    with open(textnum+source+target+"-mean-std.csv",'w',newline='',encoding='utf-8_sig') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([rrmean, rgmean, rbmean])
        writer.writerow([rrstd, rgstd,rbstd])
    """
    """
    #histogram
    for i in range(3):
        
        if i==0:
            #source
            print(textnum+"_source")
            b_channel=sb_channel
            g_channel=sg_channel
            r_channel=sr_channel
            cname=textnum+source
        elif i==1:
            #target
            print(textnum+"_target")
            b_channel=tb_channel                        
            g_channel=tg_channel
            r_channel=tr_channel
            cname=textnum+target
        else:
            print(textnum+"_result")
            #target
            b_channel=rb_channel                       
            g_channel=rg_channel
            r_channel=rr_channel
            cname=textnum+source+target
        bnp=np.array(b_channel)
        gnp=np.array(g_channel)
        rnp=np.array(r_channel)
        bhis=[[]for x in range(256)]
        ghis=[[]for x in range(256)]
        rhis=[[]for x in range(256)]
        for i in range(256):
            bhis[i].append(np.count_nonzero(bnp==i))
            ghis[i].append(np.count_nonzero(gnp==i))
            rhis[i].append(np.count_nonzero(rnp==i))
        with open(cname+"-his.csv",'w',newline='',encoding='utf-8_sig') as csvfile:
            writer = csv.writer(csvfile)
            for i in range(256):
                writer.writerow([rhis[i][0], ghis[i][0], bhis[i][0]])
        """
if __name__ == "__main__":
    sol("_kodim05","_kodim06","01")
    sol("_kodim07","_kodim08","02")
    sol("_kodim09","_kodim10","03")
    