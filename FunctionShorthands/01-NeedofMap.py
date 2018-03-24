def temp_conv(c):
    return 9 / 5 * c + 32

cel = [34.5,32.3,36.7,33.1,38.2]

# f = []

# for temp in cel:
#     f.append(temp_conv(temp))

f = list(map(temp_conv, cel))

print(f)