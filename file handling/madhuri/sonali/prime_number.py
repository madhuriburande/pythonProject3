def isprime_num(n):
    if n<=1:
        return False
    for i in range(2,n):
        if (n%i)==0:
            return False
    return True

## or 

def prime():
    
    for num in range(100,200):
        for i in range(2,num):
            if (num%i)==0:
                break
                print(num,"is not prime number")
        else:
            print(num,"is  prime number")
      
               







    