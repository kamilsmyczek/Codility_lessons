def solution(A):
    cumSum = [0] * len(A)
    cumSum[0] = A[0]
    for idx, val in enumerate(A[1:]):
        cumSum[idx + 1] = cumSum[idx] + val
    
    passingPairs = 0
    for idx, val in enumerate(A):
        if not val:
            passingPairs += cumSum[len(A) - 1] - cumSum[idx]
        if passingPairs > 1000000000:
            return -1
    
    return passingPairs