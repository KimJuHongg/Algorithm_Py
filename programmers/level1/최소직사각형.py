def solution(sizes):
    answer_w = []
    max_w = 0
    answer_h = []
    max_h = 0
    for w,h in sizes:
        if w < h:
            w, h = h, w
        
        max_w = max(max_w, w)
        max_h = max(max_h, h)
        answer = max_w * max_h
        
    return answer
