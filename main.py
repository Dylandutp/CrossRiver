import state 

A = 2  # Capacity of BoatA
B = 3  # Capacity of BoatB
number = 1

def addChild(list, current):
    global number
    # when both boat are on the right bank
    if current.a == True and current.b == True:
        # sail boatA
        for a1 in range(1, A + 1):
            for a2 in range(0, a1 + 1):
                next_state = state.State(current.m - a2, current.c - (a1 - a2), not current.a, current.b)
                next_state.g = current.g + 3
                next_state.h = state.h(next_state)
                next_state.f = next_state.g + next_state.h
                boat_state = state.BoatState(a2, a1 - a2, 0, 0)
                if state.isLegal(next_state, boat_state):
                    next_state.num = number
                    number += 1
                    next_state.parent = current.num
                    next_state.boat = boat_state
                    list.append(next_state)

        # sail boatB
        for b1 in range(1, B + 1):
            for b2 in range(0, b1 + 1):
                next_state = state.State(current.m - b2, current.c - (b1 - b2), current.a, not current.b)
                next_state.g = current.g + 25
                next_state.h = state.h(next_state)
                next_state.f = next_state.g + next_state.h
                boat_state = state.BoatState(0, 0, b2, b1 - b2)
                if state.isLegal(next_state, boat_state):
                    next_state.num = number
                    number += 1
                    next_state.parent = current.num
                    next_state.boat = boat_state
                    list.append(next_state)

        # sail boatA and boatB
        for a1 in range(1, A + 1):
            for a2 in range(0, a1 + 1):
                for b1 in range(1, B + 1):
                    for b2 in range(0, b2 + 1):
                        next_state = state.State(current.m - a2 - b2, current.c - (a1 - a2) - (b1 - b2), not current.a, not current.b)
                        next_state.g = current.g + 28
                        next_state.h = state.h(next_state)
                        next_state.f = next_state.g + next_state.h
                        boat_state = state.BoatState(a2, a1 - a2, b2, b1 - b2)
                        if state.isLegal(next_state, boat_state):
                            next_state.num = number
                            number += 1
                            next_state.parent = current.num
                            next_state.boat = boat_state
                            list.append(next_state)

    # when boatA is on the right bank and boatB is on the left bank
    if current.a == True and current.b == False:
        # sail boatA
        for a1 in range(1, A + 1):
            for a2 in range(0, a1 + 1):
                next_state = state.State(current.m - a2, current.c - (a1 - a2), not current.a, current.b)
                next_state.g = current.g + 3
                next_state.h = state.h(next_state)
                next_state.f = next_state.g + next_state.h
                boat_state = state.BoatState(a2, a1 - a2, 0, 0)
                if state.isLegal(next_state, boat_state):
                    next_state.num = number
                    number += 1
                    next_state.parent = current.num
                    next_state.boat = boat_state
                    list.append(next_state)
                    
        # sail boatB
        for b1 in range(1, B + 1):
            for b2 in range(0, b1 + 1):
                next_state = state.State(current.m + b2, current.c + (b1 - b2), current.a, not current.b)
                next_state.g = current.g + 25
                next_state.h = state.h(next_state)
                next_state.f = next_state.g + next_state.h
                boat_state = state.BoatState(0, 0, b2, b1 - b2)
                if state.isLegal(next_state, boat_state):
                    next_state.num = number
                    number += 1
                    next_state.parent = current.num
                    next_state.boat = boat_state
                    list.append(next_state)
        
        # sail boatA and boatB
        for a1 in range(1, A + 1):
            for a2 in range(0, a1 + 1):
                for b1 in range(1, B + 1):
                    for b2 in range(0, b2 + 1):
                        next_state = state.State(current.m - a2 + b2, current.c - (a1 - a2) + (b1 - b2), not current.a, not current.b)
                        next_state.g = current.g + 28
                        next_state.h = state.h(next_state)
                        next_state.f = next_state.g + next_state.h
                        boat_state = state.BoatState(a2, a1 - a2, b2, b1 - b2)
                        if state.isLegal(next_state, boat_state):
                            next_state.num = number
                            number += 1
                            next_state.parent = current.num
                            next_state.boat = boat_state
                            list.append(next_state)

    # when boatA is on the left bank and boatB is on the right bank
    if current.a == False and current.b == True:
        # sail boatA
        for a1 in range(1, A + 1):
            for a2 in range(0, a1 + 1):
                next_state = state.State(current.m + a2, current.c + (a1 - a2), not current.a, current.b)
                next_state.g = current.g + 3
                next_state.h = state.h(next_state)
                next_state.f = next_state.g + next_state.h
                boat_state = state.BoatState(a2, a1 - a2, 0, 0)
                if state.isLegal(next_state, boat_state):
                    next_state.num = number
                    number += 1
                    next_state.parent = current.num
                    next_state.boat = boat_state
                    list.append(next_state)

        # sail boatB
        for b1 in range(1, B + 1):
            for b2 in range(0, b1 + 1):
                next_state = state.State(current.m - b2, current.c - (b1 - b2), current.a, not current.b)
                next_state.g = current.g + 25
                next_state.h = state.h(next_state)
                next_state.f = next_state.g + next_state.h
                boat_state = state.BoatState(0, 0, b2, b1 - b2)
                if state.isLegal(next_state, boat_state):
                    next_state.num = number
                    number += 1
                    next_state.parent = current.num
                    next_state.boat = boat_state
                    list.append(next_state)
        
        # sail boatA and boatB
        for a1 in range(1, A + 1):
            for a2 in range(0, a1 + 1):
                for b1 in range(1, B + 1):
                    for b2 in range(0, b2 + 1):
                        next_state = state.State(current.m + a2 - b2, current.c + (a1 - a2) - (b1 - b2), not current.a, not current.b)
                        next_state.g = current.g + 28
                        next_state.h = state.h(next_state)
                        next_state.f = next_state.g + next_state.h
                        boat_state = state.BoatState(a2, a1 - a2, b2, b1 - b2)
                        if state.isLegal(next_state, boat_state):
                            next_state.num = number
                            number += 1
                            next_state.parent = current.num
                            next_state.boat = boat_state
                            list.append(next_state)

    # when both boats are on the left bank
    if current.a == False and current.b == False:
        # sail boatA
        for a1 in range(1, A + 1):
            for a2 in range(0, a1):
                next_state = state.State(current.m + a2, current.c + (a1 - a2), not current.a, current.b)
                next_state.g = current.g + 3
                next_state.h = state.h(next_state)
                next_state.f = next_state.g + next_state.h
                boat_state = state.BoatState(a2, a1 - a2, 0, 0)
                if state.isLegal(next_state, boat_state):
                    next_state.num = number
                    number += 1
                    next_state.parent = current.num
                    next_state.boat = boat_state
                    list.append(next_state)

        # sail boatB
        for b1 in range(1, B + 1):
            for b2 in range(0, b1):
                next_state = state.State(current.m + b2, current.c + (b1 - b2), current.a, not current.b)
                next_state.g += current.g + 25 
                next_state.h = state.h(next_state)
                next_state.f = next_state.g + next_state.h
                boat_state = state.BoatState(0, 0, b2, b1 - b2)
                if state.isLegal(next_state, boat_state):
                    next_state.num = number
                    number += 1
                    next_state.parent = current.num
                    next_state.boat = boat_state
                    list.append(next_state)

        # sail boatA and boatB
        for a1 in range(1, A + 1):
            for a2 in range(0, a1 + 1):
                for b1 in range(1, B + 1):
                    for b2 in range(0, b2 + 1):
                        next_state = state.State(current.m + a2 + b2, current.c + (a1 - a2) + (b1 - b2), not current.a, not current.b)
                        next_state.g = current.g + 28
                        next_state.h = state.h(next_state)
                        next_state.f = next_state.g + next_state.h
                        boat_state = state.BoatState(a2, a1 - a2, b2, b1 - b2)
                        if state.isLegal(next_state, boat_state):
                            next_state.num = number
                            number += 1
                            next_state.parent = current.num
                            next_state.boat = boat_state
                            list.append(next_state)

open_list = []
closed_list = []
result = False

init = state.State(state.M, state.C, True, True)
goal = state.State(0, 0, False, False)  # the last four elements 0 are not important

open_list.append(init)

while(len(open_list) != 0):
    current_state = open_list.pop(0)
    closed_list.append(current_state)
    if state.isGoal(current_state):
        result = True
        break
    
    children = []
    addChild(children, current_state)

    for child in children:
        if state.inOpen(child, open_list):
            for e in open_list:
                if e.m == child.m and e.c == child.c and e.a == child.a and child.b == child.b:
                    if child.g < e.g:
                        e = child
                    break
        else:
            open_list.append(child)

    # order open_list with the key: f(x) and cost(h(x) small and cost small -> forward)
    
    open_list = sorted(open_list, key = lambda x: x.h)
    open_list = sorted(open_list, key = lambda x: x.f)

if result == True:
    print("The condition has solution.")
    print("Cost = ", closed_list[-1].g)
    answer = state.showResult(closed_list)
    for e in closed_list:
        e.display()
    print("-" * 50)
    answer = reversed(answer)
    for e in answer:
        e.display()
else:
    print("The condition doesn't have a solutiion.")
