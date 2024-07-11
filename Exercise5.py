# Take two lists, say for example these two:
#   a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#   b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# and write a program that returns a list that contains only the elements that are common between the lists (without duplicates). 
# Make sure your program works on two lists of different sizes.
# Extras:
#     Randomly generate two lists to test this
#     Write this in one line of Python (don’t worry if you can’t figure this out at this point - we’ll get to it soon)
import random
MIN,MAX,ELEMENTS = 0,100,9
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13,89]
merge = []
for x in a:
    if x in b:
        merge.append(x)
merge = set(merge)
print(merge)

randomlistA = random.sample(range(MIN,MAX),random.randint(3,ELEMENTS))
randomlistB = random.sample(range(MIN,MAX),random.randint(3,ELEMENTS))
merge = [x for x in randomlistA if x in randomlistB]
if merge:
    merge = set(merge)
    print('\nList 1: {}\nList 2: {}\nMerges: {}'.format(randomlistA,randomlistB,merge))
else:
    print('\nList 1: {}\nList 2: {}\nNo Identical fields or Empty'.format(randomlistA,randomlistB))