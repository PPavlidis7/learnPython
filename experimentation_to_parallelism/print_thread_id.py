import threading
import time


def worker(id, a):
    """thread worker function"""
    a += 1
    print('Worker\'s id = %d and made a = %d' % (id, a))
    return


# threads = []
# for i in range(10):
#     a = 0
#     t = threading.Thread(target=worker, args=(i, a))
#     threads.append(t)
#     t.start()


def worker1(num, t):
    time.sleep(0.1)  # pretend to take time to do the work
    """thread worker function"""
    print('Hello from thread: %s out of %s' % (num, t))
    return


threads = []
total = 10
main_thread = threading.currentThread()

for i in range(total):
    print('Main creates thread: %s' % i)
    t = threading.Thread(target=worker1, args=(i, total - 1,))
    threads.append(t)
    t.start()

for t in threading.enumerate():
    if t is main_thread:
        continue
    t.join()
print('Finished')
