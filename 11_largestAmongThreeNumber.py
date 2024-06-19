# find the largest among three number 

num1 = int(input('Enter First Number'))
num2 = int(input('Enter Second Number'))
num3 = int(input('Enter Third Number'))

if (num1 > num2) and (num2 > num3):
    print('{} is the larget number'.format(num1))
elif (num2 > num1) and (num2 > num3):
    print('{} is the largest number'.format(num2))
else:
    print('{} is the largest number'.format(num3))
