day = int(input("Input a day [1-31]: "))
month_length = 31
if day < month_length:
    day += 1
else:
    print("U have not belong to our planet.")
print("The next date is %d" % day)
