# heapq 사용!!
def solution(scoville, K):
    import heapq
    heapq.heapify(scoville) 
    count = 0

    while scoville[0] < K:
        if len(scoville) > 1:
            first = heapq.heappop(scoville)   
            second = heapq.heappop(scoville)
            new = first + second*2
            heapq.heappush(scoville, new)    
            count += 1 
        
        else:
            return -1
        
    return count