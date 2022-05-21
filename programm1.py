def maximum(x, y, z):
    if x > y & x > z:
        max = x
    elif y > x & y > z:
        max = y
    else:
        max = z
    return max

x = 4
y = 5
z = 6
print(maximum(x, y, z))