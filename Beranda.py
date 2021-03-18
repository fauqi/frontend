from cloud import *
from cloud import result
from tkinter import messagebox
from coba_threading import *


tertekanFlag=0
k=0
c=0
z=0
flag =0
starFlag=0
stock=False
operator=""
lastUpdate=0
#nyoba commit
#nyoba commit 2
SCREENWIDTH = int(lontong.winfo_screenwidth())
SCREENHEIGHT = int(lontong.winfo_screenheight())
lontong.geometry("{0}x{1}+0+0".format(SCREENWIDTH, SCREENHEIGHT))
getKaryawan()
#print(arrayKaryawan[2]['nama'])

#print(url)
def splitter(s,maksChar):
    total =0
    result=""
    c = s.split()
    for i in range(len(c)):
        counter=len(c[i])
        total=total+counter
       # print(total)
        if(total<maksChar):
            result=result+" "+c[i]
        else :
            result=result+"\n"+c[i]
            total=0
    return (result)

class Beranda:
    def __init__(self,master):
        self.master=master
        self.master.title("apanihman")
        self.pegawai=["Imam","Aji","Roni","MBAK bi"]
        self.sW=SCREENWIDTH
        self.sH=SCREENHEIGHT
        self.frame=Frame(self.master,bg="#f9f9f9")
        self.showLayar()
        self.btnTask =[[0 for x in range(88)]  for x in range(5)]

        for i in range(5):
            for j in range(88):    
                self.btnTask[i][j] = Button(self.frame,text="hallo")            
                  
        
    
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

    def switch(self,dataReady):
        global stock
        url = "/api/v1/mutation-stock"
        if self.dataReady['is_stock']== True:
            self.dataReady['is_stock']= False
            query = dict(zip(( 'id','is_stock'), (self.identify,"0")))
            
            self.switch_btn.config(image=self.switch_tidak_ada)
        else:
            self.dataReady['is_stock']= True
            self.switch_btn.config(image=self.switch_ada)
            query = dict(zip(( 'id','is_stock'), (self.identify,"1")))
        httpPost(url,query)
    def tertekan(self,hasil,identify,nomor,id_karyawan):
        global stock,tertekanFlag,server
        self.identify=identify
        self.id_karyawan=id_karyawan
        self.url = server+"/api/v1/get-project?id="+ str(identify)
        self.data= requests.get(self.url)
        self.dataReady  = self.data.json()
        dataReady=self.dataReady
        
        #print(self.dataReady['image'])

        
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
            self.photoLabel=Label(self.frame2,bg="RED")
            self.photoLabel.place(x=0.062*self.sW,y=0.45*self.sH,width=0.3*self.sW,height=0.23*self.sH)

    #startButton
        self.photo10=Image.open("cancel.png")
        self.photo10=self.photo10.resize((int(0.1*self.sW),int(0.057*self.sH)),Image.ANTIALIAS)
        self.startPhoto2=ImageTk.PhotoImage(self.photo10)
        self.photo3=Image.open("start.png")
        self.photo3=self.photo3.resize((int(0.1*self.sW),int(0.057*self.sH)),Image.ANTIALIAS)

        self.startPhoto=ImageTk.PhotoImage(self.photo3)
        self.startButton=Button(self.frame2,image = self.startPhoto,borderwidth=0,bg="WHITE",command=lambda:self.startPressed(nomor))
        self.startButton.place(x=0.08*self.sW,y=self.sH*0.68,width=0.12*self.sW,height=0.08*self.sH,anchor=NW)
        if self.dataReady['is_start']==True:
            self.startButton.config(image=self.startPhoto2)
        else:
            self.startButton.config(image=self.startPhoto)

    #finishButton
        self.photo8=Image.open("finish.png")
        self.photo8=self.photo8.resize((int(0.1*self.sW),int(0.057*self.sH)),Image.ANTIALIAS)
        self.finishPhoto=ImageTk.PhotoImage(self.photo8)
        self.finishButton=Button(self.frame2,image = self.finishPhoto,borderwidth=0,bg="WHITE",command=lambda:self.finishPressed(nomor,id_karyawan))
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
        self.pauseButton=Button(self.frame2,image = self.pausePhoto,borderwidth=0,bg="WHITE",command=lambda:self.pausePressed(id_karyawan))
        self.pauseButton.place(x=0.644*(self.sW*0.41),y=(self.sH*0.82)*0.08,width=0.045*self.sW,height=0.063*self.sH,anchor=W)

            #switch widget
        self.photo6=Image.open("switch_ada.png")
        self.photo6= self.photo6.resize((int(0.06*self.sW),int(0.077*self.sH)), Image.ANTIALIAS)
        self.switch_ada= ImageTk.PhotoImage(self.photo6)
        self.photo7=Image.open("switch_tidak_ada.png")
        self.photo7= self.photo7.resize((int(0.06*self.sW),int(0.077*self.sH)), Image.ANTIALIAS)
        self.switch_tidak_ada= ImageTk.PhotoImage(self.photo7)
        self.switch_btn = Button(self.frame2,bg="WHITE",image=self.switch_tidak_ada,borderwidth=0,command=lambda:self.switch(self.dataReady))
        self.switch_btn.place(x=0.19*self.sW,y=0.03*self.sH,width=0.06*self.sW,height=0.077*self.sH)
        if self.dataReady['is_stock']==True:
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
        
        self.labelDeadline.config(text=splitter(self.dataReady['deadline'],15))
        self.labelCustomer.config(text=splitter(self.dataReady['customer'],15))
        self.labelQty.config(text=splitter(self.dataReady['qty'],15))
        self.labelInfo.config(text=splitter(self.dataReady['info'],15))
        self.labelBrand.config(text=splitter(self.dataReady['brand'],15))
        self.labelStock.config(text=splitter(self.dataReady['stock'],15))
        self.labelWarna.config(text=splitter(self.dataReady['warna'],15))
        
        try:
            self.picturePopup=loadImageWebPublic(self.dataReady['image'],0,0.21*self.sH)
            self.photoLabel.config(image=self.picturePopup,bg="WHITE")
        except:
            self.fotoLabel=Image.open("no image.png")
            self.fotoLabel=self.fotoLabel.resize((int(0.13*self.sW), int(0.21*self.sH)), Image.ANTIALIAS)
            self.gambarLabel= ImageTk.PhotoImage(self.fotoLabel)
            #print("no image bro")
            self.photoLabel.config(image=self.gambarLabel,bg="WHITE")

    def startPressed(self,nomor):
        global starFlag,tertekanFlag
        url="/api/v1/start-project"
        self.a = self.dataReady['is_start']

        #print(self.dataReady['is_start'])
        if self.dataReady['is_start']==False:
            self.frame2.destroy()
            tertekanFlag=0
            query= dict(zip(( 'id',""), (self.identify,"")))
            httpPost(url, query)

        elif self.dataReady['is_start']==True:
            #print("cancel tertekan")
            url= "/api/v1/cancel-start-project"
            query= dict(zip(( 'id',""), (self.identify,"")))
            httpPost(url, query)
            self.frame2.destroy()
            tertekanFlag=0
        

        result=requests.get(server+"/api/v1/get-project?karyawan_id="+str(arrayKaryawan[nomor]['id']))
        result=result.json()
        #print (arrayKaryawan[nomor]['id'])
        appendCad(nomor,result['data'],1)

        
    def cancel(self):
        pass
    def closePressed(self):
        global tertekanFlag
        self.frame2.destroy()
        tertekanFlag=0
    def Exit(self,event):
        global tertekanFlag
        self.frame2.destroy()
        tertekanflag=0
    def pausePressed(self,id_karyawan):
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

        self.btnKalEnter = Button(self.frame3,text="\n".join("ENTER"),bg="#E7EBF0",fg='#1687A7',font=25,command = lambda:self.enter(id_karyawan))
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
        
    def finishPressed(self,nomor,id_karyawan):
        global tertekanFlag,jumlahJob
        if self.dataReady['is_stock']== False:
            messagebox.showerror("warning","Silahkan mutasi dulu stocknya")
            # self.frame2.destroy()
            # tertekanFlag=0
        else :
            response=messagebox.askokcancel("messageBox","Apakah Anda yakin sudah menyelesaikan tugas?")
            #print(response)
            # print(id_karyawan)
            if response==True:
                self.frame2.destroy()
                tertekanFlag=0
                url = "/api/v1/production-stock"
                
                query = dict(zip(( 'id','is_finish','qty','karyawan_id'), (self.identify,True,self.dataReady['qty'],id_karyawan)))
                result=requests.get(server+"/api/v1/get-project?karyawan_id="+str(arrayKaryawan[nomor]['id']))
                httpPost(url,query)
                result=result.json()
                # appendCad(nomor,result,1)
                karyawanReq(nomor)
    def enter(self,id_karyawan):
        global operator
        self.qty=operator
        url = "/api/v1/production-stock"
        query = dict(zip(( 'id','qty','karyawan_id'), (self.identify,self.qty,id_karyawan)))
        httpPost(url,query)

        response=messagebox.askokcancel("messageBox","Apakah Anda yakin sudah mengerjakan "+self.qty+" pcs?")
        #print(response)
        if response==True:
            self.frame3.destroy()
            operator=""
            httpPost(url,query)
            self.frame3.destroy()
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

