def solution(s):
    answer = ''
    for i in range(len(s)):
        if len(s) % 2 == 1:
            answer = s[len(s) // 2]
        elif len(s) % 2 == 0:
            answer = s[(len(s) // 2) - 1 : (len(s) // 2) + 1]
    return answer
