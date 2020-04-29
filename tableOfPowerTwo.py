num = int(input("Enter value of N : "))
while num < 0 or num >= 50:
    print(" Num between 0 to 31...!")
    num = int(input(" Num again : "))

i = 0
powerOf2 = 1
print("Table of power 2 is : ")
while i <= num:
    print(i,powerOf2)
    powerOf2 = 2 * powerOf2
    i=i+1