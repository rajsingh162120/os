def findWaitingTime(processes, n, bt, wt, quantum):
    rem_bt = bt[:]
    t = 0

    while True:
        done = True

        for i in range(n):
            if rem_bt[i] > 0:
                done = False
                if rem_bt[i] > quantum:
                    t += quantum
                    rem_bt[i] -= quantum
                else:
                    t += rem_bt[i]
                    wt[i] = t - bt[i]
                    rem_bt[i] = 0

        if done:
            break

def findTurnAroundTime(processes, n, bt, wt, tat):
    for i in range(n):
        tat[i] = bt[i] + wt[i]

def findavgTime(processes, n, bt, quantum):
    wt = [0] * n
    tat = [0] * n

    findWaitingTime(processes, n, bt, wt, quantum)
    findTurnAroundTime(processes, n, bt, wt, tat)

    print("Processes Burst Time  Waiting Time Turn-Around Time")
    total_wt = 0
    total_tat = 0
    for i in range(n):
        total_wt += wt[i]
        total_tat += tat[i]
        print(" ", processes[i], "\t\t", bt[i], "\t\t", wt[i], "\t\t", tat[i])

    print("\nAverage waiting time = %.5f" % (total_wt / n))
    print("Average turn around time = %.5f" % (total_tat / n))

if __name__ == "__main__":
    n = int(input("Enter the number of processes: "))
    burst_time = list(map(int, input("Enter the burst times of processes separated by space: ").split()))
    quantum = int(input("Enter the time quantum: "))
    proc = [i + 1 for i in range(n)]

    findavgTime(proc, n, burst_time, quantum)
