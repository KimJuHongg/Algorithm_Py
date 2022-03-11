def solution(n):
    answer = ''
    
    for i in sorted(str(int(n)), reverse = True):
        answer += i
        
    return int(answer)
