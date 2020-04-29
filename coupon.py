from random import random

n = int(input("Enter the Number of Distinct coupon You Want: "))
randomList = []
count = 0

def pow():
    rangeOfRandom = 10
    temp = n
    while temp != 0:
        rangeOfRandom *= 10
        temp //= 10
    return rangeOfRandom

while True:
    number = int((random() * pow()) // 10)
    count += 1
    if number not in randomList:
        randomList.append(number)
    if len(randomList) == n:
        break
print("Total Number of Random number Generated: ",count)
print("Random Numbers are :",end=" ")
for i in range(0,len(randomList)):
    print(randomList[i],end=" ")
print()
