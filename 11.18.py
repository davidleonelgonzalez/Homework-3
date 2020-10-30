# David Gonzalez
# 1630338

integer = input().split()

num_int = []

for i in integer:
    i = int(i)
    if i >= 0:
        num_int.append(i)

    num_int.sort()

for n in num_int:
    print(n, end=' ')
