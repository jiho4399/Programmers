# 프로그래머스 : 최솟값 만들기


# 다 맞았으나 효율성에서 시간초과
def solution(A, B):
  answer = 0
  for i in range(len(A)):
    s = A.pop(A.index(max(A))) * B.pop(B.index(min(B)))
    answer += s
  
  return answer


# 성공
def solution(A, B):
  return sum(a * b for a, b in zip(sorted(A), sorted(B, reverse=True)))