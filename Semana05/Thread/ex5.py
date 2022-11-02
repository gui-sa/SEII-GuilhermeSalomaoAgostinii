#Running Assincrounously....
from asyncio import as_completed
import concurrent.futures
import time

start = time.perf_counter() #returns 

def do_something(seconds):
    print(f'Sleeping {seconds} second(s)...')
    time.sleep(seconds) 
    return "Done Sleeping"



with concurrent.futures.ThreadPoolExecutor() as executor: #let you access the return of the funtions runned
    secs = [5,4,3,2,1]
    results = [executor.submit(do_something,sec) for sec in secs] #creates a list of five elements... five threads beginning with 5, then 4,3,2 and 1... each element in there is a thread with executor in which permits controlling it better

    for f in concurrent.futures.as_completed(results):
        print(f.result())




#threads = [] #To joint them, in here... 
#
#for _ in range(10):
#    t = threading.Thread(target=do_something, args=[1.5]) #args are passed thru key argument that accepts a list for args and dict for kwargs
#    t.start()
#    threads.append(t)
#
#
#for thread in threads:
#    thread.join()
#

finish = time.perf_counter()
print(f'Finished in {round(finish-start,2)} second(s)')
 