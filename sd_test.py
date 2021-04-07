text = 'hello'
fileName = 'data.txt'

file=open(fileName, 'w')

file.write(text)
file.close()

file = open(fileName, 'r')
input_text = file.readline()
file.close()

print(input_text)


