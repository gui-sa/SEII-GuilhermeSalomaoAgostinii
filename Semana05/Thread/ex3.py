#Running Assincrounously....
from asyncio import threads
import threading
import time

start = time.perf_counter() #returns 

def do_something():
    print('Sleeping 1 second...')
    time.sleep(1) #sleep for 1 second.. This function puts you program im IO bounds.
    print('Done Sleeping')


threads = [] #To joint them, in here... 

for _ in range(10):
    t = threading.Thread(target=do_something)
    t.start()
    threads.append(t)


for thread in threads:
    thread.join()


finish = time.perf_counter()
print(f'Finished in {round(finish-start,2)} second(s)')

#Stills finish in one seconds... even when calling 10 IO bounds tasks
