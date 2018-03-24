# Lambda - Anonymous Function

# def temp_conv(c):
#     return 9 / 5 * c + 32

# temp_conv = lambda c : 9 / 5 * c + 32
# print(temp_conv(33.4))

cel = [34.5,32.3,36.7,33.1,38.2]

f = list(map(lambda c : 9 / 5 * c + 32, cel))

print(f)