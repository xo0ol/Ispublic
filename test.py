f = open(r'C:\Users\xo0ol\OneDrive\바탕 화면\test.txt', 'r')
read = f.readlines()
print(read)


i = [x.strip('\n') for x in read]
print(i)

