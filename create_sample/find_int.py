s = input()
word_list = s.split()
num_list = []

for word in word_list:
    if word.isnumeric():
        num_list.append(int(word))

print(num_list)