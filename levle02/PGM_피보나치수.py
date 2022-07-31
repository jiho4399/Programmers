# 프로그래머스 피보나치 수

# a = 0, b = 1

# f(2) = f(1) + f(0)

# f(3) = f(2) + f(1)

# f(4) = f(3) + f(2) 

# f(5) = f(4) + f(3)

def solution(num):
    a, b = 0, 1

    for i in range(num):
        a, b = b, a+b
        
    return a % 1234567