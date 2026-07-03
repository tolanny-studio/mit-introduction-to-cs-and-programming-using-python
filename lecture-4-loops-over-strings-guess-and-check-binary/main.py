s = "taoheed"

# for char in s:
#     print(char)

# for index in range(len(s)):
#     print(s[index])

# for char in s:
#     if char == 'a':
#         print("first")
#     else:
#         print(char)

# for char in s:
#     if char in 'aeiou':
#         print("vowel")
#     else:
#         print(char)


r = "abca"

unique = {}

# unique['a'] = True
#
# print(unique)
#
# print('a' in unique)


# for char in r:
#     if char not in unique:
#         unique[char] = 0
# print(len(unique))

# a,b,c = 0
#
# b = a - 2
#
# c = 2 * a

#  a + b + c = 10

# for a in range (11):
#     for b in range (11):
#         for c in range (11):
#             total = (a + b + c == 10)
#             two_less = (b == a - 2)
#             twice = (c ==  2 * a)
#
#             if total and two_less and twice:
#                 print(a)
#                 print(b)
#                 print(c)


for a in range (1001):
    b = a - 2
    c = 2 * a

    if a + b + c == 1000:
        print(a)
        print(b)
        print(c)

# x = 0
#
# for i in range(11):
#     x += 0.1
#     print(x)

bits = 1507
divisor = 2

binary = ""

while bits  > 0:

    binary = str(bits % divisor) + binary

    bits //= divisor

print(binary)