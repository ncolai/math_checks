#tests if DFA accepts given strings (ends in A) or rejects (ends in R)
if __name__ == "__main__":
    letters = 'abc'
    combos = [i + j + k + l for i in letters for j in letters for k in letters for l in letters]
    output = open('1i.txt', 'w');
    for c in combos:
        my_sum = 0
        for i in range(len(c)):
            if c[i] == 'c':
                my_sum += 1
        if my_sum is 2:
            output.write(c + 'A' + '\n')
        else:
            output.write(c + 'R' + '\n')

