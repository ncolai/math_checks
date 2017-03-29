def ringsums(m, n):
    sums = {(i, j):(n*i + m*j)% (m*n) for i in range(m) for j in range(n)}
    return sums
    
if __name__ == "__main__":
    my_sums = ringsums(4, 9)
    seq1 = [1,1,0,0]
    seq2 = [0,0,1,2,2,0,2,1,1]
    bigstring = ""
    for i in range(4*9):
        for mysum in my_sums:
            if my_sums[mysum] == i:
                bigstring += str(seq1[mysum[0]]) 
                bigstring += str(seq2[mysum[1]]) + ' '
                print(mysum, my_sums[mysum])

    print(bigstring)
