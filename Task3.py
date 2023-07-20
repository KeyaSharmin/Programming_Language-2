
dict1 = {}
dict2 = {}
inp1 = input().split(',')
inp2 = input().split(',')
for i in inp1:
    kv = i.split(':')
    dict1[kv[0]] = int(kv[1])

for i in inp2:
    kv = i.split(':')
    dict2[kv[0]] = int(kv[1])

for k, v in dict2.items():
    if k not in dict1:
        dict1[k] = v
    else:
        dict1[k] += v
print(dict1)
unique_values = []
for k, v in dict1.items():
    if v not in unique_values:
        unique_values.append(v)
print(tuple(sorted(unique_values)))