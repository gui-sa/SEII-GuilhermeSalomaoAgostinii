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
    results = executor.map(do_something,secs)# do the same as before 
    
    #for result in results: #context manager deals with that...
    #    print(result) #will print them at same time... however it has not run in the same time
    

finish = time.perf_counter()
print(f'Finished in {round(finish-start,2)} second(s)')
 