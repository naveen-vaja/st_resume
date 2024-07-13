# file open
s = open('demo.txt',mode='r')
print(s.read())
s.close()


 #write mode
s = open('demo.txt',mode='a')
s.write("welcome to python class")
s.close()

s = open('demo.txt',mode='r+')

print(s.read())

s.write("welcomer")