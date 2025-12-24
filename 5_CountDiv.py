def solution(A, B, K):
    # Implement your solution here
    minValue = (A // K) * K
    if minValue < A:
        minValue += K
    
    maxValue = (B // K) * K
    if minValue > B or maxValue < A:
        return 0

    return (maxValue - minValue) // K + 1