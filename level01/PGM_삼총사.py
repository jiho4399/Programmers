# 성공
count = 0
def combination(arr, r):

  result = []

  def function(c, index):
    if len(c) == r:
      result.append(c)
      return
         
    for idx, data in enumerate(arr):
      if idx > index:
        function(c+[data], idx)
   
  function([], -1)
    
  return result

def solution(number):
  global count
  for r in combination(number, 3):
    if sum(r) == 0:
      count += 1
  
  return count

#########################

# import combination
def solution(number) :
    from itertools import combinations
    count = 0
    for i in combinations(number,3):
        if sum(i) == 0 :
            count += 1
    return count