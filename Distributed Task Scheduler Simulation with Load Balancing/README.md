# Fault-Tolerant Distributed Task Scheduler Simulation  
**with Priority, Load Balancing, and Monitoring**

## Project Overview
This project implements a **simulation of a distributed task scheduling system**
using a **master–worker architecture**. The system demonstrates fundamental
concepts of **parallel computing and distributed systems**, including:

- Parallel task execution
- Priority-based scheduling
- Dynamic load balancing
- Fault tolerance through task retry
- Basic system monitoring

The implementation is designed as a **software simulation**, without requiring
physical distributed hardware or real network communication.

---

## Objectives
The objectives of this project are:
- To simulate parallel task execution using multiple worker threads
- To implement priority-based task scheduling
- To demonstrate load balancing across worker nodes
- To handle worker failures using fault-tolerant retry mechanisms
- To monitor task execution and worker performance

---

## System Architecture

### Master–Worker Model
The system follows a **Master–Worker architecture**:

- **Master Node**
  - Generates tasks with different priorities
  - Distributes tasks to available workers
  - Reassigns tasks if a worker fails
  - Collects execution results and statistics

- **Worker Nodes**
  - Execute tasks in parallel using threads
  - Simulate task execution time
  - Randomly simulate failures
  - Report execution results to the master

---

## Parallelism and Scheduling

- Multiple workers run concurrently using **multithreading**
- Tasks are stored in a **priority queue**
- Higher-priority tasks are executed before lower-priority tasks
- Load balancing ensures tasks are distributed evenly across workers

---

## Fault Tolerance

To simulate real distributed system behavior, this project includes:

- Random worker failure simulation
- Automatic task retry when a failure occurs
- Task re-queuing to ensure no task is permanently lost

This mechanism demonstrates **fault tolerance** commonly used in distributed
systems.

---

## Monitoring and Logging

The system provides simple monitoring features, including:
- Task execution start and completion logs
- Worker activity logs
- Execution time tracking

These logs help observe system behavior and workload distribution.

---

## Project Structure

---

## How to Run the Simulation

### Requirements
- Python 3.8 or higher

### Steps
1. Clone the repository: git clone https://github.com/NotSh1ne/CuffnCode.git

2. Navigate to the project directory:

3. Run the master node:

The terminal output will display task execution, load balancing behavior,
and fault recovery in real time.

---

## Expected Output
- Multiple workers executing tasks concurrently
- Tasks executed based on priority
- Retry attempts for failed tasks
- Monitoring logs showing execution flow

---

## Conclusion
This project successfully demonstrates the core concepts of **distributed task
scheduling and parallel computation** through a software-based simulation.
It highlights how scheduling, fault tolerance, and load balancing can be
implemented without requiring physical distributed infrastructure.

---

## Author
**Name:** Dwicky  
**NRP:** 152024055  
**Course:** Komputasi Paralel & Sistem Terdistribusi
