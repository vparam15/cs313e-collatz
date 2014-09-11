import random

file = open("RunCollatz.in.txt", "w")

for i in range (1000):
    file.write(str(random.randint(1,1000000)) + " " + str(random.randint(1,1000000)) + "\n")    
