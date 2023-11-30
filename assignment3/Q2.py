def eliminate_duplicates(lst):
    return list(set(lst))

def main():
    while True:
        try:
            # First: Input ten numbers
            numbers = input("Enter ten numbers separated by spaces: ").split()
            
            #Then: Convert the input to integers
            numbers = [int(num) for num in numbers]
            
            # Check if there are exactly ten numbers
            if len(numbers) == 10:
                break  # Exit the loop if exactly ten numbers are entered
            else:
                print("Please enter exactly ten numbers.")

        except ValueError:
            print("Invalid input. Please enter valid integers.")

    # Call the function to eliminate duplicates
    distinct_numbers = eliminate_duplicates(numbers)
    
    # Display the result
    print("The distinct numbers are:", end=" ")
    for num in distinct_numbers:
        print(num, end=" ")
    print()
main()

