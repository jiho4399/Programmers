# 프로그래머스 하노이의 탑

def hanoi(n, start, arrive, mid, answer):
  # 종료 조건
    if n == 1:
        return answer.append([start, arrive])
    # 1번 기둥에 있는 n개의 원반 중 n-1개를 2번 기둥으로 옮김 
    hanoi(n-1, start, mid, arrive, answer)
    answer.append([start, arrive])
    # 2번 기둥에 있는 n-1개의 원반을 다시 3번 기둥으로 옮김
    hanoi(n-1, mid, arrive, start, answer)
    
def solution(n):
    answer = []
    hanoi(n, 1, 3, 2, answer)
    return answer