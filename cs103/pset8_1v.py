import re

#tests if CFG accepts given strings or rejects
if __name__ == "__main__":
    letters = 'yd'
    combos = [j + k + l + m + n for j in letters for k in letters for l in letters for m in letters for n in letters]
    output = open('8_1v.txt', 'w');
    n_matches = 0
    for c in combos:
        num_y = [y.start() for y in re.finditer('y', c)]
        num_d = [d.start() for d in re.finditer('d', c)]
        print(num_y)
        print(num_d)
        if len(num_d) == len(num_y):
            output.write(c + 'A--------------' + '\n')
            n_matches += 1
        else:
            output.write(c + 'R' + '\n')

    output.write(str(n_matches) + '\n')

