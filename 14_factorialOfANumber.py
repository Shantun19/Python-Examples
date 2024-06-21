# factorial of a Number 

num = int(input('Enter a Number')) # 5 
fact = 1

for i in range(1 , num+1): # 1 , 2 , 3 , 4 , 5
    fact = fact * i
    

print('the factorial of {} is {}'.format(num , fact))
