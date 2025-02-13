list = [1, 2, 3, 4, 5, 5, 5]
d = {}

for i in list:
    d[i] = list[i - 1]


print(d)
