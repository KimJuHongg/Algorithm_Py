def solution(A,B):
    answer = 0
    A = sorted(A)
    B.sort(reverse=True)
    for i in range(len(A)):
        answer += A[i] * B[i]
    
    return answer
