file = open("data.txt", "w")
file.write("Hello File")
file.close()

with open("data1.txt", "w") as file:
    file.write("Hello File111")