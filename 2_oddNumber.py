A = [42,1,1,5,5]

def solution(A):
    # return empty array
    if not A:
        return A
        
    A.sort()
    print(A)
    last = A[0]
    cnt = 1
    for idx in range(1, len(A)):
        if A[idx] == last:
            cnt += 1     
        else:
            last = A[idx]
            if cnt % 2:
                return A[idx-1]
            cnt = 1
        print('For: i=', A[idx], ', cnt=', cnt, sep='')
        
    if cnt % 2:
        return last
    else:
        return None
        
print(solution(A))