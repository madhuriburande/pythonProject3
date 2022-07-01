def Fib(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return Fib(n-1)+Fib(n-2)

### or range between 0 to 12
def Fib_num(no):
    if no==0:
        return 1
    elif no==1:
         return 1
    else:
        return Fib_num(no-1)+Fib_num(no-2)
for i in range(0,12):
    print(Fib_num(i))