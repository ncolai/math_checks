#I believe this was a false start; check out debruijn2.py for an accurate implementation.
def order(start, group):
    temp = start
    nums = [start]
    while temp != 1:
        print(temp)
        temp *= start
        temp %= group
        nums.append(temp)
    return nums

if __name__ == "__main__":
    seq1 = [0,0,1,2,2,0,2,1,1]
    seq2 = [0,0,1,1]

    long1 = ""
    long2 = ""
    for i in range(36):
        long1 += str(seq1[i % 9])
        long2 += str(seq2[i % 4])

    len_dict = {}
    long1 += long1
    long2 += long2
    for i in range(36):
        mytuple = (long1[i], long2[i], long1[i+1], long2[i+1])
        if mytuple not in len_dict:
            len_dict[mytuple] = 1
        else:
            len_dict[mytuple] += 1

    for i in len_dict:
        if len_dict[i] != 1:
            print i


    """
    my_dict = {(4*i + 9*j) % (4*9):(i,j) for i in range(9) for j in range(4)}
    nums = {i:0 for i in range(12)}
    foundstring = ""
    
    print(order(11, 36))

    #function 1
    print(nums)
    for i in range(4*9):
        for j in my_dict:
            if j == i:
                foundnum = (seq1[my_dict[j][0]]+3*seq2[my_dict[j][1]])
                foundstring += str(foundnum)
                print(j, my_dict[j], foundnum)
                nums[foundnum] += 1
    
    #function 2
    twofound = foundstring + foundstring
    founddict = {}
    for i in range(36):
        if twofound[i:i+2] not in founddict:
            founddict[twofound[i:i+2]] = 1
        else:
            founddict[twofound[i:i+2]] += 1

    print(founddict)
    """
    


