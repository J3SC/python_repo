import random

def attack (damage):
    if damage == 0:
        return 'you missed'
    elif damage == 1:
        return 'you barely scratched em.'
    elif damage == 3:
        return 'that was a hit'
    elif damage == 4:
        return 'great hit but needs more power'
    elif damage == 5:
        return 'hit'
    elif damage == 6:
        return 'solid hit counter, deserves a follow up'   
    elif damage == 7:
        return 'accurate strike'
    elif damage == 8:
        return 'perfect hit'
    elif damage == 9:
        return 'critical hit'
    
r = random.randint(0, 9)
fight = attack(r)
#in this block of code there is apre defind function for our code to run on
#assuming the the attack function isnt defined the random.randint(0, 9)
#will return int of 0 to 9


#print (range(10, 1))
numbers = range (10, 1)
for number in numbers:
    print (number)
#basically the range call 0r (10, 1) will result to an error