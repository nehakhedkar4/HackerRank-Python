''' You are given a string  consisting only of digits 0-9, commas ,, and dots .

Your task is to complete the regex_pattern defined below, which will be used to re.split() all of the , and . symbols in . '''

regex_pattern = r"\.|\,"	# Do not delete 'r'.

import re
print("\n".join(re.split(regex_pattern, input())))



# re.spilt()