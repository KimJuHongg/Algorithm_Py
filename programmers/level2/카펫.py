def solution(brown, yellow):
    answer = []
     
    for i in range(1, yellow+1):
        if (yellow / i) + i + 2 == brown // 2:
            answer.append((yellow//i) + 2)
            answer.append(i + 2)
    
            return answer
