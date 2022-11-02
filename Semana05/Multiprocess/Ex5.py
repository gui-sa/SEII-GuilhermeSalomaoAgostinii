from asyncio import as_completed
import time
import concurrent.futures

#Assincronously

start = time.perf_counter() #returns 

def do_something(seconds):
    print(f'Sleeping {seconds} second(s)...')
    time.sleep(seconds) #sleep for x second.. This function puts you program im IO bounds.
    return f'Done Sleeping...{seconds}'

with concurrent.futures.ProcessPoolExecutor() as executor:  #with IS a context manager!!!!!!!!!
    secs = [5,4,3,2,1]
    results = executor.map(do_something,secs) #will run every element present in secs in  do_something.... just creating instances
    for result in results:
        print(result) #Here is the place to handle with exceptions

finish = time.perf_counter()
print(f'Finished in {round(finish-start,2)} second(s)')

# It takes more time because CPU takes time realocating between them! (for smaller tasks)