def solution(d, budget):
    
    result = 0
    d = sorted(d)
    
    for i in range(0, len(d)):
        if d[i] <= budget:
            budget = budget - d[i]
            result += 1
        else :
            break
    return result
