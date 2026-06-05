import random
import time

class Task:
    def __init__(self, task_id, priority):
        self.task_id = task_id
        self.priority = priority
        self.duration = random.randint(1, 4)
        self.retry_count = 0

    def execute(self, worker_id):
        print(f"[Worker {worker_id}] Task {self.task_id} | Priority {self.priority}")
        time.sleep(self.duration)

        # simulate failure (20%)
        if random.random() < 0.2:
            raise Exception("Simulated task failure")

        return self.duration