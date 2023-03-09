''' Dr. John Wesley has a spreadsheet containing a list of student's ,ID ,MARKS, CLASS  and NAME .

Your task is to help Dr. Wesley calculate the average marks of the students. '''

from collections import namedtuple

total_stu = int(input())
myf = input().split()
Student = namedtuple('Student', myf)
v=0
for i in range(total_stu):
    a,b,c,d = input().split()
    s = Student(a,b,c,d)
    v += int(s.MARKS)

print(format((v/total_stu),".2f"))  