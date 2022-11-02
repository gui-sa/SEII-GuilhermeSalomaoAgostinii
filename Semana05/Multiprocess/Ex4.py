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
    #f1 = executor.submit(do_something,1.5)#submit creat1es a future... a promise of something will be returned ... WHen it is done we can grab the result!!!
    #f2 = executor.submit(do_something,1.5)#submit creat1es a future... a promise of something will be returned ... WHen it is done we can grab the result!!!
    
    #print(f1.result()) #grabs the result one completed... Or promise returned!
    #print(f2.result()) #grabs the result one completed... Or promise returned!
    secs = [5,4,3,2,1]
    
    results = [executor.submit(do_something, sec) for sec in secs]#List comprehension.
    for f in concurrent.futures.as_completed(results):
        print(f.result()) 


finish = time.perf_counter()
print(f'Finished in {round(finish-start,2)} second(s)')

# It takes more time because CPU takes time realocating between them! (for smaller tasks)