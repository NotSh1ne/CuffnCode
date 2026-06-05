import threading
from config import MAX_RETRY

class Worker(threading.Thread):
    def __init__(self, worker_id, task_queue, monitor):
        super().__init__()
        self.worker_id = worker_id
        self.task_queue = task_queue
        self.monitor = monitor
        self.daemon = True

    def run(self):
        while True:
            priority, task_id, task = self.task_queue.get()
            try:
                duration = task.execute(self.worker_id)
                self.monitor.task_completed(self.worker_id, task, duration)
            except Exception:
                task.retry_count += 1
                self.monitor.task_failed(self.worker_id, task)
                if task.retry_count <= MAX_RETRY:
                    # reinsert task with same priority
                    self.task_queue.put((priority, task.task_id, task))
            finally:
                self.task_queue.task_done()