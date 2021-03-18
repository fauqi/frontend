import threading
print("bisa kok")
import time

def delay5():
    event.set()
    print("mulai 5 detik")  
    time.sleep(5)
    print("selesai")
    event.clear()
def penyela():  
    event.wait()
    if event.is_start == True:
        print("tersela ni ges yak")

event = threading.Event()
t1= threading.Thread(target=delay5)
t2= threading.Thread(target=penyela)
delay5()
