#tests if DFA accepts given strings (ends in A) or rejects (ends in R)
if __name__ == "__main__":
    letters = 'abc'
    combos = [i + j + k + l + m for i in letters for j in letters for k in letters for l in letters for m in letters]
    output = open('1iii.txt', 'w');
    for c in combos:
        output.write(c + 'cocoa' + 'A' + '\n');
