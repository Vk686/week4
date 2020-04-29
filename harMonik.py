num = int(input("Enter Harmonic value N : "))
while num <= 0:
    num = int(input("please enter greater than zero value : "))

sum = 0.0
i = 1
while i <= num:
    sum += 1.0/i
    i=i+1

print(" Harmonic value is :",round(sum,2))