# jumlahJob=len(result)

def appendCad(bariskaryawan,result,karyawan_id,kontainer=1,delete=0):
 
    global k,gambar
    maksJob=7
    #print(karyawan_id)
    jumlahJob=len(result)
    
    wContainer=0.843 * b.sW

    for i in range(87):
        b.btnTask[bariskaryawan][i].place_forget()
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
        # print("jumlah container"+str(i)+"="+str(containerJob[i]))
    jumlahItem=containerJob[0]
    icontainer=0
    x=0

    # print("mulai \r\n")
    for i in range(jumlahJob):
        b.btnTask[bariskaryawan][i].config(command=lambda:b.tertekan(result[i]))
        
        if(x>=(containerJob[icontainer]-1)):
            icontainer=icontainer+1
        sigmaContainerTerlewat=0
        for m in range(icontainer):
            sigmaContainerTerlewat=sigmaContainerTerlewat+containerJob[m]

        x=i-sigmaContainerTerlewat
        
        panjangButton=(wContainer-((0.01*b.sW)+((jumlahItem+1)*0.01*b.sW)))/containerJob[icontainer]
    
        offsetH=0.164*b.sH + (bariskaryawan*0.180*b.sH)
        offsetW=0.163*b.sW      
              
        b.btnTask[bariskaryawan][i].place(x=(x)*(panjangButton+(0.01*b.sW))+offsetW,y=((int(icontainer)*0.180*b.sH)+offsetH),width=panjangButton,height=0.158*b.sH) 
        #print("i="+str(i) +",x="+str(x)+",sigma="+str(sigmaContainerTerlewat) +",icontainer= " + str(icontainer))
        x=i
        # try:
        #     gambar[x]=loadImageWebPublic(result[x]['image'],0,80)
        #     btnTask[i].config(image=gambar[x])
    
        # except:
        #     print("no Image")
        #     photo=Image.open("no image.png")
        #     photo =photo.resize((80, 80), Image.ANTIALIAS)
        #     gambar[x]= ImageTk.PhotoImage(photo)
        #     btnTask[i].config(image=gambar[x])
        text = splitter(result[i]['stock'],8)
        #print(result[i]['is_start'])
        if result[i]['is_start']==True:
            background="GREEN"
        else:
            background="#11698E"
        # print("buat button lo ini cuy "+str(bariskaryawan)+"-"+str(i))
        # print(b.btnTask[bariskaryawan][i])
        b.btnTask[bariskaryawan][i].config(command=lambda x=i,id=result[x]['id'],nomor=bariskaryawan,karyawan_id=karyawan_id:b.tertekan(result[x],id,nomor,karyawan_id),text =text,bg =background,fg="WHITE",font='Roboto 12 bold')
    

