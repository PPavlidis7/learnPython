import threading


def worker(id, a):
    """thread worker function"""
    a += 1
    print('Worker\'s id = %d and made a = %d' % (id, a))
    return


threads = []
for i in range(10):
    a = 0
    t = threading.Thread(target=worker, args=(i, a))
    threads.append(t)
    t.start()
