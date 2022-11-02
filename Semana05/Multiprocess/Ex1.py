import time
#Sincronously

start = time.perf_counter() #returns 

def do_something():
    print('Sleeping 1 second...')
    time.sleep(1) #sleep for 1 second.. This function puts you program im IO bounds.
    print('Done Sleeping')

do_something()
do_something()

finish = time.perf_counter()
print(f'Finished in {round(finish-start,2)} second(s)')

#Using multiprocessing when you want to significantly speed up a process. It literally creates processess... With a new thread of python
#REF: https://www.youtube.com/watch?v=fKl2JW_qrso
#It is highly recoomended for IO bounded process...
 