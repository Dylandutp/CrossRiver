import state 

number = 1
def addChild(list, current):
    global number
    # when both boat are on the right bank
    if current.a == True and current.b == True:
        # sail boatA
        for a1 in range(1, 3):
            for a2 in range(0, a1 + 1):
                people_state = state.State(current.m - a2, current.c - (a1 - a2), not current.a, current.b, current.g + 3, 0)
                boat_state = state.BoatState(a2, a1 - a2, 0, 0)
                if state.isLegal(people_state, boat_state):
                    people_state.num = number
                    number += 1
                    people_state.parent = current.num
                    people_state.boat = boat_state
                    list.append(people_state)

        # sail boatB
        for b1 in range(1, 4):
            for b2 in range(0, b1 + 1):
                people_state = state.State(current.m - b2, current.c - (b1 - b2), current.a, not current.b, current.g + 25, 0)
                boat_state = state.BoatState(0, 0, b2, b1 - b2)
                if state.isLegal(people_state, boat_state):
                    people_state.num = number
                    number += 1
                    people_state.parent = current.num
                    people_state.boat = boat_state
                    list.append(people_state)

        # sail boatA and boatB
        for a1 in range(1, 3):
            for a2 in range(0, a1 + 1):
                for b1 in range(1, 4):
                    for b2 in range(0, b2 + 1):
                        people_state = state.State(current.m - a2 - b2, current.c - (a1 - a2) - (b1 - b2), not current.a, not current.b, current.g + 28, 0)
                        boat_state = state.BoatState(a2, a1 - a2, b2, b1 - b2)
                        if state.isLegal(people_state, boat_state):
                            people_state.num = number
                            number += 1
                            people_state.parent = current.num
                            people_state.boat = boat_state
                            list.append(people_state)

    # when boatA is on the right bank and boatB is on the left bank
    if current.a == True and current.b == False:
        # sail boatA
        for a1 in range(1, 3):
            for a2 in range(0, a1 + 1):
                people_state = state.State(current.m - a2, current.c - (a1 - a2), not current.a, current.b, current.g + 3, 0)
                boat_state = state.BoatState(a2, a1 - a2, 0, 0)
                if state.isLegal(people_state, boat_state):
                    people_state.num = number
                    number += 1
                    people_state.parent = current.num
                    people_state.boat = boat_state
                    list.append(people_state)
                    
        # sail boatB
        for b1 in range(1, 4):
            for b2 in range(0, b1 + 1):
                people_state = state.State(current.m + b2, current.c + (b1 - b2), current.a, not current.b, current.g + 25, 0)
                boat_state = state.BoatState(0, 0, b2, b1 - b2)
                if state.isLegal(people_state, boat_state):
                    people_state.num = number
                    number += 1
                    people_state.parent = current.num
                    people_state.boat = boat_state
                    list.append(people_state)
        
        # sail boatA and boatB
        for a1 in range(1, 3):
            for a2 in range(0, a1 + 1):
                for b1 in range(1, 4):
                    for b2 in range(0, b2 + 1):
                        people_state = state.State(current.m - a2 + b2, current.c - (a1 - a2) + (b1 - b2), not current.a, not current.b, current.g + 28, 0)
                        boat_state = state.BoatState(a2, a1 - a2, b2, b1 - b2)
                        if state.isLegal(people_state, boat_state):
                            people_state.num = number
                            number += 1
                            people_state.parent = current.num
                            people_state.boat = boat_state
                            list.append(people_state)

    # when boatA is on the left bank and boatB is on the right bank
    if current.a == False and current.b == True:
        # sail boatA
        for a1 in range(1, 3):
            for a2 in range(0, a1 + 1):
                people_state = state.State(current.m + a2, current.c + (a1 - a2), not current.a, current.b, current.g + 3, 0)
                boat_state = state.BoatState(a2, a1 - a2, 0, 0)
                if state.isLegal(people_state, boat_state):
                    people_state.num = number
                    number += 1
                    people_state.parent = current.num
                    people_state.boat = boat_state
                    list.append(people_state)

        # sail boatB
        for b1 in range(1, 4):
            for b2 in range(0, b1 + 1):
                people_state = state.State(current.m - b2, current.c - (b1 - b2), current.a, not current.b, current.g + 25, 0)
                boat_state = state.BoatState(0, 0, b2, b1 - b2)
                if state.isLegal(people_state, boat_state):
                    people_state.num = number
                    number += 1
                    people_state.parent = current.num
                    people_state.boat = boat_state
                    list.append(people_state)
        
        # sail boatA and boatB
        for a1 in range(1, 3):
            for a2 in range(0, a1 + 1):
                for b1 in range(1, 4):
                    for b2 in range(0, b2 + 1):
                        people_state = state.State(current.m + a2 - b2, current.c + (a1 - a2) - (b1 - b2), not current.a, not current.b, current.g + 28, 0)
                        boat_state = state.BoatState(a2, a1 - a2, b2, b1 - b2)
                        if state.isLegal(people_state, boat_state):
                            people_state.num = number
                            number += 1
                            people_state.parent = current.num
                            people_state.boat = boat_state
                            list.append(people_state)

    # when both boats are on the left bank
    if current.a == False and current.b == False:
        # sail boatA
        for a1 in range(1, 2):
            for a2 in range(0, a1):
                people_state = state.State(current.m + a2, current.c + (a1 - a2), not current.a, current.b, current.g + 3, 0)
                boat_state = state.BoatState(a2, a1 - a2, 0, 0)
                if state.isLegal(people_state, boat_state):
                    people_state.num = number
                    number += 1
                    people_state.parent = current.num
                    people_state.boat = boat_state
                    list.append(people_state)

        # sail boatB
        for b1 in range(1, 3):
            for b2 in range(0, b1):
                people_state = state.State(current.m + b2, current.c + (b1 - b2), current.a, not current.b, current.g + 25, 0)
                boat_state = state.BoatState(0, 0, b2, b1 - b2)
                if state.isLegal(people_state, boat_state):
                    people_state.num = number
                    number += 1
                    people_state.parent = current.num
                    people_state.boat = boat_state
                    list.append(people_state)

        # sail boatA and boatB
        for a1 in range(1, 3):
            for a2 in range(0, a1 + 1):
                for b1 in range(1, 4):
                    for b2 in range(0, b2 + 1):
                        people_state = state.State(current.m + a2 + b2, current.c + (a1 - a2) + (b1 - b2), not current.a, not current.b, current.g + 28, 0)
                        boat_state = state.BoatState(a2, a1 - a2, b2, b1 - b2)
                        if state.isLegal(people_state, boat_state):
                            people_state.num = number
                            number += 1
                            people_state.parent = current.num
                            people_state.boat = boat_state
                            list.append(people_state)

open_list = []
closed_list = []
result = False

init = state.State(state.M, state.C, True, True, 0, 0)
goal = state.State(0, 0, False, False, 0, 0)       # the last four elements 0 are not important

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
                    node = e
                    break
            if child.g < node.g:
                node = child
        else:
            open_list.append(child)

    # order open_list with the key: f(x) and cost(h(x) small and cost small -> forward)
    open_list = sorted(open_list, key = lambda x: x.h)
    open_list = sorted(open_list, key = lambda x: x.cost)

if result == True:
    print("The condition has solution.")
    print("Cost = ", closed_list[-1].cost)
    answer = state.showResult(closed_list)
    for e in closed_list:
        e.display()
    print("-" * 50)
    for e in answer:
        e.display()
else:
    print("The condition doesn't have a solution.")

