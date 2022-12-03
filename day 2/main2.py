def getRoundScores(p):
    #rps game conditions for each player [player1, player2]
    rps = [
        [['A','Z'],['C','X']], #rock beats scissors
        [['B','X'],['A','Y']], #paper beats rock
        [['C','Y'],['B','Z']], #scissors beats paper
        [['A','X'],['B','Y'],['C','Z']] #draw
    ]

    playerScore = [0,0]

    #check for draw
    for d in rps[3]:
        if p == d:
            return [3,3]

   #check for win
    for i,r in enumerate(rps):
        if p == r[0] and i != 3:
            #player 1 wins
            return [6,0]
        elif p == r[1] and i != 3:
            #player 2 wins
            return [0,6]
    
    #check for lose
    if playerScore == [0,0]:
        return playerScore

def getShapeScore(p):
    shapeScore = 0
    if p == 'A' or p == 'X':
        shapeScore = 1
    elif p == 'B' or p == 'Y':
        shapeScore = 2
    elif p == 'C' or p == 'Z':
        shapeScore = 3
    
    return shapeScore

def checkRound(g):
    roundScores = getRoundScores(g)
    p1Score = roundScores[0] + getShapeScore(g[0])
    p2Score = roundScores[1] + getShapeScore(g[1])
    return [p1Score, p2Score]


def part1():
    f = open("input.txt","r")
    lines = f.readlines()

    p1Total = 0
    p2Total = 0

    for ln in lines:
        roundScores = checkRound([ln[0],ln[2]])
        p1Total += roundScores[0]
        p2Total += roundScores[1]
    
    print("Player 1 totaled: " + str(p1Total))
    print("Player 2 totaled: " + str(p2Total))


#part 2:

def setMyMove(op, me):
    if me == 'X':
        #lose the game
        if op == 'A': return 'Z'
        elif op == 'B': return 'X'
        elif op == 'C': return 'Y'
    elif me == 'Y':
        #make draw
        if op == 'A': return 'X'
        elif op == 'B': return 'Y'
        elif op == 'C': return 'Z'
    elif me == 'Z':
        #win the game
        if op == 'A': return 'Y'
        elif op == 'B': return 'Z'
        elif op == 'C': return 'X'


def part2():
    f = open("input.txt","r")
    lines = f.readlines()

    p1Total = 0
    p2Total = 0

    for ln in lines:
        opponent = ln[0]
        me = setMyMove(ln[0],ln[2])

        roundScores = checkRound([opponent,me])
        p1Total += roundScores[0]
        p2Total += roundScores[1]
    
    print("Player 1 totaled: " + str(p1Total))
    print("Player 2 totaled: " + str(p2Total))

part1()
