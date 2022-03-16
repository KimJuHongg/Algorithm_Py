def solution(strings, n):
    answer = []
    
    for i in strings:
        answer.append(i[n] + i)
        
    answer.sort()
    
    answer = [x[1:] for x in answer]
    
    return answer
