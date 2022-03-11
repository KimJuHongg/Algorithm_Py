import math

def solution(n,m):
    answer = []
    a = math.gcd(n,m)
    answer.append(a)
    
    for i in range(1,(n*m)+1,1) :
        if i%n==0 and i%m==0:
            answer.append(i)
            break
            
    return answer
