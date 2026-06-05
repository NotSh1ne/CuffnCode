import queue
from worker import Worker
from task import Task
from monitor import Monitor
from config import NUM_WORKERS, PRIORITY_LEVELS

task_queue = queue.PriorityQueue()
monitor = Monitor()

# start workers
workers = []
for i in range(NUM_WORKERS):
    w = Worker(worker_id=i + 1, task_queue=task_queue, monitor=monitor)
    w.start()
    workers.append(w)

# create tasks with priority
task_id = 1
for priority_name, priority_value in PRIORITY_LEVELS.items():
    for _ in range(4):
        task = Task(task_id, priority_name)
        # (priority, task_id, task) -> SAFE for PriorityQueue
        task_queue.put((priority_value, task_id, task))
        task_id += 1

# wait until all tasks are done
task_queue.join()
monitor.summary()