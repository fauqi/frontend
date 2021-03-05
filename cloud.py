print("lontong")
import requests
import json
import urllib3
from tkinter import*
from PIL import ImageTk, Image
import io

dataku = requests.get("https://indowella.com/new/public/api/v1/get-customers")
dataku = requests.get("https://indowella.com/new/public/api/v1/get-project")
#print(dataku.json())
dataku_objek = json.dumps(dataku.json(),sort_keys=True,indent=4)
print(dataku_objek)
result =dataku.json()

# result=[
#     {   
#         "brand": "balibul aqiqah",
#         "customer": "anieta",
#         "deadline": "Senin, 08 maret  2021",
#         "image": "https://indowella.com/new/public/",
#         "info": "2 sisi atau lebih screen :",
#         "is_stock": False,
#         "qty": "2000 pcs",
#         "stock": "[balibul aqiqah] sablon  #10 oz hok",
#         "warna": "hitam -"
#     },
#     {
#         "brand": "joja house",
#         "customer": "johanes",
#         "deadline": "Jum'at, 05 maret  2021",
#         "image": "https://indowella.com/new/public/desain/20210303043450-joja house baru 2 warna.JPG",
#         "info": "2 sisi atau lebih screen :B4",
#         "is_stock": False,
#         "qty": "500 pcs",
#         "stock": "[joja house] sablon 14 HOKKAKU OV",
#         "warna": "hitam kuning"
#     },
#     {
#         "brand": "padma",
#         "customer": "andrea",
#         "deadline": "Minggu, 07 maret  2021",
#         "image": "https://indowella.com/new/public/desain/20210303073346-padma 14oz oval wita.JPG",
#         "info": "2 sisi atau lebih screen :",
#         "is_stock": False,
#         "qty": "1000 pcs",
#         "stock": "[padma] sablon 14 Wita OV",
#         "warna": "hitam -"
#     },
#     {
#         "brand": "Dzaice",
#         "customer": "candra",
#         "deadline": "Minggu, 07 maret  2021",
#         "image": "https://indowella.com/new/public/",
#         "info": "2 sisi atau lebih screen :",
#         "is_stock": False,
#         "qty": "500 pcs",
#         "stock": "[Dzaice] sablon 22 Mcup D L",
#         "warna": "hitam -"
#     },
#     {
#         "brand": "inikah rasanya",
#         "customer": "Fajar ibnu",
#         "deadline": "Minggu, 07 maret  2021",
#         "image": "https://indowella.com/new/public/",
#         "info": "2 sisi atau lebih screen :B2",
#         "is_stock": False,
#         "qty": "1000 pcs",
#         "stock": "[inikah rasanya] sablon 16 HOKKAKU OV",
#         "warna": "hitam -"
#     },
#     {
#         "brand": "tebus haus",
#         "customer": "surya",
#         "deadline": "Minggu, 07 maret  2021",
#         "image": "https://indowella.com/new/public/desain/20201019085135-tebus haus 16starindo 5gr.PNG",
#         "info": "2 sisi atau lebih screen :",
#         "is_stock": False,
#         "qty": "500 pcs",
#         "stock": "[tebus haus] sablon 16 SI D 5g",
#         "warna": "hitam -"
#     },
#     {
#         "brand": "tebus haus",
#         "customer": "surya",
#         "deadline": "Minggu, 07 maret  2021",
#         "image": "https://indowella.com/new/public/desain/20201019085135-tebus haus 16starindo 5gr.PNG",
#         "info": "2 sisi atau lebih screen :",
#         "is_stock": False,
#         "qty": "500 pcs",
#         "stock": "[tebus haus] sablon 16 SI D 5g",
#         "warna": "hitam -"
#     },
#     {
#         "brand": "nyeker",
#         "customer": "adtya",
#         "deadline": "Rabu, 10 maret  2021",
#         "image": "https://indowella.com/new/public/",
#         "info": "1 sisi screen :",
#         "is_stock": False,
#         "qty": "500 pcs",
#         "stock": "[nyeker] sablon box burger",
#         "warna": "hitam -"
#     },
#     {
#         "brand": "protiga",
#         "customer": "taufiq",
#         "deadline": "Sabtu, 06 maret  2021",
#         "image": "https://indowella.com/new/public/desain/20210302083954-protiga.PNG",
#         "info": "2 sisi atau lebih screen :",
#         "is_stock": False,
#         "qty": "1000 pcs",
#         "stock": "[protiga] sablon 16 HOKKAKU OV",
#         "warna": "hitam -"
#     },
#     {
#         "brand": "protiga",
#         "customer": "taufiq",
#         "deadline": "Sabtu, 06 maret  2021",
#         "image": "https://indowella.com/new/public/desain/20210302084040-protiga sealcup.PNG",
#         "info": "1 sisi screen :",
#         "is_stock": False,
#         "qty": "1 roll",
#         "stock": "[protiga] sablon seal cup (1000)",
#         "warna": "hitam -"
#     }
# ]
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
# photo=Image.open("beranda.png")
# photo = photo.resize((200, 100), Image.ANTIALIAS)
# gambar = ImageTk.PhotoImage(photo)

# gambar=loadImageWebPublic(result[1]['image'],0,80)
# labelImage=Label(frame,text="LONTONG",height=100,width=200,bg="BLUE",image=gambar)
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
