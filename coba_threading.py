import threading
print("bisa kok")
import time
import queue
flagThread=0
def delay5():
    event.set()
    print("mulai 5 detik")  
    time.sleep(5)
    print("selesai")
    event.clear()

def penyela():  
    #event.wait()
    if event.is_set():
        print("tersela ni ges yak")

event = threading.Event()

t1= threading.Thread(target=delay5)
t2= threading.Thread(target=penyela)
t1.start()
t2.start()
