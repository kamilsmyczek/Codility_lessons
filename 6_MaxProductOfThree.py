def solution(A):
    A.sort()
    product_minus = A[0] * A[1] * A[-1]
    product_plus = A[-3] * A[-2] * A[-1]

    return product_minus if product_minus > product_plus else product_plus