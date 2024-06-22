# weather a number is amstrong or not 

num = int(input('Enter a number')) # 9474
temp = num # 9474 
sum = 0

def calculteDigits(num):
    return len(str(num))

# calculate the digits 
while temp > 0:
    digits = calculteDigits(num)
    sum += (temp%10) ** digits
    temp = temp//10
    
if num == sum:
    print('{} is a amstrong number'.format(num))
else :
    print('{} is not a amstrong number'.format(num))
