import re
#tests if DFA accepts given strings (ends in A) or rejects (ends in R)
if __name__ == "__main__":
    letters2 = 'ab '
    letters = 'ab'
    combos = [i + j + k + l for i in letters for j in letters for k in letters for l in letters2]
    output = open('1ii.txt', 'w');
    for c in combos:
        my_sum = 0
        ab = [m.start() for m in re.finditer('ab', c)]
        ba = [m.start() for m in re.finditer('ba', c)]
        if len(ab) == len(ba):
            output.write(c + 'A' + '\n')
        else:
            output.write(c + 'R' + '\n')
