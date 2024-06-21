# check the number is a prime or not (1 , n)

#user input 
num = int(input('Enter a Number')) #5 

flag = False

for i in range(2 , num): # 2 , 3 , 4 
    if (num%i) == 0:
        flag = True
        break;

if flag:
    print('{} is not a prime number'.format(num))
else:
    print('{} is a prime number'.format(num))
    
