#90. DMOJ problem ampl2023p2 Amplitude Hackathon '23 Problem 2 - Gigatron Lag
N = int(input())

partition_lags = {}
global_offset = 0
output = []

for i in range(N):
    line = input().split()
    operation = line[0]

    if operation == "ADD":
        p, x = int(line[1]), int(line[2])
        if p not in partition_lags:
            partition_lags[p] = 0
        partition_lags[p] += x

    elif operation == "ADDALL":
        x = int(line[1])
        global_offset += x
        
    
    elif operation == "PROCESS":
        p, x = int(line[1]), int(line[2])
        if p not in partition_lags:
            partition_lags[p] = 0
        effective_lag = partition_lags[p] + global_offset
        to_process = min(x, effective_lag)
        partition_lags[p] -= to_process
    
    elif operation == "PROCESSALL":
        x = int(line[1])
        global_offset -= x
        if global_offset <= 0:
            global_offset = 0
        else:
            for p in list(partition_lags.keys()):
                effective_lag = partition_lags[p] + global_offset
                if effective_lag <= 0:
                    partition_lags[p] = 0
                else:
                    partition_lags[p] = effective_lag - global_offset

    elif operation == "LAG":
        p = int(line[1])
        effective_lag = partition_lags.get(p, 0) + global_offset
        output.append(str(effective_lag))

    elif operation == "MAXLAG":
        if partition_lags:
            max_lag = max(partition_lags.values()) + global_offset 
        else:
            max_lag = global_offset
        output.append(str(max_lag))

for o in output:
    print(o)
