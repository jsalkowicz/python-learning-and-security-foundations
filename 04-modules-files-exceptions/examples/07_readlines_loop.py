content = open("testfile.txt", "r")
lines = content.readlines()

for i in lines:
    print(i, end="")

content.close()
