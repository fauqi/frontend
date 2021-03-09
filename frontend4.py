import requests
import json
import urllib3
from tkinter import *

from PIL import ImageTk, Image
from Beranda import *

#print(SCREENWIDTH)

b=Beranda(lontong)
b.showLayar()
jumlahJob=0

def increment():
    global jumlahJob
    
   # print(k)
    for i in range(jumlahJob):
        btnTask[i].destroy()
    jumlahJob=jumlahJob+1
    appendCad(1,3)

def listKaryawan():
    tryButton = Button(b.frame,text= "mbak bi",command = increment)
    tryButton.place(x=200,y=50,width=50,height=50)
    
    labelUser=len(b.pegawai)

    labelPegawai=[0 for z in range(5)]
    labelUser=[0 for y in range(5)]
    for j in range(len(b.pegawai)):
        labelPegawai[j]= Label(b.frame,text = b.pegawai[j],bg="WHITE",fg='#1687A7',font=10)
        labelPegawai[j].place(x=0.085*b.sW,y=j*((0.078*b.sH)+0.09*b.sH)+(0.243*b.sH),width=0.056*b.sW,height=0.078*b.sH,anchor=W)
        labelUser[j]= Label(b.frame,text="Lontong",image = b.userGambar,bg="WHITE")
        labelUser[j].place(x=0.0285*b.sW,y=j*((0.078*b.sH)+0.09*b.sH)+(0.243*b.sH),width=0.056*b.sW,height=0.078*b.sH,anchor=W)


def appendCad(bariskaryawan,kontainer=1):
        global jumlahJob
        global  btnTask,k,result,gambar
        maksJob=7
        #print(len(result))
        k=len(result)
  
        wContainer=0.843 * b.sW
        btnTask =[0 for x in range(88)]
        gambar=[0 for y in range(60)]
        containerJob=[0 for y in range(kontainer)]
        itembaris=jumlahJob/kontainer
        if itembaris<maksJob:
            k=7
            kelebihan=0
        else:
            k=int(jumlahJob/kontainer)
            kelebihan= jumlahJob%kontainer
        lastBaris=0

        for i in range(kontainer):
            if kelebihan>0:
                containerJob[i]=k+1
                kelebihan=kelebihan-1
            else :
                containerJob[i]=k
            print("jumlah container"+str(i)+"="+str(containerJob[i]))
        jumlahItem=containerJob[0]
        icontainer=0
        x=0

        print("mulai \r\n")
        for i in range(jumlahJob):
            btnTask[i] = Button(b.frame,text="hallo "+str(i))            
            btnTask[i].config(command=lambda:b.tertekan(result[i]))
            
            if(x>=(containerJob[icontainer]-1)):
                icontainer=icontainer+1
            sigmaContainerTerlewat=0
            for m in range(icontainer):
                sigmaContainerTerlewat=sigmaContainerTerlewat+containerJob[m]

            x=i-sigmaContainerTerlewat
          
            panjangButton=(wContainer-((0.01*b.sW)+((jumlahItem+1)*0.01*b.sW)))/containerJob[icontainer]
        
            offsetH=0.170*b.sH + (bariskaryawan*0.180*b.sH)
            offsetW=0.163*b.sW            
            btnTask[i].place(x=(x)*(panjangButton+(0.01*b.sW))+offsetW,y=((int(icontainer)*0.180*b.sH)+offsetH),width=panjangButton,height=0.158*b.sH) 
            print("i="+str(i) +",x="+str(x)+",sigma="+str(sigmaContainerTerlewat) +",icontainer= " + str(icontainer))

          


            # elif i>6 and i <=13:
            #     c=i-7
            #     #print(c)
            #     btnTask[i].place(x=c*(((pnjangBtn-((7+1)*0.01*b.sW))/7)+0.01*b.sW)+((0.163*b.sW)),y=0.347*b.sH,width=(pnjangBtn-((0.01*b.sW)+((7+1)*0.01*b.sW)))/7,height=0.158*b.sH)
            # elif i>13 and i<=20:
            #     d=i-14
            #     btnTask[i].place(x=d*(((pnjangBtn-((7+1)*0.01*b.sW))/7)+0.01*b.sW)+((0.163*b.sW)),y=0.52*b.sH,width=(pnjangBtn-((0.01*b.sW)+((7+1)*0.01*b.sW)))/7,height=0.158*b.sH)
            # elif i>20:
            #     e=i-21
            #     btnTask[i].place(x=e*(((pnjangBtn-((7+1)*0.01*b.sW))/7)+0.01*b.sW)+((0.163*b.sW)),y=0.7*b.sH,width=(pnjangBtn-((0.01*b.sW)+((7+1)*0.01*b.sW)))/7,height=0.158*b.sH)


# for i in range(len(result)):
#     x=i
#     try:
#         gambar[x]=loadImageWebPublic(result[x]['image'],0,80)
#         btnTask[i].config(image=gambar[x])
#        # print("ada gambar")
#     except:
#         print("no Image")
#         photo=Image.open("no image.png")
#         photo =photo.resize((80, 80), Image.ANTIALIAS)
#         gambar[x]= ImageTk.PhotoImage(photo)
#         btnTask[i].config(image=gambar[x])
#     #print("luar try")
#     btnTask[i].config(command=lambda x=i,id=result[x]['id']:b.tertekan(result[x],id))
    

#print(result[0]['is_stock'])

#btnTask[0].config(image=gambar10)
listKaryawan()
lontong.mainloop()
