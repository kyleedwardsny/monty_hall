import random


def monty_hall(size, omniscient, switch):
    prize = random.randint(1, size)
    choice = random.randint(1, size)

    if not omniscient or choice == prize:
        unopened = random.randint(1, size)
        while unopened == choice:
            unopened = random.randint(1, size)
    else:
        unopened = prize

    if switch:
        return unopened == prize
    else:
        return choice == prize


win = 0
lose = 0
for i in range(10000):
    if monty_hall(3, True, True):
        win += 1
    else:
        lose += 1

print("Win: %i" % win)
print("Lose: %i" % lose)
print("Total: %i" % (win + lose))
