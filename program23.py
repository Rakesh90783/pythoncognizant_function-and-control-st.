digits = [10,20,30,40,50]
for i in range(len(digits)):
    last_item = digits.pop()
    digits.insert(i, last_item)
print(digits)