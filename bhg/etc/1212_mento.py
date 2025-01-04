all_students = set(range(1, 31))

in_students = set()
for list in in_students:
    print(list)


for i in range(28):
    n = int(input())
    in_students.add(n)
    

out_students = sorted(all_students - in_students)

for an in out_students:
    print(an)