def str_reverse(numbers):
    rev = ''
    n = len(numbers)
    while n > 0:
        rev += numbers[n - 1]
        n = n - 1
    return rev
print(str_reverse('1234abcd'))
