def trueop(num, divnum):
    divnumnum = 0
    while(num % 2 == 0):
        divnumnum += 1
        num = num // 2
    if divnumnum < divnum:
        return True
    else:
        return False

gfnum, maxnum = map(int, input().split())
divnum = 0
while(gfnum % 2 == 0):
    divnum += 1
    gfnum = gfnum / 2
ops = range(1, maxnum)
finalops = []
for i in ops:
    if trueop(i, divnum):
        finalops.append(i)
print(len(finalops))
print(*finalops)
