
with open("data.txt", "r") as file:
    content = file.read()
    print(content)

file=open("data.txt", "r")
content=file.read()
print(content)
file.close()
