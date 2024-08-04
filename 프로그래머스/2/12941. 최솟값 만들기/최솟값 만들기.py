def solution(A, B):
    A.sort(reverse=True)
    B.sort(reverse=False)

    return sum(A[i] * B[i] for i in range(len(A)))