def solution(price, money, count):
    answer = 0
    for i in range(1,count+1):
        answer += i
    
    answer *= price
    
    if answer > money:
        answer = answer - money
    elif answer <= money:
        return 0
        
    return answer
