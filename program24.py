start = int(input("Enter the start point : "))
end = int(input("Enter the end point : "))
for n in range(start,end + 1):
   if n > 1:
       for i in range(2,n):
           if (n % i) == 0:
               break
       else:
           print(n)