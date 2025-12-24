def solution(S, P, Q):
    NUCLEOTIDES_IMPACT = {'A' : 1, 'C' : 2, 'G': 3, 'T' : 4}
    NUCLEOTIDES_IDX  = {'A' : 0, 'C' : 1, 'G': 2, 'T' : 3}
    
    cumSum = list([[0] * (len(S) + 1) for i in NUCLEOTIDES_IMPACT])

    for idx, c in enumerate(S):
        for i in range(len(cumSum)):
            cumSum[i][idx + 1] = cumSum[i][idx]
        cumSum[NUCLEOTIDES_IDX[c]][idx + 1] += 1
    print("Cumsum:", cumSum)
    
    result = [0] * len(P)
    for idx in range(len(P)):
        print("idx:", P[idx], Q[idx])
        for type in NUCLEOTIDES_IDX:
            print("type:",type, cumSum[NUCLEOTIDES_IDX[type]][Q[idx] + 1] - cumSum[NUCLEOTIDES_IDX[type]][P[idx]])
            if cumSum[NUCLEOTIDES_IDX[type]][Q[idx] + 1] - cumSum[NUCLEOTIDES_IDX[type]][P[idx]] > 0:
                result[idx] = NUCLEOTIDES_IMPACT[type]
                print("result:", type)
                break
    
    return result

    
print(solution('CAGCCTA', [2, 5, 0], [4, 5, 6]))