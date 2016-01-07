P = [1, 0, 2, 4, 8, 6]

somethingHapened = True

while somethingHapened :
    i = -1
    for R in P :
        i += 1
        if i != len(P) :
            if R > P[i + 1] :
                H = P[i + 1]
                P[i + 1] = P[i]
                P[i] = H

    print P
        
print P
