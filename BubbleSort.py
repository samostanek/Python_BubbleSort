P = [18, 4, 49, 34, 83, 59, 37, 68, 57, 22, 60, 56, 98, 72, 6, 23, 93, 83, 55, 89]

somethingHapened = True

while somethingHapened :
    i = -1
    somethingHapened = False
    for R in P :
        i += 1
        if not( i == len(P) - 1) :
            if R > P[i + 1] :
                H = P[i + 1]
                P[i + 1] = P[i]
                P[i] = H
                somethingHapened = True

print P
