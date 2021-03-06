# -*- coding: utf-8 -*-
"""레벨1-1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ylMqV2yq_RFTNBSGZENFbpnE1lgkXI3f

# 1.짝수와 홀수
"""

def solution(num):
  if num % 2 == 0:
    return 'Even'
  else :
    return 'Odd'

"""다른 사람 풀이"""

def evenOrOdd(num):
    return ["Even", "Odd"][num & 1]

#아래는 테스트로 출력해 보기 위한 코드입니다.
print("결과 : " + evenOrOdd(3))
print("결과 : " + evenOrOdd(2))

def evenOrOdd(num):
    if (num%2):
        return "Odd"
    else:
        return "Even"

evenOrOdd(3)

"""# 2.직사각형 별찍기"""

a, b = map(int, input().split(' '))

for i in range(b):
    for j in range(a):
        print('*', end='')
    print()

"""다른 사람 풀이"""

a, b = map(int, input().split(' '))

for _ in range(b):
    print('*'*a)

"""# 3.x 간격 n개 숫자"""

def solution(x, n):
  answer = []

  for i in range(1, n+1):
    num = x * i
    answer.append(num)
  return answer

def solution(x, n):
  return [x * i for i in range(1, n+1)]

solution(-4, 2)

"""# 4.행렬의 덧셈"""

def solution(arr1, arr2):
  for i in range(len(arr1)):
    for j in range(len(arr1[i])):
      arr1[i][j] += arr2[i][j]
    
    return arr1

"""# 5.핸드폰 번호 가리기"""

def solution(num):
    num = num.replace(num[:-4], '*'*len(num[:-4]))
    return num

solution("01033334444")

"""# 6.하샤드 수"""

def solution(x):
  return x % sum([int(i) for i in str(x)]) == 0

x = 324

lst = []

for i in str(x):
  lst.append(int(i))
  a = sum(lst)

# sum([int(i) for i in str(x)])

324
3+2+4

324/9

x[1]

solution(13)

