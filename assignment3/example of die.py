def count_input(n):
    attempts = input("Enter your attempts: ")
    counter = [0] * 10  # Initialize a counter list for digits 0-9
    for char in attempts:
        if char.isdigit():
            digit = int(char)
            counter[digit] += 1
    return counter[1:n+1] 
    """attempts = input("Enter your attempts: ").split(",")
    counter= []
    for i in range(1, n+1):
        counter.append(attempts.count(str(i)))
    return counter"""
def print_count(lst):
    for i in range (1, len(lst)+1):
        print ("{}: {}".format(i, lst[i-1]))
def main ():
    saides = int (input("Enter the number of sides for die:  "))
    count_list = count_input(saides)
    print_count(count_list)

main()