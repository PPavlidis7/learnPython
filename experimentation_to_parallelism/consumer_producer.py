import queue
import threading
import time


class Consumer(threading.Thread):
    def __init__(self,q):
        threading.Thread.__init__(self)
        self._queue = q

    def run(self):
        while True:
            content = self._queue.get()
            if isinstance(content,str) and content =='quit':
                break
            print(content)
        print("Bye Bye")


def producer():
    urls = [
        'http://www.python.org', 'http://www.yahoo.com'
                                 'http://www.scala.org', 'http://www.google.com'
        # etc..
    ]
    q = queue.Queue()
    worker_threads= build_worker_pool(q, 4)
    start_time = time.time()

    for url in urls:
        q.put(url)

    for worker in worker_threads:
        q.put('quit')
        worker.join()

    print('Done! Time taken: {}'.format(time.time() - start_time))


def build_worker_pool(q,size):
    workers =[]
    for _ in range(size):
        worker = Consumer(q)
        worker.start()
        workers.append(worker)
    return workers


if __name__ == '__main__':
    producer()
