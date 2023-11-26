import random
import string
n = int (input ("Enter a size: "))
def get_random_string(length):
    result_str = ''.join(random.choice(string.ascii_letters) for i in range(length))
    print(result_str)

get_random_string(n)
