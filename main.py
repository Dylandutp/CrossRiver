import heapq
import queue
import state 

init = state.State(3, 3, 1, 1)
goal = state.State(0, 0, 0, 0)

x = []
x.append(init)
a = state.State(3, 3, 1, 1)
b = state.State(1, 1, 1, 1)
c = state.State(1, 2, 1, 1)
d = state.State(5, 5, 5, 5)
print(state.isClosed(a, x), state.isClosed(b, x), state.isLegal(c), state.isLegal(d))
print(state.isLegal(a))

print(123)
