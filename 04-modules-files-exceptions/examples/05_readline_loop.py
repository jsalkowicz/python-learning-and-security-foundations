content = open("testfile.txt", "r")

for i in range(2):
    print(content.readline())

content.close()
