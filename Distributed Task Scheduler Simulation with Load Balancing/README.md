# Fault-Tolerant Distributed Task Scheduler with Priority and Monitoring

## Project Overview
This project implements a simulation of a distributed task scheduling system
using a master–worker architecture. The system demonstrates key concepts of
parallel computing and distributed systems such as task scheduling, priority
handling, load balancing, fault tolerance, and system monitoring.

## Objectives
The objectives of this project are:
- To simulate parallel task execution using multiple worker nodes
- To implement priority-based task scheduling
- To demonstrate fault tolerance through task retry mechanisms
- To monitor system performance and workload distribution

## System Architecture
The system consists of the following components:
- **Master Node**: Responsible for creating tasks and assigning priorities
- **Worker Nodes**: Execute tasks concurrently using multithreading
- **Task Queue**: Priority-based queue for scheduling tasks
- **Monitor**: Collects execution statistics and system metrics

## Key Features
- Priority-based task scheduling (High, Medium, Low)
- Parallel execution using multithreading
- Dynamic load balancing among workers
- Fault tolerance with retry mechanism
- Centralized monitoring and execution summary

## Technologies Used
- Python 3
- Threading
- Queue and PriorityQueue
- Object-Oriented Programming

## How the System Works
1. The master node generates tasks with different priority levels.
2. Tasks are inserted into a priority queue.
3. Worker nodes fetch tasks concurrently based on priority.
4. Task failures are simulated and retried automatically.
5. The monitor collects statistics and prints a summary report.

## How to Run
```bash
python master.py