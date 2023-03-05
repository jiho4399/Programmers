def solution(msg):
    lst = []
    n, m = 0, 0
    dic = {}
    
    for i in range(26):
        dic[chr(65+i)] = i+1

    while m != len(msg):
        m += 1
        if msg[n:m+1] not in dic:
            dic[msg[n:m+1]] = len(dic)+1
            lst.append(dic[msg[n:m]])
            n = m
        elif m == len(msg):
            lst.append(dic[msg[n:m]])

    return lst