# This program reads words from file in.txt, filters those with >5 letters and writes them into file out.txt

# Reading from in.txt
path = "./in.txt"
reader = open(path, mode="r")
data = reader.read()
reader.close()
data = data.split()

# Finding words with len > 5 and preparing them for output
str = ""
for elem in data:
    if len(elem) > 5:
        str += f"{elem} "

# Writing output in out.txt
path = "./out.txt"
writer = open(path, mode="w")
writer.write(str)



