import threading
import time


def worker(counter):
    id = threading.current_thread()
    print("thread %s started" % id)
    time.sleep(2)
    if counter < 1000:
        counter += 1
        t = threading.Thread(target=worker, args=(counter,))
        t.start()
        t.join()
    else:
        print("teliosa! counter = %s, id = %s " % (counter, id))


if __name__ == '__main__':
    counter = 0
    t = threading.Thread(target=worker, args=(counter,))
    t.start()
    t.join()
