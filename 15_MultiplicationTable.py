# display multiplication table 

num = int(input('Enter a Number'))

for i in range(1 , 11):
    val = num * i
    print('{} X {} = {}'.format(num , i , val))
