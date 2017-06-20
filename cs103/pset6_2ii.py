
#tests if DFA accepts given strings (ends in A) or rejects (ends in R)
if __name__ == "__main__":
    letters = 'abcde'
    combos = [i + j + k + l for i in letters for j in letters for k in letters for l in letters]
    output = open('2ii.txt', 'w');
    for c in combos:
        if c[len(c) - 1] in c[:-1]:
            output.write(c + 'R' + '\n')
        else:
            output.write(c + 'A' + '\n')

