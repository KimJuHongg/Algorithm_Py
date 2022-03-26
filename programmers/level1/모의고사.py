def solution(answers):
    answer = []
    a = [1,2,3,4,5]
    b = [2,1,2,3,2,4,2,5]
    c = [3,3,1,1,2,2,4,4,5,5]
    a_count = 0
    b_count = 0
    c_count = 0
    for i in range(len(answers)):
        if a[i%(len(a))] == answers[i]:
            a_count += 1
        if b[i%(len(b))] == answers[i]:
            b_count += 1
        if c[i%(len(c))] == answers[i]:
            c_count += 1
    if max(a_count, b_count, c_count) == a_count:
        answer.append(1)
    if max(a_count, b_count, c_count) == b_count:
        answer.append(2)
    if max(a_count, b_count, c_count) == c_count:
        answer.append(3) 
    return answer
