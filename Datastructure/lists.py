#          0        1        2         3         4
names = ["Sara", "Arvin", "Shuib", "Jasmine", "Nyla"]

names[3] = "John"

for i in range(4,-1,-1): # Starting at indexing of 4, to -1 (as Python is n-1), at the interval of -1
    print (names[i])
