#Running Sincronously....
import time

start = time.perf_counter() #returns 

def do_something():
    print('Sleeping 1 second...')
    time.sleep(1) #sleep for 1 second.. This function puts you program im IO bounds.
    print('Done Sleeping')

do_something()
do_something()

finish = time.perf_counter()
print(f'Finished in {round(finish-start,2)} second(s)')


#Use threading when want run diferents tasks concurrently improving the program perfonrmance.
#REF: https://www.youtube.com/watch?v=IEEhzQoKtQU
#IO bounds: reading/writing files, reading from WEB...
#You need to know that to create a thread, you need to organize 
#It just creates a ILUSION (in python), because there are just one interpreter... SIngle threaded, however it improves when it dont use CPU... In other words, it is IO bounds.
#If you use Thread for CPU bounds tasks, you can reduce process performance due that.
#