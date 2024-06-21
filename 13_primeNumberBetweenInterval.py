# all the prime number in an interval.

num1 = int(input('Enter first Number'))
num2 = int(input('Enter second Number'))

def checkPrime(num):
    if num <= 2: # 0 , 1 , 2
        return False
        
    for i in range(2 , num): # 2 --- 10 
        if (num%i == 0):
            return False
    
    return True
    
for i in range(num1 , num2):
    if checkPrime(i):
        print(i)
    
