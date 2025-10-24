# Call Center Simulation

# Project Title

A Call Center with Limited Agents

## 1. Project Overview

This simulation models the performance of a call center that handles incoming customer calls using a limited number of agents.
The objective is to study how the number of available agents affects:

- Customer waiting time
- Maximum delay experienced
- Number of calls that had to wait

The simulation provides insight into service efficiency and helps identify the optimal staffing level for better performance and cost balance.

## 2. Purpose of the Simulation

The purpose is to analyze system performance under different staffing scenarios.
By simulating random call arrivals and service durations, the study observes how queues form when agents are busy and measures how this affects customer waiting time.

## 3. Software and Tools Used

- Language: Python 3.x
- Libraries Required:

```
pip install matplotlib
```

- IDE Options: VS Code, PyCharm, or any Python-supported environment.

## 4. How to Run the Simulation

### Step 1: Save the code

Save the simulation file as `call_center_simulation.py`.

### Step 2: Run the file

Open a terminal in the same directory and run:

```
python call_center_simulation.py
```

### Step 3: View results

The program will:

- Display simulation results in the console for 2, 3, and 5 agents.
- Generate visualizations (average wait time, maximum wait time, and number of waiting calls).

## 5. Parameters Used

You can modify the following parameters at the beginning of the script to test other situations:

```python
total_calls = 30          # total number of calls to simulate
min_call_time = 2         # minimum call duration in minutes
max_call_time = 10        # maximum call duration in minutes
min_arrival_gap = 1       # minimum time gap between calls
max_arrival_gap = 4       # maximum time gap between calls
agents_list = [2, 3, 5]   # agent counts for scenarios
```

## 6. Output Explanation

### Console Output Example:

```
============================================================
         A CALL CENTER WITH LIMITED AGENTS SIMULATION
============================================================

--- Scenario: 2 Agents ---
Total Calls Handled     : 30
Average Wait Time (min) : 5.64
Maximum Wait Time (min) : 43
Calls That Waited       : 6

--- Scenario: 3 Agents ---
Total Calls Handled     : 30
Average Wait Time (min) : 1.00
Maximum Wait Time (min) : 11
Calls That Waited       : 5

--- Scenario: 5 Agents ---
Total Calls Handled     : 30
Average Wait Time (min) : 0.00
Maximum Wait Time (min) : 0
Calls That Waited       : 0
============================================================
```

### Charts Generated:

1. Average Waiting Time vs Number of Agents
2. Maximum Waiting Time vs Number of Agents
3. Number of Calls That Waited vs Number of Agents

## 7. Project Summary

- Increasing the number of agents reduces waiting times.
- Beyond 5 agents, further improvement is negligible, showing diminishing returns.
- Helps determine optimal staffing for cost-effective performance.
