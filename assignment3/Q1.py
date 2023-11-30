def count_point(die1, die2):
    total = die1 + die2
    print("You rolled {} + {} = {}".format(die1, die2, total))

    if total in (7, 11):
        print("You win")
    elif total in (2, 3, 12):
        print("You lose")
    else:
        print("Point is {}".format(total))
        return total

def play_craps():
    # Initial roll
    die1 = int(input("Enter the value for die 1: "))
    die2 = int(input("Enter the value for die 2: "))
    
    point = count_point(die1, die2)

    # Continue rolling until a 7 or the same point is rolled
    while point is not None:
        die1 = int(input("Enter the value for die 1: "))
        die2 = int(input("Enter the value for die 2: "))
        point = count_point(die1, die2)

if __name__ == "__main__":
    play_craps()


