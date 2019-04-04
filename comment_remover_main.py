x = input('Enter the name of python file: ')
Comment_char = input('Enter the comment character : ')
x = x + '.py'
file = open(x, 'r')
temp = open('D:\\temp.txt', 'w')
for line in file:
    lin = line.strip()
    if lin.startswith(Comment_char):
        continue
    temp.write(line)
temp.close()
file.close()

file = open(x, 'w')
temp = open('d:\\temp.txt', 'r')
for line in temp:
    lin = line.strip()
    if lin.startswith('#'):
        continue
    file.write(line)
temp.close()
file.close()
print('Done Dana Done...!!!')
