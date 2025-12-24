def solution(X, A):
    path = [False] * X
    path_sum = 0
    expectedSum = X/2 * (1+X)
    for idx, p in enumerate(A):
        if not path[p-1]:
            path_sum += p
        path[p - 1] = True
        
        if path_sum == expectedSum:
            return idx
    return -1