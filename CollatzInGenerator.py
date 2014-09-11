import random

file = open("RunCollatz.out.txt", "w")

def collatz_eval (i, j) :
    """
    i the beginning of the range, inclusive
    j the end       of the range, inclusive
    return the max cycle length of the range [i, j]
    """
    
    if (i > j):
        i, j = j, i

    def cycle_length (n):
        assert n > 0
        c = 1
        while n > 1:
            if n % 2 == 0:
                n = n // 2
            else:
                n = n + (n // 2) + 1
                c += 1
            c += 1
        return c

    if (i < (j // 2)):
        i = j // 2 + 1

    v = 1
    for num in range (i, j + 1):
        if cycle_length(num) > v:
            v = cycle_length(num)

    return (v)

for n in range (1000):
    i = random.randint(1,1000000)
    j = random.randint(1,1000000)
    v = collatz_eval(i, j)
            
    print(str(i) + " " + str(j) + " " + str(v) + "\n")    

