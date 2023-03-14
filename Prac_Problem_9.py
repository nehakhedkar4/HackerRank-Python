''' You are given n words. Some words may repeat. 
For each word, output its number of occurrences. 
The output order should correspond with the input order of appearance of the word. See the sample input/output for clarification. '''

from collections import Counter
n = input()
lst = []
for i in range(int(n)):
    lst.append(input(""))
    
print(len(set(lst)))
d = Counter(lst)
for i in d.values():
    print(i, end=' ')





#     4
# bcdef
# abcdefg
# bcde
# bcdef
