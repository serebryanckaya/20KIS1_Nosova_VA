l = []
def sum_digits(b):
    if (b == 0):
        return l
    dig = b % 10
    l.append(dig)
    sum_digits(b // 10)
n = int(input("Введите число: "))
sum_digits(n)
print(sum(l))