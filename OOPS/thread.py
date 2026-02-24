#threading - execution of tasks
#multitherading - execution of many tasks at a time - concurrent execution
#process - execution unit
#threads - light weight unit inside the process
#simle thread

import threading
import time

def task ():
    print("Thread started")
    time.sleep(2)
    print("Thread finished")

t = threading.Thread(target = task)
t.start()
t.join()
print("Thread terminated")





