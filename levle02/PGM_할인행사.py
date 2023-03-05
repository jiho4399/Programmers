def solution(want, number, discount):
    want_1 = dict(zip(want, number))
    n = len(discount) - sum(number)
    answer = 0

    for i in range(n+1):
        discount_1 = discount[i:sum(number)+i]
        mart = dict.fromkeys(want,0)
        count = 0

        for j in discount_1:
            if j in want:
                mart[j] += 1

        for k in mart:
            if mart[k] >= want_1[k]:
                count += 1
            if count == len(want):
                answer += 1
                
    return answer