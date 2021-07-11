file = "test.txt"

s = open(file, mode='r')

ch = s.read(1)
while ch != '':
    print(ch, end='')
    ch = s.read(1)

s.close()