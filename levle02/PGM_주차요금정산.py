def solution(fees, records):
  import math
  answer = []
  in_dic = {}
  out_dic = {}
  sum_dic = {}

  for i in records:
    time, num, in_out = i.split()
    hour, min = time.split(':')
    time = int(hour)*60 + int(min)

    if in_out == 'IN':
      in_dic[num] = time
    else:
      out_dic[num] = time
      
      if num not in sum_dic:
        sum_dic[num] = out_dic[num] - in_dic[num]
      else:
        sum_dic[num] += out_dic[num] - in_dic[num]
      
      del in_dic[num]

  if in_dic:
    for num, time in in_dic.items():
      if num not in sum_dic:
        sum_dic[num] = 1439 - time
      else:
        sum_dic[num] += 1439 - time

  for num, time in sum_dic.items():
    if time <= fees[0]:
      cost = fees[1]
    
    else:
      plus = math.ceil((time - fees[0])/fees[2]) * fees[3]
      cost = fees[1] + plus

    answer.append((num, cost))

  answer.sort()
  return [i[1] for i in answer]


######################
# 메모1

fees = [180, 5000, 10, 600]
records = ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", 
           "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]

in_dic = {}
out_dic = {}
sum_dic = {}

for i in records:
  time, num, in_out = i.split()
  hour, min = time.split(':')
  time = int(hour)*60 + int(min)

  if in_out == 'IN':
    in_dic[num] = time
  else:
    out_dic[num] = time
    if num not in sum_dic:
      sum_dic[num] = out_dic[num] - in_dic[num]
      del in_dic[num]
    else:
      sum_dic[num] += out_dic[num] - in_dic[num]
      del in_dic[num]

if in_dic:
  for num, time in in_dic.items():
    sum_dic[num] += 1439 - time


print(sum_dic)

################
# 메모2
import math

answer = []

for num, time in sum_dic.items():
  if time <= fees[0]:
    cost = fees[1]
  
  else:
    plus = math.ceil((time - fees[0])/fees[2]) * fees[3]
    cost = fees[1] + plus

  answer.append((num, cost))

answer.sort()