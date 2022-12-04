legend = " abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

def getData(filename):
    file = open(filename,"r")
    data = file.readlines()

    groups = []
    for i, x in enumerate(data):
        if i % 3 == 0:
            groups.append([data[i].strip(),data[i+1].strip(),data[i+2].strip()])
    return groups


def checkCommonGroupData(groups):
    common = []
    for g in groups:
        for l in g[0]:
            if l in g[1] and l in g[2]:
                common.append(l)
                break
            
    return common

def part2():
    totalScore = 0
    groupData = getData('input.txt')
    groupCommons = checkCommonGroupData(groupData)

    for c in groupCommons:
        groupScore = 0
        for i in range(0,len(legend)):
                if c == legend[i]:
                    #print("The score for: " + c + " is " + str(i) + "\n\n")
                    groupScore += i
        totalScore += groupScore

    print("Total score: " + str(totalScore))
part2()