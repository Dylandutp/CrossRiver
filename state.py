M = 3  #Total number of Misionaries
C = 3  #Total number of Cannibals

#State (Misionaries, Cannibals, BoatA, BoatB)
class State:
    def __init__(self, m, c, a, b):
        self.m = m  #The number of Misionaries on the right side
        self.c = c  #The number of Cannibals on the right side
        self.a = a  # a = 1: BoatA on the right side; a = 0: BoatA on the left side
        self.b = b  # b = 1: BoatB on the right side; b = 0: BoatB on the left side
        self.parent = None
        self.node = [m, c, a, b]


class BoatState:
    def __init__(self, am, ac, bm, bc):
        self.am = am  #The number of Misionaries on BoatA
        self.ac = ac  #The number of Cannibals on BoatA
        self.bm = bm  #The number of Misionaries on BoatB
        self.bc = bc  #The number of Cannibals on BoatB
        self.parent = None
        self.node = [am, ac, bm, bc]

#Dtermine whether the state reach the goal
def isGoal(x):
    if x.m == 0 and x.c == 0 and (x.a == 0 or x.b == 0):
        return True
    else:
        return False

#Determine whether the state is in the Closed List
def isClosed(x, closed):
    for e in closed:
        if x.m == e.m and x.c == e.c and x.a == e.a and x.b == e.b:
            return True
    return False

#Determine whether the state is legal
def isLegal(x):
    if x.m >= 0 and x.m <= M and x.c >=0 and x.c <= C:
        if x.c > x.m:
            return False
        else:
            return True
    else:
        return False

