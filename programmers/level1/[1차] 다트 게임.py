def solution(dartResult):
    
    answer = []
    score = []

    for i in range(len(dartResult)):
        if dartResult[i] == '1' and dartResult[i+1] == '0':
            score.append('10')
        elif dartResult[i] == '0' and dartResult[i-1]=='1':
            continue
        else :
            score.append(dartResult[i])
            
    for i in range(1, len(score)):
        if score[i] == 'S':
            answer.append(int(score[i-1]))          
        elif score[i] == 'D':
            answer.append(int(score[i-1])**2)
        elif score[i] == 'T':
            answer.append(int(score[i-1])**3)
            
        if score[i] == '*':
            if len(answer) >= 2:
                answer[-2] *= 2
            answer[-1] *= 2
        elif score[i] == '#':
            answer[-1] *= -1
    
    return sum(answer)
