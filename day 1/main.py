elves = [
    #{'id': 0,'food': [], 'calories': 0}
]

def readData():
    f = open("input.txt","r")
    lines = f.readlines()

    group = []
    currentGroup = []
    for ln in lines:
        if ln.strip():
            #non-empty line
            currentGroup.append(int(ln.strip()))
        else:
            #empty line
            group.append(currentGroup)
            currentGroup = []

    for i,g in enumerate(group):
        totalCalories = 0
        for j,gg in enumerate(group[i]):
            totalCalories += gg

        o = {'id': i, 'food': group[i], 'calories': totalCalories}
        elves.append(o)

def calorieTotalArray(list):
    totals = []
    for e in list:
        totals.append(e['calories'])
    return totals


readData()

#narrow data to just calories & sort
totalCalories = calorieTotalArray(elves)
totalCalories.sort()
print("The top elf has a total of: " + str(totalCalories[-1]) + " calories!") # <-- answer #1  

#add the sum of the top 3 total calories for all elves
top3 = [totalCalories[-1],totalCalories[-2],totalCalories[-3]]
sum = top3[0] + top3[1] + top3[2]
print("The top 3 elves have a sum of: " + str(sum) + " calories!")