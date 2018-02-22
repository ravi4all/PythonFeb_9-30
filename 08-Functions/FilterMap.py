def temp_conv(c):
    return 9/5 * c + 32


temp = [34.5,37.8,32.4,38.4,29.8]

# for t in temp:
#     print(temp_conv(t))

# map(arg1 - Function, arg2 - Iterable) - Applied on logic
# Iterable - List/Tuple/Sets/Dict

f = list(map(temp_conv, temp))
# print(f)

########################################################

# x = []
# def even(num):
#
#     if num % 2 == 0:
#         x.append(num)
#     return x

numbers = []
for n in range(1,51):
    numbers.append(n)

# even_nums = []
#
# for n in numbers:
#     even_nums.append(even(n))

# even_nums = []
# for n in numbers:
#     even_nums = even(n)
#
# print(even_nums)

def even(num):
    return num % 2 == 0

even_nums = list(filter(even, numbers))
print(even_nums)