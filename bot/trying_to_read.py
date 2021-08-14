import codecs
f = codecs.open('C:/Users/HP/PycharmProjects/TAS/files/Zharskiy_Egor_Aleksandrovich/scanWorks/teacher.jpg/marks_of_the_pupils!!@#$%^&.txt', encoding='utf-8', mode='r')
s = f.read().splitlines()
print(s)