def multi_inter(a, b):
    result = 0
    while b > 0:
        result += a
        b -= 1
    return result
a = input('first number')
b = 5
print('Answer: ', multi_inter(a, b))