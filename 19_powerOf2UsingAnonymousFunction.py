# Python Program to Display Powers of 2 Using Anonymous Function

term = int(input('Enter the term ? '))
result = list(map(lambda x : 2 ** x , range(term)))

for i in range(term):
    print("2 raised to power",i,"is",result[i])
