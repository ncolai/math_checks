def order(n, ringn):
    counter = 1
    start = n
    if start == 1:
        return 1
    while start % ringn != 1:
        #print( start )
        start *= n
        counter += 1
        if counter >= 35:
            break
    return counter 

if __name__ == "__main__":
    counter = 0
    for i in range(1, 1001):
        result = order(i, 1001)
        if result == 30:
            counter += 1
        print(i, result)
    print(counter)
        
