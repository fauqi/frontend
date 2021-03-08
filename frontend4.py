import requests
import json
import urllib3
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
from appendCad import *

tertekanFlag=0
k=0
c=0
z=0
flag =0
starFlag=0

stock=False
operator=""




def splitter(s):
    total =0
    result=""
    c = s.split()
    for i in range(len(c)):
        counter=len(c[i])
        total=total+counter
       # print(total)
        if(total<15):
            result=result+" "+c[i]
        else :
            result=result+"\n"+c[i]
            total=0
    return (result)

print(splitter(result[1]['stock']))

#print(SCREENWIDTH)
b=Beranda(lontong)
b.showLayar()


# def increment():
#     global k
    
#    # print(k)
#     for i in range(k):
#         btnTask[i].destroy()
#     k=k+1
#     appendCad()

def appendCad():
        global  btnTask,k,result,gambar
        maksJob=7
        kontainer=1
        #print(len(result))
        k=len(result)
       
        # tryButton = Button(b.frame,text= "mbak bi",command = increment)
        # tryButton.place(x=200,y=50,width=50,height=50)
       
        labelUser=len(b.pegawai)

        labelPegawai=[0 for z in range(5)]
        labelUser=[0 for y in range(5)]
        for j in range(len(b.pegawai)):
            labelPegawai[j]= Label(b.frame,text = b.pegawai[j],bg="WHITE",fg='#1687A7',font=10)
            labelPegawai[j].place(x=0.085*b.sW,y=j*((0.078*b.sH)+0.09*b.sH)+(0.243*b.sH),width=0.056*b.sW,height=0.078*b.sH,anchor=W)
            labelUser[j]= Label(b.frame,text="Lontong",image = b.userGambar,bg="WHITE")
            labelUser[j].place(x=0.0285*b.sW,y=j*((0.078*b.sH)+0.09*b.sH)+(0.243*b.sH),width=0.056*b.sW,height=0.078*b.sH,anchor=W)


        pnjangBtn=0.843 * b.sW
        
        btnTask =[0 for x in range(88)]
        gambar=[0 for y in range(60)]
        for i in range(k):
            btnTask[i] = Button(b.frame,text="hallo "+str(i))


            
            #btnTask[i].config(command=lambda:b.tertekan(result[i]))
            
            if kontainer == 1:
                if k<=maksJob:
                    btnTask[i].place(x=i*(((pnjangBtn-((7+1)*0.01*b.sW))/7)+0.01*b.sW)+((0.163*b.sW)),y=0.175*b.sH,width=(pnjangBtn-((0.01*b.sW)+((7+1)*0.01*b.sW)))/7,height=0.158*b.sH) 
                else :
                    btnTask[i].place(x=i*(((pnjangBtn-((k+1)*0.01*b.sW))/k)+0.01*b.sW)+((0.163*b.sW)),y=0.175*b.sH,width=(pnjangBtn-((0.01*b.sW)+((k+1)*0.01*b.sW)))/k,height=0.158*b.sH) 
            elif  kontainer ==2 :
                if i<=6 :
                    btnTask[i].place(x=i*(((pnjangBtn-((7+1)*0.01*b.sW))/7)+0.01*b.sW)+((0.163*b.sW)),y=0.175*b.sH,width=(pnjangBtn-((0.01*b.sW)+((7+1)*0.01*b.sW)))/7,height=0.158*b.sH) 
                elif i>6:
                    c=i-7
                    #print(c)
                    btnTask[i].place(x=c*(((pnjangBtn-((7+1)*0.01*b.sW))/7)+0.01*b.sW)+((0.163*b.sW)),y=0.347*b.sH,width=(pnjangBtn-((0.01*b.sW)+((7+1)*0.01*b.sW)))/7,height=0.158*b.sH) 
            elif kontainer == 3:
                if i<=6 :
                    btnTask[i].place(x=i*(((pnjangBtn-((7+1)*0.01*b.sW))/7)+0.01*b.sW)+((0.163*b.sW)),y=0.175*b.sH,width=(pnjangBtn-((0.01*b.sW)+((7+1)*0.01*b.sW)))/7,height=0.158*b.sH) 
                elif i>6 and i <=13:
                    c=i-7
                   #
                   # print(c)
                    btnTask[i].place(x=c*(((pnjangBtn-((7+1)*0.01*b.sW))/7)+0.01*b.sW)+((0.163*b.sW)),y=0.347*b.sH,width=(pnjangBtn-((0.01*b.sW)+((7+1)*0.01*b.sW)))/7,height=0.158*b.sH)
                elif i>13:
                    d=i-14
                    btnTask[i].place(x=d*(((pnjangBtn-((7+1)*0.01*b.sW))/7)+0.01*b.sW)+((0.163*b.sW)),y=0.52*b.sH,width=(pnjangBtn-((0.01*b.sW)+((7+1)*0.01*b.sW)))/7,height=0.158*b.sH)
            elif kontainer == 4:
                if i<=6 :
                    btnTask[i].place(x=i*(((pnjangBtn-((7+1)*0.01*b.sW))/7)+0.01*b.sW)+((0.163*b.sW)),y=0.175*b.sH,width=(pnjangBtn-((0.01*b.sW)+((7+1)*0.01*b.sW)))/7,height=0.158*b.sH) 
                elif i>6 and i <=13:
                    c=i-7
                    #print(c)
                    btnTask[i].place(x=c*(((pnjangBtn-((7+1)*0.01*b.sW))/7)+0.01*b.sW)+((0.163*b.sW)),y=0.347*b.sH,width=(pnjangBtn-((0.01*b.sW)+((7+1)*0.01*b.sW)))/7,height=0.158*b.sH)
                elif i>13 and i<=20:
                    d=i-14
                    btnTask[i].place(x=d*(((pnjangBtn-((7+1)*0.01*b.sW))/7)+0.01*b.sW)+((0.163*b.sW)),y=0.52*b.sH,width=(pnjangBtn-((0.01*b.sW)+((7+1)*0.01*b.sW)))/7,height=0.158*b.sH)
                elif i>20:
                    e=i-21
                    btnTask[i].place(x=e*(((pnjangBtn-((7+1)*0.01*b.sW))/7)+0.01*b.sW)+((0.163*b.sW)),y=0.7*b.sH,width=(pnjangBtn-((0.01*b.sW)+((7+1)*0.01*b.sW)))/7,height=0.158*b.sH)

appendCad()

for i in range(k):
    x=i
    try:
        gambar[x]=loadImageWebPublic(result[x]['image'],0,80)
        btnTask[i].config(image=gambar[x])
        print("ada gambar")
    except:
        print("no Image")
        photo=Image.open("no image.png")
        photo =photo.resize((80, 80), Image.ANTIALIAS)
        gambar[x]= ImageTk.PhotoImage(photo)
        btnTask[i].config(image=gambar[x])
    print("luar try")
    btnTask[i].config(command=lambda x=i,id=result[x]['id']:b.tertekan(result[x],id))
    

print(result[0]['is_stock'])

#btnTask[0].config(image=gambar10)
lontong.mainloop()
