def solution(n, lost, reserve):
    answer = 0
    l_lost = len(lost)
    
    lost = sorted(lost)
    reserve = sorted(reserve)
    
    for i in lost:
        if i in reserve:
            reserve.remove(i)
            l_lost -= 1
    
    answer = n - l_lost
    
    for i in lost:
        if (i-1) in reserve:
            reserve.remove(i-1)
            answer += 1
            
        elif (i+1) in reserve:
            reserve.remove(i+1)
            answer += 1
    
    return answer
