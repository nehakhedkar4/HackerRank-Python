''' You are given a string .
Your task is to find out whether  is a valid regex or not. '''

import re
num = input()
for i in range(int(num)):
    f = input()
    try:
        check = re.compile(f)
        print(True)
    except re.error:
        print(False)