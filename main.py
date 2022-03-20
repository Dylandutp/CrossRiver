import heapq
lt = [3, 1, 7, 5, 2, 6]
heapq.heapify(lt)
print(heapq.nsmallest(3, lt))

