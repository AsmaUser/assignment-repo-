import random

def roll_dice():
    return random.randint(1, 6), random.randint(1, 6)

def count_die(die1, die2):
    total = die1 + die2
    print("You rolled {} + {} = {}".format(die1, die2, total))
    
    if total == 7 or total == 11:
        print("You Win! :)")
    elif total == 2 or total == 3 or total == 12:
        print("You lose! :(")
    else:
        print("Point is {}".format(total))
        return total

def main():
    # To Initial roll
    die1, die2 = roll_dice()
    point = count_die(die1, die2)

    # Continue rolling until a 7 or the same point is rolled
    while point is not None:
        input("Press Enter to roll the dice ^-^")
        die1, die2 = roll_dice()
        point = count_die(die1, die2)

main()


