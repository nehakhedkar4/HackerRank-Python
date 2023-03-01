'''
PROBLEM STATEMENT :
Handling Exceptions
You are given two values  and .
Perform integer division and print .. '''

num = input()
for i in range(int(num)):
    a,b = input().split()
    try: 
        print(int(a)//int(b))
    except ZeroDivisionError as e:
        print(f"Error Code: {e}")
    except ValueError as e:
        print(f"Error Code: {e}")
        