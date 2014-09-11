#!/usr/bin/env python3

# ---------------------------
# projects/collatz/Collatz.py
# Copyright (C) 2014
# Glenn P. Downing
# ---------------------------

# ------------
# collatz_read
# ------------

def collatz_read (r) :
    """
    read two ints
    r a reader
    return a list of two ints, representing the beginning and end of a range, [i, j]
    """
    s = r.readline()
    if s == "" :
        return []
    a = s.split()
    return [int(v) for v in a]

# ------------
# collatz_eval
# ------------

cache = {}

def collatz_eval (i, j) :
    """
    i the beginning of the range, inclusive
    j the end       of the range, inclusive
    return the max cycle length of the range [i, j]
    """
    
    if (i > j):
        i, j = j, i

    if (i < (j // 2)):
        i = j // 2 + 1

    max_cycle_length = 1
    
    for a in range (i, j + 1):
        assert a > 0
        b = a
        cycle_length = 1
        while (b > 1):
            if (b in cache.keys()):
                cycle_length += cache[b] - 1
                break
            else:
                if b % 2 == 0:
                    b = b // 2
                    cycle_length += 1
                else: 
                    b += (b // 2) + 1
                    cycle_length += 2
        cache[a] = cycle_length
        if cycle_length > max_cycle_length:
            max_cycle_length = cycle_length
        v = max_cycle_length

    return (v)

# -------------
# collatz_print
# -------------

def collatz_print (w, i, j, v) :
    """
    print three ints
    w a writer
    i the beginning of the range, inclusive
    j the end       of the range, inclusive
    v the max cycle length
    """
    w.write(str(i) + " " + str(j) + " " + str(v) + "\n")

# -------------
# collatz_solve
# -------------

def collatz_solve (r, w) :
    """
    r a reader
    w a writer
    """
    while True :
        a = collatz_read(r)
        if not a :
            return
        i, j = a
        v = collatz_eval(i, j)
        collatz_print(w, i, j, v)
