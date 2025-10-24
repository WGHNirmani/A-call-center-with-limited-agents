import random
import matplotlib.pyplot as plt

# ============================================================
#   A CALL CENTER WITH LIMITED AGENTS - SIMULATION REPORT
# ============================================================

# ----------------------------
# Simulation settings
# ----------------------------
random.seed(42)
total_calls = 30
min_call_time = 2
max_call_time = 10
min_arrival_gap = 1
max_arrival_gap = 4

# ----------------------------
# Function to simulate the call center
# ----------------------------
def simulate_call_center(num_agents):
    call_queue = []
    agents_busy = [0] * num_agents
    waiting_times = []
    current_time = 0

    for call_id in range(1, total_calls + 1):
        # new call arrival
        arrival_gap = random.randint(min_arrival_gap, max_arrival_gap)
        current_time += arrival_gap

        # update agent timers
        for i in range(num_agents):
            if agents_busy[i] > 0:
                agents_busy[i] = max(0, agents_busy[i] - arrival_gap)

        # check for free agent
        assigned = False
        for i in range(num_agents):
            if agents_busy[i] == 0:
                call_duration = random.randint(min_call_time, max_call_time)
                agents_busy[i] = call_duration
                waiting_times.append(0)
                assigned = True
                break

        # if all busy, add to queue
        if not assigned:
            call_queue.append((call_id, current_time))

        # assign queued calls when free
        for i in range(num_agents):
            if agents_busy[i] == 0 and call_queue:
                waiting_call = call_queue.pop(0)
                waited_time = current_time - waiting_call[1]
                waiting_times.append(waited_time)
                call_duration = random.randint(min_call_time, max_call_time)
                agents_busy[i] = call_duration

    average_wait = sum(waiting_times) / len(waiting_times)
    max_wait = max(waiting_times)
    calls_waited = sum(1 for w in waiting_times if w > 0)

    return average_wait, max_wait, calls_waited


# ----------------------------
# Run simulations
# ----------------------------
agents_list = [2, 3, 5]
average_waits = []
max_waits = []
calls_waited_list = []

print("============================================================")
print("         A CALL CENTER WITH LIMITED AGENTS SIMULATION")
print("============================================================\n")

for agents in agents_list:
    avg_wait, max_wait, calls_waited = simulate_call_center(agents)
    average_waits.append(round(avg_wait, 2))
    max_waits.append(max_wait)
    calls_waited_list.append(calls_waited)

    print(f"--- Scenario: {agents} Agents ---")
    print(f"Total Calls Handled     : {total_calls}")
    print(f"Average Wait Time (min) : {avg_wait:.2f}")
    print(f"Maximum Wait Time (min) : {max_wait}")
    print(f"Calls That Waited       : {calls_waited}")
    print()

print("============================================================")

# ----------------------------
# Generate charts 
# ----------------------------
plt.bar(agents_list, average_waits, color='skyblue')
plt.title("Average Wait Time vs Number of Agents")
plt.xlabel("Number of Agents")
plt.ylabel("Average Wait Time (minutes)")
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.savefig("average_wait_time.png")
plt.close()

plt.bar(agents_list, max_waits, color='salmon')
plt.title("Maximum Wait Time vs Number of Agents")
plt.xlabel("Number of Agents")
plt.ylabel("Maximum Wait Time (minutes)")
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.savefig("maximum_wait_time.png")
plt.close()

plt.bar(agents_list, calls_waited_list, color='lightgreen')
plt.title("Calls That Waited vs Number of Agents")
plt.xlabel("Number of Agents")
plt.ylabel("Number of Calls That Waited")
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.savefig("calls_waited.png")
plt.close()
