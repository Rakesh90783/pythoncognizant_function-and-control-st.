def cases(s):
    return str(s).upper(), str(s).lower()


chrars = {'a', 'b', 'E', 'f', 'a', 'i', 'o', 'U', 'a'}
print("Original Characters:\n", chrars)

result = map(cases, chrars)
print("\nafter converting above characters in upper and lower cases\nand eliminating duplicate letters:")
print(set(result))