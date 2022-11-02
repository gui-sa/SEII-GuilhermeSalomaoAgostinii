#Running Assincrounously....
from asyncio import threads
import threading
import time

start = time.perf_counter() #returns 

def do_something(seconds):
    print(f'Sleeping {seconds} second(s)...')
    time.sleep(seconds) 
    print('Done Sleeping')


threads = [] #To joint them, in here... 

for _ in range(10):
    t = threading.Thread(target=do_something, args=[1.5]) #args are passed thru key argument that accepts a list for args and dict for kwargs
    t.start()
    threads.append(t)


for thread in threads:
    thread.join()


finish = time.perf_counter()
print(f'Finished in {round(finish-start,2)} second(s)')

#Stills finish in one seconds... even when calling 10 IO bounds tasks
