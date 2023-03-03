''' You are given a string .
Your task is to find the first occurrence of an alphanumeric character in  (read from left to right) that has consecutive repetitions. '''

import re

expression=r"([a-zA-Z0-9])\1+"

m = re.search(expression,input())

if m:
    print(m.group(1))
else:
    print(-1)


    # Group(), Groups() & Groupdict()