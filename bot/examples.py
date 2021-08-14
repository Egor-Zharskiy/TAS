s = '[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]'
first = []
for i in s:
    try:
        first.append(int(i))
    except:
        pass
print(first)
print(type(first))