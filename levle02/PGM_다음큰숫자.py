# 프로그래머스 : 다음 큰 숫자

def solution(n):
  m = bin(n).count('1')

  for h in range(n+1, 1000001):
    if bin(h).count('1') == m:

      return h