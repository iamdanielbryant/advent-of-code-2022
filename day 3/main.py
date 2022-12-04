legend = " abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

def getData(filename):
    file = open(filename,"r")
    sacks = file.readlines()

    result = []
    for s in sacks:
        compSize = int(len(s) / 2)
        comp1 = s[0:compSize]
        comp2 = s[compSize:int(len(s))]
        result.append([comp1,comp2])
    return result

def checkCommonData(comp):
    common = []
    for i in comp[0]:
        for j in comp[1]:
            if i == j:
                if i not in common:
                    common.append(i)                    
    return common


sacks = getData('input.txt')

def part1():
    totalScore = 0

    for s in sacks:
        commonLetters = checkCommonData(s)
        #print("Sack: " + s[0] + " + " + s[1] + "\nCommon: " + str(commonLetters) + "\n")
        sackScore = 0
        for c in commonLetters:
            for i in range(0,len(legend)):
                if c == legend[i]:
                    #print("The score for: " + c + " is " + str(i) + "\n\n")
                    sackScore += i
        totalScore += sackScore

    print("Total score: " + str(totalScore))

part1()

