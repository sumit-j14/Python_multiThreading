import threading
from threading import Thread
import time


def func1_thread1():
    for i in range(10):
        # sleep imitates I/O task
        time.sleep(2)
        print("user thread_id ", end="")
        print(str(threading.get_native_id()) + " first thread: " + str(i))


def func2_thread2():
    for i in range(10):
        time.sleep(2)
        print("user thread_id ", end="")
        print(str(threading.get_native_id()) + " second thread: " + str(i))


def mainfunc():
    start_time = time.time()
    func1_thread1()
    func2_thread2()
    end_time = time.time()
    result = end_time - start_time
    print("time taken ", result, "seconds")


mainfunc()
