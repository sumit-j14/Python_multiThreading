import threading
from threading import Thread


def func1_thread1():
    for i in range(5):
        print("user thread_id ", end="")
        print(str(threading.get_native_id()) + "  first user thread: " + str(i))


def func2_thread2():
    for i in range(5):
        print("user thread_id ", end="")
        print(str(threading.get_native_id()) + " second user thread: " + str(i))


def mainfunc():
    thread1 = Thread(target=func1_thread1)
    thread2 = Thread(target=func2_thread2)
    thread1.start()
    thread2.start()
    thread1.join()
    thread2.join()


mainfunc()
