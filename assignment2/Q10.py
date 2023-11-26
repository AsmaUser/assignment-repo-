def filter_long_words(word_list, n):
    longer_words = [word for word in word_list if len(word) > n]
    return longer_words

# Get input from the user
words_input = input("Enter a list of words separated by spaces: ")
threshold_length_input = int(input("Enter the threshold length: "))

# Split the input string into a list of words
words_list = words_input.split()

# Call the function with user inputs
result = filter_long_words(words_list, threshold_length_input)

# Print the result
print("Words longer than {threshold_length_input} characters: {result}")
