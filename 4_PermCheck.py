def solution(A):
    A_set = set(A)
    return int((len(A) == len(A_set)) and (max(A_set) == len(A_set)))