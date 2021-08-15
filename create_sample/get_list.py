from finding_squares_uxuxuuxux import *
w = (8, 5)
start_time = time.time()

s = main('C:/Users/HP/PycharmProjects/TAS/create_sample/search_for_3333333.png', 1, 'C:/Users/HP/PycharmProjects/TAS/the_second_files\klmnk926725842\scanWorks/test_items.png/answers', 'C:/Users/HP/PycharmProjects/TAS/the_second_files\klmnk926725842\scanWorks/test_items.png/current_answers')

# s = [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]
print("--- 2.47345 seconds ---")#% (time.time() - start_time))
pup = [[1, 0, 0, 0, 1], [0, 0, 1, 0, 0], [1, 0, 0, 1, 0], [1, 0, 0, 1, 0], [0, 1, 0, 0, 0], [0, 1, 1, 0, 0], [0, 1, 0, 1, 0], [1, 0, 0, 0, 1]]
# print(pup, 'pup')
# print(s, 'axaxax')

kol = 0
for i in s:
    if i == 1:
        kol+=1
# print(kol)
q = []
#обработка самого массива
for i in range(w[0]):
    e = []
    q.append(e)
    for j in range(i, len(s), w[0]):
        e.append(s[j])

print('[', end='')
for i in q:
    print(i)
    if i == q[-1]:
        print(i, end='')
        print(']')
print('сформированный список с ответами')
# print(q, '\nмассив после распознавания квадратов')

kol = []
c = 0

for i in range(len(q)):
    for j in range(len(q[i])):
        # print(q[i][j])
        if q[i][j] == 1:
            c+=1
    kol.append(c)
    c = 0
# print()
#
# print(kol)


kol_of_pup = []
mark = 0
'''for i in range(len(q)):
    mark = 0
    for j in range(len(q[i])):
        if q[i][j] == pup[i][j] == 0:
            pass
        if q[i][j] == pup[i][j] == 1:
            print(q[i], pup[i])
            mark += 1
        if q[i][j] == 1 and pup[i][j] == 0:
            pass
        if q[i][j] == 0 and pup[i][j] == 1:
            mark -= 1
    # print(mark, kol[i])
    kol_of_pup.append(mark/kol[i])
print(kol_of_pup)'''
mark_pupil = 0
# for i in kol_of_pup:
#     mark_pupil += i
# print(mark_pupil)
# print(kol)
mark_pupil = 0
for i in range(len(q)):
    mark_pupil = 0
    if kol[i] != 0:
        kp = 1 / kol[i]

    kn = 1 / (w[1] - kol[i])
    # print(1/(w[1]-kol[i]))
    for j in range(len(q[i])):
        if q[i][j] == pup[i][j] == 1:
            mark_pupil += kp
        # elif q[i][j] == 1 and pup[i][j] == 0:
        #     mark_pupil -= kn
        elif q[i][j] ==  pup[i][j] == 0:
            pass
        elif q[i][j] == 0  and pup[i][j] == 1:
            mark_pupil -= kn
    kol_of_pup.append(mark_pupil)
# print(kol_of_pup)
# print(w[1])
ocenka = 0
for i in kol_of_pup:
    ocenka += i
# print(ocenka)
#давать не оцкенку а процент выполнения
procent = (ocenka * 10)/w[0]
# print(f'{str(procent * 10)}%')
# тут процент выдается
# print(f"{procent * 10:.{0}f}%")
