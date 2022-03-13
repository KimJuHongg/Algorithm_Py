def solution(s):
    answer = ''
    count = 0
    s = list(s.lower())
    
    for i in range(len(s)):
        if s[i] == ' ':
            answer += ' '
            count = 0
        else :
            if count % 2 == 0:
                count += 1
                answer += s[i].upper()
            
            else:
                count += 1
                answer += s[i]
            
    return answer
