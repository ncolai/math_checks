def floorval(big, i, j, p, n):
    return int(big * n / (p ** i))
    #return int(big/(p ** i) + j/n)

def compsum(n, p, i):
    for j in range(0, n):
        exp1 = floorval(30, i, j, p, n) + floorval(1, i, j, p, n)
        exp2 = floorval(15,i, j, p, n) + floorval(6,i, j, p, n) + floorval(10,i, j, p, n)
        print(n, p, i, exp1, exp2)

def multiples_after(k,n):
    counter1 = 0
    counter2 = 0
    counter3 = 0
    counter5 = 0
    counter_sum = 0
    for i in range(k + 1, n):
        counter1 += 1
        print(i, "------")
        printnums = []
        if i % 2 == 0:
            counter2 += 1
        if i % 3 == 0:
            counter3 += 1
        if i % 5 == 0:
            counter5 += 1

    print(counter1, counter2 + counter3 + counter5)

if __name__ == "__main__":
    multiples_after(12, 30)
    
