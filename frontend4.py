import requests
import json
import urllib3
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
from cloud import result
from cloud import *

tertekanFlag=0
k=0
c=0
z=0
flag =0
starFlag=0

stock=False
operator=""

SCREENWIDTH = int(lontong.winfo_screenwidth())
SCREENHEIGHT = int(lontong.winfo_screenheight())


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
    #print(result)
   # print(x)
    #print(counter)
print(splitter(result[1]['stock']))

#print(SCREENWIDTH)
lontong.geometry("{0}x{1}+0+0".format(SCREENWIDTH, SCREENHEIGHT))
class Beranda:
    def __init__(self,master):
        self.master=master
        self.master.title("apanihman")
        self.pegawai=["Imam","Aji","Roni","MBAK bi"]
        self.sW=SCREENWIDTH
        self.sH=SCREENHEIGHT
        self.frame=Frame(self.master,bg="#f9f9f9")
        
    
    def showLayar(self):

        self.frame.place(x=0,y=0,height=SCREENHEIGHT,width=SCREENWIDTH,anchor=NW)
        self.photo=Image.open("beranda.png")
        self.photo = self.photo.resize((SCREENWIDTH, SCREENHEIGHT), Image.ANTIALIAS)
        self.gambar = ImageTk.PhotoImage(self.photo)
     
        self.labelImage=Label(self.frame,text="LONTONG",height=SCREENHEIGHT,width=SCREENWIDTH,bg="BLUE",image=self.gambar)
        self.labelImage.place(x=0,y=0,height=SCREENHEIGHT,width=SCREENWIDTH,anchor=NW)
        self.btn=Button(self.frame,text="lontong")

       # self.frame.bind('<Button-1>', self.Exit)
       # self.btn.place(x=200,y=200,width= 50,height=50)
       
        self.rW=int(self.sW*0.41)
        self.rH=int(self.sH*0.822)
        #print(self.rH)
        self.photo11=Image.open("lontong.png")
        self.gambar2 = ImageTk.PhotoImage(self.photo11)

        self.userPhoto=Image.open("user.png")
        self.userPhoto= self.userPhoto.resize((int(0.055*self.sW),int(0.078*self.sH)), Image.ANTIALIAS)
        self.userGambar= ImageTk.PhotoImage(self.userPhoto)
    def switch(self,hasil):
        global stock
        if hasil['is_stock']== True:
            hasil['is_stock']=False
            self.switch_btn.config(image=self.switch_tidak_ada)
        else:
            self.switch_btn.config(image=self.switch_ada)
            hasil['is_stock']=True
    def tertekan(self,hasil,identify):
        global stock,tertekanFlag
        self.identify=identify
        print(identify)
        if tertekanFlag==0:
            tertekanFlag=1
            self.hasil=hasil
        # print(hasil['brand'])
            self.frame2=Frame(self.master)
            
            self.frame2.place(x=(self.sW*0.5),y=(self.sH*0.5),height=self.sH*0.79,width=self.sW*0.41,anchor=CENTER)
            
        #ngebuat labelnye
    


            self.photo2=Image.open("popup.png")
            self.photo2 = self.photo2.resize((self.rW,self.rH), Image.ANTIALIAS)
            self.gambar3 = ImageTk.PhotoImage(self.photo2)
            

            
            
            self.label2 = Label(self.frame2,text="LONTONG",bg="WHITE",image=self.gambar3,borderwidth=4)
            self.label2.place(x=0,y=0,height=self.sH*0.79,width=self.sW*0.41,anchor=NW)
    #startButton
        self.photo10=Image.open("!start.png")
        self.photo10=self.photo10.resize((int(0.1*self.sW),int(0.057*self.sH)),Image.ANTIALIAS)
        self.startPhoto2=ImageTk.PhotoImage(self.photo10)
        self.photo3=Image.open("start.png")
        self.photo3=self.photo3.resize((int(0.1*self.sW),int(0.057*self.sH)),Image.ANTIALIAS)
        self.startPhoto=ImageTk.PhotoImage(self.photo3)
        self.startButton=Button(self.frame2,image = self.startPhoto,borderwidth=0,bg="WHITE",command=self.startPressed)
        self.startButton.place(x=0.08*self.sW,y=self.sH*0.68,width=0.12*self.sW,height=0.08*self.sH,anchor=NW)
        if starFlag==1:
            self.startButton.config(image=self.startPhoto2)

    #finishButton
        self.photo8=Image.open("finish.png")
        self.photo8=self.photo8.resize((int(0.1*self.sW),int(0.057*self.sH)),Image.ANTIALIAS)
        self.finishPhoto=ImageTk.PhotoImage(self.photo8)
        self.finishButton=Button(self.frame2,image = self.finishPhoto,borderwidth=0,bg="WHITE",command=self.finishPressed)
        self.finishButton.place(x=0.2*self.sW,y=self.sH*0.68,width=0.12*self.sW,height=0.08*self.sH,anchor=NW)
    #closeButton
        self.photo9=Image.open("close.png")
        self.photo9=self.photo9.resize((int(0.028*self.sW),int(0.04*self.sH)),Image.ANTIALIAS)
        self.closePhoto=ImageTk.PhotoImage(self.photo9)
        self.closeButton=Button(self.frame2,image = self.closePhoto,borderwidth=0,bg="WHITE",command=self.closePressed)
        self.closeButton.place(x=0.35*self.sW,y=self.sH*0.03,width=0.028*self.sW,height=0.04*self.sH,anchor=NW)
    #pauseButton
        self.photo4=Image.open("pause.png")
        self.photo4=self.photo4.resize((int(0.045*self.sW),int(0.063*self.sH)),Image.ANTIALIAS)
        self.pausePhoto=ImageTk.PhotoImage(self.photo4)
        self.pauseButton=Button(self.frame2,image = self.pausePhoto,borderwidth=0,bg="WHITE",command=self.pausePressed)
        self.pauseButton.place(x=0.644*(self.sW*0.41),y=(self.sH*0.82)*0.08,width=0.045*self.sW,height=0.063*self.sH,anchor=W)


            #switch widget
        self.photo6=Image.open("switch_ada.png")
        self.photo6= self.photo6.resize((int(0.06*self.sW),int(0.077*self.sH)), Image.ANTIALIAS)
        self.switch_ada= ImageTk.PhotoImage(self.photo6)
        self.photo7=Image.open("switch_tidak_ada.png")
        self.photo7= self.photo7.resize((int(0.06*self.sW),int(0.077*self.sH)), Image.ANTIALIAS)
        self.switch_tidak_ada= ImageTk.PhotoImage(self.photo7)
        self.switch_btn = Button(self.frame2,bg="WHITE",image=self.switch_tidak_ada,borderwidth=0,command=lambda:self.switch(hasil))
        self.switch_btn.place(x=0.19*self.sW,y=0.03*self.sH,width=0.06*self.sW,height=0.077*self.sH)
        if hasil['is_stock']==True:
            self.switch_btn.config(image=self.switch_ada)
        else:
            self.switch_btn.config(image=self.switch_tidak_ada)
        
        self.labelDeadline=Label(self.frame2,bg="WHITE")
        self.labelCustomer=Label(self.frame2,bg="WHITE")
        self.labelQty=Label(self.frame2,bg="WHITE")
        self.labelInfo=Label(self.frame2,bg="WHITE")
        self.labelBrand=Label(self.frame2,bg="WHITE")
        self.labelStock=Label(self.frame2,bg="WHITE")
        self.labelWarna=Label(self.frame2,bg="WHITE")
    
        self.labelDeadline.place(x=0.12*self.sW,y=0*(0.04*self.sH+(0.02*self.sW))+(0.16*self.sH),width=0.07*self.sW,height=0.05*self.sH)
        self.labelCustomer.place(x=0.12*self.sW,y=1*(0.04*self.sH+(0.02*self.sW))+(0.16*self.sH),width=0.07*self.sW,height=0.05*self.sH)
        self.labelQty.place(x=0.12*self.sW,y=2*(0.04*self.sH+(0.02*self.sW))+(0.16*self.sH),width=0.07*self.sW,height=0.05*self.sH)
        self.labelInfo.place(x=0.12*self.sW,y=3*(0.04*self.sH+(0.02*self.sW))+(0.16*self.sH),width=0.07*self.sW,height=0.05*self.sH)
       
        self.labelBrand.place(x=0.28*self.sW,y=0*(0.04*self.sH+(0.02*self.sW))+(0.16*self.sH),width=0.07*self.sW,height=0.05*self.sH)
        self.labelStock.place(x=0.28*self.sW,y=1*(0.04*self.sH+(0.02*self.sW))+(0.16*self.sH),width=0.105*self.sW,height=0.07*self.sH)
        self.labelWarna.place(x=0.28*self.sW,y=2*(0.04*self.sH+(0.02*self.sW))+(0.16*self.sH),width=0.07*self.sW,height=0.05*self.sH)
        
        self.labelDeadline.config(text=splitter(hasil['deadline']))
        self.labelCustomer.config(text=splitter(hasil['customer']))
        self.labelQty.config(text=splitter(hasil['qty']))
        self.labelInfo.config(text=splitter(hasil['info']))
        self.labelBrand.config(text=splitter(hasil['brand']))
        self.labelStock.config(text=splitter(hasil['stock']))
        self.labelWarna.config(text=splitter(hasil['warna']))
        
    def startPressed(self):
        global starFlag,tertekanFlag
        if starFlag==0:
            self.frame2.destroy()
            tertekanFlag=0
            starFlag=1
        else:
            self.startButton.config(command=self.nul)
            self.startButton.config(image=self.startPhoto2)

    def nul(self):
        pass
    def closePressed(self):
        global tertekanFlag
        self.frame2.destroy()
        tertekanFlag=0
    def Exit(self,event):
        global tertekanFlag
        self.frame2.destroy()
        tertekanflag=0
    def pausePressed(self):
        global z
    #kalkulator
        self.frame3=Frame(self.frame2,bg='#1687A7')
        self.frame3.place(x=(0.41*self.sW)*0.5,y=(self.sH*0.79)*0.5,anchor=CENTER,width=self.sW*0.28,height=0.46*self.sH)
        self.btnKal = [[0 for x in range(4)] for x in range(4)]
        for j in range(3):
            for i in range(3):
                z=z+1
               # print(z)
                self.btnKal[i][j] = Button(self.frame3,text=z,bg="#E7EBF0",fg='#1687A7',font=25)
                self.btnKal[i][j].place(x=i*((0.055*self.sW)+(0.011*self.sW))+(0.0097*self.sW), y=j*(0.0156*self.sH+0.078*self.sH)+(0.165*self.sH), width=0.055*self.sW, height=0.078*self.sH)
        self.btnKal0 = Button(self.frame3,text="0",bg="#E7EBF0",fg='#1687A7',font=25,command=lambda:self.input(0))
        self.btnKal0.place(x=0.21*self.sW, y=0.352*self.sH, width=0.055*self.sW, height=0.078*self.sH,anchor= NW)

        self.btnKalEnter = Button(self.frame3,text="\n".join("ENTER"),bg="#E7EBF0",fg='#1687A7',font=25,command = self.enter)
        self.btnKalEnter.place(x=0.21*self.sW, y=0.165*self.sH, width=0.055*self.sW, height=0.172*self.sH,anchor= NW)

        self.btnKalDel = Button(self.frame3,text="DEL",bg="#E7EBF0",fg='#1687A7',font=25,command=self.Delpressed)
        self.btnKalDel.place(x=0.21*self.sW, y=0.01*self.sH, width=0.055*self.sW, height=0.13*self.sH,anchor= NW)

        self.btnKal[0][0].config(command=lambda:self.input(1))
        self.btnKal[1][0].config(command=lambda:self.input(2))
        self.btnKal[2][0].config(command=lambda:self.input(3))
        self.btnKal[0][1].config(command=lambda:self.input(4))
        self.btnKal[1][1].config(command=lambda:self.input(5))
        self.btnKal[2][1].config(command=lambda:self.input(6))
        self.btnKal[0][2].config(command=lambda:self.input(7))
        self.btnKal[1][2].config(command=lambda:self.input(8))
        self.btnKal[2][2].config(command=lambda:self.input(9))


        self.kalLab=Label(self.frame3,bg="WHITE",text="",fg='#1687A7',font='Helvetica 50 bold')
        self.kalLab.place(x=0.0097*self.sW,y=0.0117*self.sH,width=0.19*self.sW,height=0.134*self.sH)
        z=0
        
    def finishPressed(self):
        global tertekanFlag
        response=messagebox.askokcancel("messageBox","Apakah Anda yakin sudah menyelesaikan tugas?")
        #print(response)
        if response==True:
            self.frame2.destroy()
            tertekanFlag=0
    def enter(self):
        global operator
        self.frame3.destroy()
        #print(operator)
        operator=""
    def Delpressed(self):
        global operator
        operator=""
        self.kalLab.config(text=operator)
    def input(self,x):
        global operator
        operator=operator+str(x)

        #print(operator)
        self.kalLab.config(text=operator)
      


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
