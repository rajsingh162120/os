def is_safe(available, max_demand, allocation, n, m):
    """
    Check if the current state is safe.
    """
    work = available.copy()
    finish = [False] * n
    sequence = []

    for _ in range(n):
        found = False
        for i in range(n):
            if not finish[i]:
                need = [max_demand[i][j] - allocation[i][j] for j in range(m)]
                if all(need[j] <= work[j] for j in range(m)):
                    work = [work[j] + allocation[i][j] for j in range(m)]
                    finish[i] = True
                    found = True
                    sequence.append(i)
                    break
        if not found:
            return False, sequence

    return True, sequence

def banker_algorithm(processes, resources, max_demand, allocation, available):
    """
    Implement the Banker's Algorithm.
    """
    n = len(processes)
    m = len(resources)

    # Calculate the remaining need for each process
    need = [[max_demand[i][j] - allocation[i][j] for j in range(m)] for i in range(n)]

    is_safe_state, sequence = is_safe(available, max_demand, allocation, n, m)

    if is_safe_state:
        print("System is in a safe state.")
        print("Sequence of processes executed:", sequence)
    else:
        print("System is in an unsafe state.")
        print("Sequence of processes executed before deadlock:", sequence)

if __name__ == "__main__":
    # Example usage
    processes = ['P0', 'P1', 'P2', 'P3', 'P4']
    resources = ['A', 'B', 'C']
    max_demand = [[7, 5, 3], [3, 2, 2], [9, 0, 2], [2, 2, 2], [4, 3, 3]]
    allocation = [[0, 1, 0], [2, 0, 0], [3, 0, 2], [2, 1, 1], [0, 0, 2]]
    available = [4, 3, 2]

    banker_algorithm(processes, resources, max_demand, allocation, available)