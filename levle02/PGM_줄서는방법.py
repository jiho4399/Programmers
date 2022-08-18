# 시간초과

def call(lst, n):
    answer = []

    if n > len(lst):
      return answer

    if n == 1:
      for i in lst:
        answer.append([i])

    elif n > 1:
      for i in range(len(lst)):
        ans = [j for j in lst]
        ans.remove(lst[i])
        for p in call(ans, n-1):
          answer.append([lst[i]]+p)
    return answer


def solution(n, k):
  lst = list(range(1, n+1))

  call(lst, n)
  
  return call(lst, n)[k-1]

####################

# 시간초과
# 하나의 리스트에서 모든 조합 수 구하기
from itertools import permutations, combinations

def solution(n, k):

  lst = list(range(1, n+1))

  answer = list(permutations(lst, n))

  return list(answer[k-1])


#######################

# 성공 

def factorial(n):
    m = 1
    for i in range(1, n+1):
        m *= i
    return m

def solution(n, k):
    answer = []
    lst = list(range(1, n+1))
    
    while lst:
        temp = factorial(n-1)
        a, b = divmod(k, temp)
        a = a-1 if b == 0 else a
        answer.append(lst.pop(a))
        
        n -= 1
        k = b
        
    return answer