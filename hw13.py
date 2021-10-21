# This program reads numbers from file in.txt, sorts them in ascending order and writes them into file out.txt

# Reading the numbers from in.txt
path = "./in.txt"
reader = open(path, mode="r")
data = reader.read()
reader.close()
data = data.split()

# Sorting numbers
data = list(map(int, data))
data.sort()

# Preparing output
str = ""
for elem in data:
    str += f"{elem} "

# Writing output in out.txt
path = "./out.txt"
writer = open(path, mode="w")
writer.write(str)

