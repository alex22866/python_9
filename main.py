# a = [1, 2, 3, 4, 5]
# b = 0
# for i in a:
#   b = b + 1
#  print(b)
# print(b)


print("10 000$")
a = float(input())

print("5 years ?")
years = int(input())


def bank(a, years):
    i = 0
    while i < years:
        a = a + a * 0.1
        i = i + 1
    return a


print(bank(a, years))
