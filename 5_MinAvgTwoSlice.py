def solution(A):
    MAX_VAL = 10000
    cumSum = [0] * (len(A) + 1)
    for idx, x in enumerate(A):
        cumSum[idx + 1] = cumSum[idx] + x
    
    minAvg = MAX_VAL
    start_idxMin = 0
    for sliceSize in [2, 3]:
        sliceSum = sliceSize * MAX_VAL
        start_idxCurrent = 0
        for idx_start in range(len(A) - sliceSize + 1):
            currentSum = cumSum[idx_start + sliceSize] - cumSum[idx_start]
            #print("start=", idx_start, ", sum=", currentSum, sep='')
            if sliceSum > currentSum:
                sliceSum = currentSum
                start_idxCurrent = idx_start
        #print("min:", start_idxCurrent, sliceSum)
        if minAvg > sliceSum / sliceSize:
            minAvg = sliceSum / sliceSize
            start_idxMin = start_idxCurrent
            
    return start_idxMin