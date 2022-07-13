import threading

def func1_thread1():
    for i in range(5):
        print("user thread_id ", end="")
        print(str(threading.get_native_id()) + "  first user thread: " + str(i))


def func2_thread2():
    for i in range(5):
        print("user thread_id ", end="")
        print(str(threading.get_native_id()) + " second user thread: " + str(i))


def mainfunc():
    func1_thread1()
    func2_thread2()


mainfunc()
