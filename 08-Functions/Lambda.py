# def temp_conv(c):
#     return 9/5 * c + 32

temp = [33.5,36.7,32.1,38.7,29.7]
f = list(map(lambda c : 9/5 * c + 32, temp))
print(f)

# numbers = []
# for n in range(1,51):
#     numbers.append(n)

even = list(filter(lambda n : n % 2 == 0, [num for num in range(1,51)]))
print(even)