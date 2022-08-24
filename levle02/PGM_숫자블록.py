# 프로그래머스 : 숫자 블록

# 테스트 케이스 통과 but 시간 초과
def solution(begin, end):
  result = [0] * end

  # 도로의 길이 : 1,000,000,000

  for j in range(begin, end+1):
    for i in range(2, 1000000001):
    # for i in range(2, end+1):
      if i * j in list(range(1, end+1)):
        result[i*j-1] = j

      elif i*j > end:
        break

  return result



# 정답

def solution(begin, end):
  result = []

  # 도로의 길이 : 1,000,000,000
  # 블럭 숫자의 최댓값 : 10,000,000

  for j in range(begin, end+1):
    # if j != 1: 
    #   k = 1
    # else:
    #   k = 0
    k = int(j != 1)
    for i in range(2, int(j**0.5)+1):
      if j%i == 0 and j//i <= 10000000:
        k = j//i
        break

    result.append(k)

  return result