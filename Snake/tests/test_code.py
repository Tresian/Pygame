row = 25
column = 25

_map = []


for i in range(row):
    _map.append([])
    for j in range(column):
        _map[i].append('x')

for i in _map:
    for j in i:
        print(j)