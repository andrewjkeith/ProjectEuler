import itertools
import math
x=30
permlist = list(itertools.permutations(range(x)))
expectedvaluecount=0
for i in permlist:
    step2acount=0
    mylist = list(i)
    while (mylist != sorted(mylist)):
        startele=0
        nextele=startele+1
        while (nextele != len(mylist)):
            if(mylist[startele] > mylist[nextele]):
                mylist.insert(0,mylist.pop(nextele))
                step2acount += 1
                break
            startele=startele+1
            nextele=startele+1
    expectedvaluecount += step2acount
expectedvaluecount
math.factorial(x)
print(expectedvaluecount/(math.factorial(x)))