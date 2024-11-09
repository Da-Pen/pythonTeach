l = [1, 2, 3, 4, 4]
print(set(l))
print(tuple(l))

s = {1, 2, 3, 4}
print(list(s))
print(tuple(s))

t = (1, 2, 3, 4, 4)
print(list(t))
print(set(t))

d = {
    1: 11,
    2: 11,
    3: 13,
    4: 14
}
print(set(d.keys()))
print(set(d.values()))
print(list(d.keys()))
print(list(d.values()))
print(tuple(d.keys()))
print(tuple(d.values()))
