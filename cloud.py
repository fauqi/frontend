print("lontong")
import requests
import json
import urllib3
from tkinter import*
from PIL import ImageTk, Image
import io
lontong=Tk()
# dataku = requests.get("https://indowella.com/new/public/api/v1/get-customers")
# dataku = requests.get("https://indowella.com/new/public/api/v1/get-project")
# #print(dataku.json())
# dataku_objek = json.dumps(dataku.json(),sort_keys=True,indent=4)
# print(dataku_objek)
# result =dataku.json()

result = [
    {
        "brand": "jeli julid",
        "customer": "fahmi",
        "deadline": "Sabtu, 06 maret  2021",
        "id": 6131,
        "image": "https://indowella.com/new/public/desain/20210106143031-jelijul.PNG",
        "info": "2 sisi atau lebih screen :C6",
        "is_stock": True,
        "qty": "2000 pcs",
        "stock": "[jeli julid] sablon 22 Hok D",
        "warna": "hitam -"
    },
    {
        "brand": "warung sleko",
        "customer": "Eki",
        "deadline": "Rabu, 10 maret  2021",
        "id": 6135,
        "image": "https://indowella.com/new/public/",
        "info": "1 sisi screen :",
        "is_stock": False,
        "qty": "500 pcs",
        "stock": "[warung sleko] sablon  #sterofoam merk Lux L01",
        "warna": "merah -"
    },
    {
        "brand": "belis",
        "customer": "pungky",
        "deadline": "Jum'at, 12 maret  2021",
        "id": 6142,
        "image": "https://indowella.com/new/public/",
        "info": "2 sisi atau lebih screen :",
        "is_stock": False,
        "qty": "1000 pcs",
        "stock": "[belis] sablon 14 SI D 5g",
        "warna": "merah -"
    },
    {
        "brand": "balibul aqiqah",
        "customer": "anieta",
        "deadline": "Senin, 08 maret  2021",
        "id": 6102,
        "image": "https://indowella.com/new/public/",
        "info": "2 sisi atau lebih screen :",
        "is_stock": False,
        "qty": "2000 pcs",
        "stock": "[balibul aqiqah] sablon  #10 oz hok",
        "warna": "hitam -"
    },
    {
        "brand": "we got you",
        "customer": "Bioderma ID tokopedia",
        "deadline": "Selasa, 09 maret  2021",
        "id": 6110,
        "image": "https://indowella.com/new/public/desain/20210305021902-mad.png",
        "info": "1 sisi screen :",
        "is_stock": False,
        "qty": "2000 pcs",
        "stock": "[we got you] sablon Paper Bag Putih Besar",
        "warna": "hitam -"
    },
    {
        "brand": "materia medica",
        "customer": "sofyan",
        "deadline": "Rabu, 10 maret  2021",
        "id": 6112,
        "image": "https://indowella.com/new/public/desain/20210304082953-materia medica 12.JPG",
        "info": "1 sisi screen :",
        "is_stock": False,
        "qty": "2500 pcs",
        "stock": "[materia medica] sablon 12 Hok D ",
        "warna": "hitam -"
    },
    {
        "brand": "materia medica",
        "customer": "sofyan",
        "deadline": "Rabu, 10 maret  2021",
        "id": 6113,
        "image": "https://indowella.com/new/public/desain/20210304083155-materia medica 14.JPG",
        "info": "1 sisi screen :",
        "is_stock": False,
        "qty": "2500 pcs",
        "stock": "[materia medica] sablon 14 HOKKAKU OV",
        "warna": "hitam -"
    },
    {
        "brand": "materia medica",
        "customer": "sofyan",
        "deadline": "Rabu, 10 maret  2021",
        "id": 6114,
        "image": "https://indowella.com/new/public/desain/20210304083332-sablon plastik.JPG",
        "info": "1 sisi screen :",
        "is_stock": False,
        "qty": "500 pcs",
        "stock": "[materia medica] sablon  #plastik 25*20",
        "warna": "hitam -"
    },
    {
        "brand": "warkop brewok",
        "customer": "mas rigel",
        "deadline": "Selasa, 09 maret  2021",
        "id": 6119,
        "image": "https://indowella.com/new/public/desain/20210305020305-warkop brewok.jpg",
        "info": "1 sisi screen :",
        "is_stock": False,
        "qty": "1000 pcs",
        "stock": "[warkop brewok] sablon Paper Bag Coklat Besar",
        "warna": "coklat tua -"
    },
    {
        "brand": "oukla coffee",
        "customer": "diah",
        "deadline": "Selasa, 09 maret  2021",
        "id": 6121,
        "image": "https://indowella.com/new/public/desain/20210305035700-oukla 360ml.JPG",
        "info": "2 sisi atau lebih screen :",
        "is_stock": False,
        "qty": "1000 pcs",
        "stock": "[oukla coffee] sablon Paper Bowl 360",
        "warna": "biru,coklat hitam"
    }
]
def loadImageWebPublic( url, w=0, h=0, mode=0):
    global location
    r = requests.get(url)
    print("load = %s" % url)

    img0 = (Image.open(io.BytesIO(r.content)))
    if w == 0 and h == 0:

        bgG = img0.resize((int(img0.width * 1), int(img0.height * 1)), Image.ANTIALIAS)
    elif w==0:
        scale=h/img0.height
        bgG = img0.resize((int(img0.width * scale), int(img0.height * scale)), Image.ANTIALIAS)
    elif h==0:
        scale=w/img0.width
        bgG = img0.resize((int(img0.width * scale), int(img0.height * scale)), Image.ANTIALIAS)
    else:
        bgG = img0.resize((w, h), Image.ANTIALIAS)
    if mode == 0:  # tkphotoImage
        bgG = ImageTk.PhotoImage(bgG.convert('RGB'))
    return (bgG)
# m=Tk()
# #print(data_customers)
# frame=Frame(m)


# frame.place(x=0,y=0,width=500,height=500)

# labelImage=Label(frame,text="LONTONG",height=100,width=200,bg="BLUE",image=gambar10)
# labelImage.place(x=0,y=0,height=100,width=200,anchor=NW)
# m.mainloop()









#http = urllib3.PoolManager()
# url = "https://indowella.com/new/public/api/v1/get-customers"
# resp = http.request('GET', url)
# print(resp.data.decode('utf-8'))
#print(response.json())
#parsed_json = json.loads(response.json())
#print(parsed_json)
# def jprint(obj):
#     # create a formatted string of the Python JSON object
#     text = json.dumps(obj, sort_keys=True, indent=4)
#     print(text)
   
# jprint(response.json())
# print (getattr(jprint,'id')) 
 #print(type(response.json()))
 #print(json.load("https://indowella.com/new/public/api/v1/get-customers"))
