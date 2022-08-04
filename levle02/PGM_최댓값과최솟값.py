# 프로그래머스 : 최댓값과 최솟값

def solution(s):
  lst = list(map(int, s.split(' ')))

  return str(min(lst)) + ' ' + str(max(lst))


# 메모
s = "1 2 3 4"

answer = []
lst = list(map(int, s.split(' ')))
# answer.append(str(min(lst)))
# answer.append(str(max(lst)))

# print(' '.join(answer))

str(min(lst)) + ' ' + str(max(lst))