from time import sleep
from threading import Thread
def task():
    sleep(2)

    print("This is from the another thread")

thread=Thread(target=task)

thread.start()

print("this is the main thread")
thread.join()
