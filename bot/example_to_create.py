
f = open("C:/Users/HP/PycharmProjects/TAS/files/Zharskiy_Egor_Aleksandrovich/scanWorks/teacher.jpg"
         "/marks_of_the_pupils!!@#$%^&.txt", 'r', encoding='utf-8')
s = f.read().splitlines()
# s.decode('cp1251').encode('utf8')

w = 'Артем Смоляр'
q = 'Гурбо Павел Михайлович'

f.close()

flag = True

for i in range(len(s)):

     if i == len(s) - 1:
        print(i)
        flag = False
     if s[i].find(w) != -1:

        flag = True
        break

if not flag:
    print(s, flag)
    s.append(w)
    line = ""
    for i in range(len(s)):
        if i != len(s) - 1:
            line += s[i] + "\n"
        else:
            line += s[i]

        f = open("C:/Users/HP/PycharmProjects/TAS/files/Zharskiy_Egor_Aleksandrovich/scanWorks/teacher.jpg"
                 "/marks_of_the_pupils!!@#$%^&.txt", 'w', encoding='utf-8')
        f.write(line)

else:
    #тут ищем этого чела в списке и добавляем ему оценку
    print(flag, s)
    for i in range(len(s)):
        if s[i].find(w) != -1:
            s[i] = s[i] + '  оценка'

    line = ""
    for i in range(len(s)):
        if i != len(s) - 1:
            line += s[i] + '\n'
        else:
            line += s[i]

            f = open(f"{path}"
                     "/marks_of_the_pupils!!@#$%^&.txt", 'w', encoding='utf-8')
            f.write(line)
            f.close()
#оформить в виде функции.
