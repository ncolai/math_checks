
#tests if CFG accepts given strings or rejects
if __name__ == "__main__":
    letters = 'ab'
    combos = [i + j + k + l + m for i in letters for j in letters for k in letters for l in letters for m in letters]
    output = open('8_1iii.txt', 'w');
    for c in combos:
        output.write(c + '\n')

