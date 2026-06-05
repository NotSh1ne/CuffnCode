import threading

class Monitor:
    def __init__(self):
        self.lock = threading.Lock()
        self.completed = 0
        self.failed = 0
        self.worker_load = {}

    def task_completed(self, worker_id, task, duration):
        with self.lock:
            self.completed += 1
            self.worker_load[worker_id] = self.worker_load.get(worker_id, 0) + duration
            print(f"[MONITOR] Task {task.task_id} completed")

    def task_failed(self, worker_id, task):
        with self.lock:
            self.failed += 1
            print(f"[MONITOR] Task {task.task_id} failed on Worker {worker_id}")

    def summary(self):
        print("\n===== SYSTEM SUMMARY =====")
        print("Completed tasks:", self.completed)
        print("Failed attempts:", self.failed)
        print("Worker load:", self.worker_load)