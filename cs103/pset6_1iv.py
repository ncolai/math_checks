import re
#tests if DFA accepts given strings (ends in A) or rejects (ends in R)
if __name__ == "__main__":
    letters = 'yd'
    combos = [j + k + l + m for i in letters for j in letters for k in letters for l in letters for m in letters]
    output = open('1iv.txt', 'w');
    for c in combos:
        my_sum = 0
        is_valid = True
        for letter in c:
            if my_sum * my_sum > 4:
                is_valid = False
                break
            elif letter == 'y':
                my_sum += 1
            elif letter == 'd':
                my_sum -= 1

        if is_valid:
            #output.write(c + 'A' + '\n')
            output.write(c + '\n')
        else:
            #output.write(c + 'R' + '\n')
            output.write(c + '\n')

