def generate(poly, exp, size):
    for r in range(exp):
        for i in range(6,-1, -1):
            poly[i + 1] += poly[i]
            poly[i + 1] %= 2

        if poly[5] >= 1:
            poly[2] += poly[5]
            poly[2] %= 2
            poly[0] += poly[5]
            poly[0] %= 2
            poly[5] = 0
        print(poly)

    

if __name__ == "__main__":
    poly = [1,1,0,0,0,0,0,0,0,0,0,0]
    generate(poly, 32, 32)
