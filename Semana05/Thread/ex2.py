#Running Assincrounously....
import threading
import time

start = time.perf_counter() #returns 

def do_something():
    print('Sleeping 1 second...')
    time.sleep(1) #sleep for 1 second.. This function puts you program im IO bounds.
    print('Done Sleeping')

t1 = threading.Thread(target=do_something) #Create a thread object that runs do_something function
t2 = threading.Thread(target=do_something)
t1.start() #Start running the thread
t2.start()
t1.join() #Wait the thread to finish... and returns here.. It is made for threading
t2.join() #Wait function is for multiprocessing tasks

finish = time.perf_counter()
print(f'Finished in {round(finish-start,2)} second(s)')


#In this case the time will reduce... Not because it has not wait 1 second each, but, because the cpu started the IO bound on the same time




