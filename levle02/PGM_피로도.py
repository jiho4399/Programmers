# 백트래킹
# for문을 돌면서 탐색하고 안되면 취소
# count값이 현재 answer보다 클 경우에 answer 업데이트 후 출력

answer = 0

def backtracking(k, count, dungeons, visited):
  global answer
  if count > answer:
    answer = count

  for i in range(len(dungeons)):
    if not visited[i] and k >= dungeons[i][0]:
      visited[i] = True
      backtracking(k-dungeons[i][1], count+1, dungeons, visited)
      visited[i] = False

def solution(k, dungeons):
  visited = [False] * len(dungeons)
  backtracking(k, 0, dungeons, visited)
  return answer