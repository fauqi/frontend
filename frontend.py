import requests
import json
import urllib3
from tkinter import *
from PIL import ImageTk, Image

lontong=Tk()
SCREENWIDTH = int(lontong.winfo_screenwidth())
SCREENHEIGHT = int(lontong.winfo_screenheight())

print(SCREENWIDTH)
lontong.geometry("{0}x{1}+0+0".format(SCREENWIDTH, SCREENHEIGHT))
class Beranda:
    def __init__(self,master):
        self.master=master
        self.master.title("apanihman")

    def showLayar(self):
        self.frame=Frame(self.master,bg="#f9f9f9")
        self.frame.place(x=0,y=0,height=SCREENHEIGHT,width=SCREENWIDTH,anchor=NW)
        self.photo=Image.open("beranda.png")
        self.photo = self.photo.resize((SCREENWIDTH, SCREENHEIGHT), Image.ANTIALIAS)
        self.gambar = ImageTk.PhotoImage(self.photo)
     
        self.labelImage=Label(self.frame,text="LONTONG",height=SCREENHEIGHT,width=SCREENWIDTH,bg="BLUE",image=self.gambar)
        self.labelImage.place(x=0,y=0,height=SCREENHEIGHT,width=SCREENWIDTH,anchor=NW)
        self.btn=Button(self.frame,text="lontong")

       # self.frame.bind('<Button-1>', self.Exit)
       # self.btn.place(x=200,y=200,width= 50,height=50)
        self.sW=SCREENWIDTH
        self.sH=SCREENHEIGHT
        self.rW=int(self.sW*0.41)
        self.rH=int(self.sH*0.822)
        print(self.rH)
        self.photo11=Image.open("lontong.png")
        self.gambar2 = ImageTk.PhotoImage(self.photo11)
        self.btnTask = [[0 for x in range(4)] for x in range(4)]

        for i in range(4):
            for j in range(4):
                self.btnTask[i][j] = Button(self.frame,image = self.gambar2,text="hallo "+str(i)+str(j),command = self.tertekan)
                self.btnTask[i][j].place(x=i*(0.205*self.sW)+(0.163*self.sW), y=j*(0.168*self.sH)+(0.174*self.sH), width=0.195*self.sW, height=0.158*self.sH)
    def tertekan(self):
        self.photo2=Image.open("popup.png")
        self.photo2 = self.photo2.resize((self.rW,self.rH), Image.ANTIALIAS)
        self.gambar3 = ImageTk.PhotoImage(self.photo2)
        self.frame2=Frame(self.master)
        self.frame2.place(x=(self.sW*0.5),y=(self.sH*0.5),height=self.sH*0.79,width=self.sW*0.41,anchor=CENTER)
        self.label2 = Label(self.frame2,text="LONTONG",bg="WHITE",image=self.gambar3,borderwidth=4)
        self.label2.place(x=0,y=0,height=self.sH*0.79,width=self.sW*0.41,anchor=NW)
        
        self.photo3=Image.open("start.png")
        self.photo3=self.photo3.resize((int(0.1*self.sW),int(0.057*self.sH)),Image.ANTIALIAS)
        self.startPhoto=ImageTk.PhotoImage(self.photo3)
        self.startButton=Button(self.frame2,image = self.startPhoto,borderwidth=0,bg="WHITE",command=self.startPressed)
        self.startButton.place(x=(0.41*self.sW)*0.5,y=(self.sH*0.78)*0.88,width=0.12*self.sW,height=0.08*self.sH,anchor=N)
        
        self.photo4=Image.open("pause.png")
        self.photo4=self.photo4.resize((int(0.045*self.sW),int(0.063*self.sH)),Image.ANTIALIAS)
        self.pausePhoto=ImageTk.PhotoImage(self.photo4)
        self.pauseButton=Button(self.frame2,image = self.pausePhoto,borderwidth=0,bg="WHITE",command=self.pausePressed)
        self.pauseButton.place(x=0.644*(self.sW*0.41),y=(self.sH*0.82)*0.08,width=0.045*self.sW,height=0.063*self.sH,anchor=W)

        self.photo5=Image.open("centang.png")
        self.photo5=self.photo5.resize((int(0.045*self.sW),int(0.063*self.sH)),Image.ANTIALIAS)
        self.centangPhoto=ImageTk.PhotoImage(self.photo5)
        self.centangButton=Button(self.frame2,image = self.centangPhoto,borderwidth=0,bg="WHITE",command=self.pausePressed)
        self.centangButton.place(x=0.754*(self.sW*0.41),y=(self.sH*0.82)*0.08,width=0.045*self.sW,height=0.063*self.sH,anchor=W)
    def startPressed(self):
 
        self.frame2.destroy()
    def Exit(self,event):
        self.frame2.destroy()
    def pausePressed(self):
        self.frame3=Frame(self.frame2)
        self.frame3.place(x=(0.41*self.sW)*0.5,y=(self.sH*0.79)*0.5,anchor=CENTER,width=self.sW*0.28,height=0.46*self.sH)

b=Beranda(lontong)
b.showLayar()



lontong.mainloop()