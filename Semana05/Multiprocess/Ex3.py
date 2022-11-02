import time
import multiprocessing

#Assincronously

start = time.perf_counter() #returns 

def do_something(seconds):
    print(f'Sleeping {seconds} second(s)...')
    time.sleep(seconds) #sleep for x second.. This function puts you program im IO bounds.
    print('Done Sleeping')

processes = []

for _ in range(10): #Creating processess
    p = multiprocessing.Process(target=do_something, args=[1.5])
    processes.append(p) #putting the pointer of the objects inside a list to dont lose its pawn
    p.start() #Starts them up

for proces in processes:
    proces.join() #With the pointer inside the list, just join them all.

finish = time.perf_counter()
print(f'Finished in {round(finish-start,2)} second(s)')


#Computer will alocate them in the available cpus.
#It returned in 1.5 seconds... It wal actually slower then the threaded one... Probably because to do process stuff, cpu wast more time... 