def listKaryawan():
    global arrayKaryawan

    
    

    labelPegawai=[0 for z in range(len(arrayKaryawan))]
    labelUser=[0 for y in range(len(arrayKaryawan))]
   # print(len(arrayKaryawan))
    for j in range(len(arrayKaryawan)):
        #print(j)
        labelPegawai[j]= Label(b.frame,text = arrayKaryawan[j]['nama'],bg="WHITE",fg='#1687A7',font=10)
        labelPegawai[j].place(x=0.085*b.sW,y=j*((0.078*b.sH)+0.09*b.sH)+(0.243*b.sH),width=0.056*b.sW,height=0.078*b.sH,anchor=W)
        labelUser[j]= Label(b.frame,text="Lontong",image = b.userGambar,bg="WHITE")
        labelUser[j].place(x=0.0285*b.sW,y=j*((0.078*b.sH)+0.09*b.sH)+(0.243*b.sH),width=0.056*b.sW,height=0.078*b.sH,anchor=W)
    

def karyawanReq(karyawan):
       # print(karyawan)
        global lastUpdate
        url = server+"/api/v1/get-project?karyawan_id="+str(arrayKaryawan[karyawan]['id'])
        result=requests.get(server+"/api/v1/get-project?karyawan_id="+str(arrayKaryawan[karyawan]['id']))
        result=result.json()
        # print(result)
        karyawan_id = arrayKaryawan[karyawan]['id']
        appendCad(karyawan,result['data'],karyawan_id)

def refresh():
    
    for i in range(len(arrayKaryawan)):
        karyawanReq(i)
# tryButton = Button(b.frame,text= "mbak bi",command = refresh)
# tryButton.place(x=200,y=50,width=50,height=50)

def rutinCekFlag():
    global lastUpdate
    result=requests.get(server+"/api/v1/get-update-flag?date="+str(lastUpdate))
    result=result.json()
    lastUpdate=result['last_updated']
    LastUpdateLabel=Label(b.frame,text = "Last Update:\n "+str(lastUpdate),bg="WHITE")
    LastUpdateLabel.place(x=0.85*b.sW,y=0.024*b.sH) 
    # print(result)
    if result['flag'] == 1:
        refresh()
    b.frame.after(3000,rutinCekFlag)
refresh()
rutinCekFlag()
    
listKaryawan()

lontong.mainloop()
      


