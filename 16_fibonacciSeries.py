num = int(input('Enter the number'))

if num <= 1:
    print(num)
    
firstTerm = 0
secondTerm = 1

count = 0

for i in range(0 , num):
    print(firstTerm)
    nterm = firstTerm + secondTerm 
    firstTerm = secondTerm
    secondTerm = nterm
