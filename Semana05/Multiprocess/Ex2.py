
import time
import multiprocessing

#Assincronously

start = time.perf_counter() #returns 

def do_something():
    print('Sleeping 1 second...')
    time.sleep(1) #sleep for 1 second.. This function puts you program im IO bounds.
    print('Done Sleeping')

p1 = multiprocessing.Process(target=do_something) #Create a process object
p2 = multiprocessing.Process(target=do_something)

p1.start() #Starts process 
p2.start()

p1.join() #Awaits for the child process to finish right here.
p2.join()

finish = time.perf_counter()
print(f'Finished in {round(finish-start,2)} second(s)')
