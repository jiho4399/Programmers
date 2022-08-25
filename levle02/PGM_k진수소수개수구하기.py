# 프로그래머스 : k진수에서 소수 개수 구하기

def solution(n, k):
  rev_base = ''

  while n > 0:
    n, mod = divmod(n, k)
    rev_base += str(mod)

  trans = rev_base[::-1] 
  trans = trans.split('0')

  count = 0

  for i in trans:
    if len(i) == 0 or int(i) == 0 or int(i) == 1:
      continue

    find_sosu = True

    for j in range(2, int(int(i)**0.5) + 1):
      if int(i)%j == 0:
        find_sosu = False
        break
    
    if find_sosu:
      count += 1

  return count