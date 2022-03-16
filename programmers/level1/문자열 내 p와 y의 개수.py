def solution(s):
    answer = True
    s1 = s.lower()
    a = s1.count('p')
    b = s1.count('y')
    
    for i in range(len(s1)):
        if a == b:
            return answer
        elif a == 0 and b == 0:
            return answer
        else :
            return False
