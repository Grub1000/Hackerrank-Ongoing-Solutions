regex_integer_in_range = r"^[1-9][0-9]{5}$"	# Do not delete 'r'.
regex_alternating_repetitive_digit_pair = r"(\d)(?=\d\1)"	# Do not delete 'r'.

import re
P = input()

print (bool(re.match(regex_integer_in_range, P)) 
and len(re.findall(regex_alternating_repetitive_digit_pair, P)) < 2)


# Task:
# Your task is to provide two regular expressions regex_integer_in_range and regex_alternating_repetitive_digit_pair. Where:
# regex_integer_in_range should match only integers range from  100000 to 999999 inclusive
# regex_alternating_repetitive_digit_pair should find alternating repetitive digits pairs in a given string.


# Sample Input:
# 110000

# Sample Output:
# False