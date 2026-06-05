# Fault-Tolerant Distributed Task Scheduler
### Parallel & Distributed Computing Project

Contributor
Name : Dwicky Megantara
NRP : 152024055

## Project Overview
This project is a **simulation of a distributed task scheduling system** implemented using a **master–worker architecture**.  
The system demonstrates key concepts in **parallel computing and distributed systems**, including:

- Parallel task execution
- Priority-based scheduling
- Dynamic load balancing
- Fault tolerance and task retry mechanisms
- Basic system monitoring

The simulation is designed to run on a **single machine** without specialized hardware, making it suitable for academic evaluation.

---

## System Architecture
The system consists of three main components:

1. **Master Node**
   - Generates tasks with priorities
   - Assigns tasks to worker nodes
   - Monitors worker status
   - Reassigns tasks if a worker fails

2. **Worker Nodes**
   - Execute tasks concurrently using threads
   - Report execution results and status to the master
   - Simulate failure and recovery scenarios

3. **Task Model**
   - Each task has an ID, priority, and execution time
   - Higher-priority tasks are scheduled first
   - Failed tasks are automatically retried

---

## Key Features
- **Parallel Execution** using multithreading
- **Priority Queue Scheduling**
- **Load Balancing** across multiple workers
- **Fault Tolerance Simulation**
- **Execution Monitoring & Logging**

---

## Project Structure

---

## Learning Outcomes

Through this project, the following concepts are demonstrated:

Distributed system coordination
Parallel workload execution
Scheduling strategies
Fault tolerance principles
Practical application of theoretical concepts in distributed computing

Course Information
Course: Komputasi Paralel & Sistem Terdistribusi
Assignment Type: Project / GitHub Contribution

---

## How to Run the Simulation
### Requirements
- Python 3.9 or later
- No external libraries required

### Steps
```bash
cd "Distributed Task Scheduler Simulation with Load Balancing"
python master.py
