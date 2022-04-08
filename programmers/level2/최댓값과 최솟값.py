def solution(s):
    answer = ''
    
    s1 = list(map(int, s.split(' ')))
    
    answer = str(min(s1)) + " " + str(max(s1))
               
    return answer
