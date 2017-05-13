import math
import copy

#in short, an implementation of the AKS algorithm developed in 2002.
#Note that some knowledge of finite fields will help with understanding this.

#I know this already has a function, but re-implementing it to really understandruntime
#exponentiation can be done quickly by hand with repeated squares.
def is_power(n, p):
    '''read this as "is n a pth power of some integer?'''
    if n == 1:
        return True
    max2 = 1
    max2count = 0
    while max2 ** p < n:
        max2 *= 2
        max2count += 1
    if max2 ** p == n:
        #print("Power of 2 %d\n" % (max2))
        return True
    max2 /= 2
    max2count -= 1
    for i in range(max2count):
        nextbin = 2 ** (max2count - i - 1)
        #print(max2, nextbin)
        if (max2 + nextbin) ** p <= n:
            max2 += nextbin
        if max2 ** p == n:
            #print("It's a power! %d\n" % (max2))
            return True
    #print(max2)
    return False

def is_divisible(n, q):
    #to show what's realy going on, like that division is (logn)(logq),
    #think about this as the Euclidean algorithm:
    #each iteration is at most logq bit-by-bit subtractions from n,
    #and each iteration removes on average a binary digit from n.
    #There are logn binary digits to remove, for (logn)(logq) operations total.
    if n % q == 0:
        return True
    return False

#standard way to find gcd.
def euclidean(a,b):
    while b >= 0:
        if a < b:
            temp = a
            a = b
            b = temp
        temp = a - b
        a = b
        b = temp
        if b == 0:
            return a
        elif b == 1:
            return 1

#order: how many times do you perform an operation on n mod r to return to n?
def order(n, r):
    #same runtime analysis as above
    n %= r
    if n == 1:
        return 1
    if n == 0 or r % n == 0:
        return -1
    order_ct = 1
    #temp is what we're multiplying by to find n's order
    temp = n * n
    order_ct += 1
    while temp != n:
        if temp == 0:
            return -1
            break
        temp *= n
        order_ct += 1
        if temp >= r:
            temp %= r
    return order_ct

#takes in an index n and returns an array of all possible nCr, 0<=r<=n.
def choose(n):
    #use a temp row to minimize space used
    choose_row = [1]
    temp_row = [1]
    if n < 0:
        return "Not a valid index"
    elif n == 0:
        return choose_row
    else:
        cur_index = 0
        while cur_index < n:
            temp_row = copy.deepcopy(choose_row)
            for i in range(len(temp_row) + 1):
                if i == 0:
                    choose_row[i] = 1
                elif i == len(choose_row): #append to choose_row
                    choose_row.append(1)
                else: #use Pascal's Identity if not an end column
                    choose_row[i] = temp_row[i-1] + temp_row[i]
                    choose_row[i] %= n #only working mod n in AKS
            cur_index += 1
        return choose_row

#Note that the AKS algorithm consists roughly of 4 steps, and the bounds chosen
#are somewhat arbitrary (but generally conform to how the proof goes)
#Step 1: is n a perfect power?
def step1(n, log_n):
    for j in range(2, int(math.floor(log_n)) + 1):
            #print(i, " is the number we're on")
            if is_power(n, j):
                print(n, j)
                return False
    return True

#Step 2: is n divisible by anything (primes) below 100(logn)^5?
def step2(n, log_n):
    up_bound = int(math.floor(log_n ** 5 * 100))
    for i in range(2, up_bound):
        if is_divisible(n, i):
            print(n, i)
            return True
    return False

#Step 3: find smallest integer r such that order of n >= 9(logn)^2.
#r guaranteed by a lemma proven in the notes.
def step3(n, log_n):
    min_order = int(math.floor(log_n ** 2 * 9))
    up_bound = int(math.floor(log_n ** 5 * 100))
    r = 0
    for i in range(2, up_bound):
        if euclidean(n, i) == 1:
            temp = order(n, i)
            #print(i, temp)
            if temp >= min_order:
                r = temp
                break
    return r

#Step 4: Check that all 1 <= a <= r satisfy (x+a)^n = x^n + a mod(n,x^r-1)
#this step works because you can substitute x^r = 1 into any exponent of x
#greater than or equal to r to check all coefficients in polynomial time.
#(r grows in polynomial time.)
def step4(n, r):
    choose_nums = choose(n)
    for a in range(1, r + 1):
        aks_poly = []
        for i in range(n + 1):
            poly_term = choose_nums[i] * (a ** (n-i))
            if i >= r:
                aks_poly[i % r] += poly_term
            else:
                aks_poly.append(poly_term)
            aks_poly[i % r] %= n
        for i in range(1, n):
            if aks_poly[i] != 0:
                return False
                break
    return True

if __name__ == "__main__":
    #n will be the number to check
    n = 255
    is_prime = True
    log_n = math.log(n, 10)

    if not step1(n, log_n):
        is_prime = False
        print("Failed step 1: is a perfect power.")
    elif step2(n, log_n):
        is_prime = False
        print("Failed step 2: is divisible by something up to 100(logn)^5")
    else:
        min_r = step3(n, log_n)
        if not step4(n, min_r):
            is_prime = False
            print("Failed step 4: fails (x+a)^n = x^n + a mod (n, x^r - 1)")
        else:
            is_prime = True
            print("Hooray, %d is prime!" % (n))

