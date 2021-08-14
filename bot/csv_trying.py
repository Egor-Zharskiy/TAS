import csv
FILE = 'd:/file.csv'
users = [
    ["Tom", 28],
    ["Alice", 23],
    ["Bob", 34]
]

name = 'Жарский Егор Александрович'

yourList = [1, 2, 3, 4, 5,]

# with open(FILE, 'w', ) as myfile:
#     wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
#     for word in yourList:
#         wr.writerow([word])
print(FILE)
with open(FILE, newline='') as f:
    # print('axaxaxaxaxaxa')
    reader = csv.reader(f)
    for row in reader:
        print(row)
        print(name in row)
        print('axaxaxa')

        if name in row:
            print(row, 'совпало')


with open(FILE, 'w', newline='') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=' ',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)

    spamwriter.writerow(['Жарский Егор Александрович', 'Baked Beans'])
    spamwriter.writerow(['Spam', 'Lovely Spam', 'Wonderful Spam'])
