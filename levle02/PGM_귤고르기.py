# test 통과, 실패
def solution(k, tangerine):
    tangerine.sort()
    answer = []
    lst = []
    for i in range(len(tangerine)):
        if tangerine[i] in tangerine[:i] or tangerine[i] in tangerine[i+1:]:
            answer.append(tangerine[i])
            if len(answer) >= k:
                break
        else:
            lst.append(tangerine[i])

    if len(answer) < k:
        for j in lst:
            answer.append(j)
            if len(answer) == k:
                break

    return len(set(answer))

###############################


# 성공
def solution(k, tangerine):
    dic = {}
    count = 0
    for i in range(len(tangerine)):
        dic[tangerine[i]] = 0

    for j in tangerine:
        if j in dic:
            dic[j] += 1

    tanger = sorted(dic.items(), key=lambda x:x[1], reverse=True)

    for key, v in tanger:
        k -= v
        count += 1
        if k <= 0:
            break

    return count

###############################


# counter 함수 사용(성공)
def solution(k, tangerine):
    from collections import Counter

    count = 0
    tanger = sorted(Counter(tangerine).items(), key=lambda x:x[1], reverse=True)

    for i, j in tanger:
        k -= j
        count += 1
        if k <= 0:
            break

    return count
