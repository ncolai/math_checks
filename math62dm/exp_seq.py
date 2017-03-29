def seqsum(n, p):
    sum = 0
    for i in range(1, n+1):
        sum += (i ** i) % p
            
    return sum 

if __name__ == "__main__":
    p = input()
    p = int(p)
    for i in range(1, 500):
        result = seqsum(i,p)
        print(i, result, result % p)

        

