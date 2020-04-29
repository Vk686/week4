import random

stake = int(input("Enter the value of Stake : "))
goal = int(input("Enter the value of Goal : "))
trails = int(input("Enter the value of Trail : "))
win = 0
loss = 0
winPercent = 0.0
lossPercent = 0.0
for x in range(trails):
    cash = stake
    while cash > 0 and cash < goal:
        if random.randrange(0,2) == 0:
            cash += 1
        else:
            cash -= 1

    if cash == goal:
        win += 1
    else:
        loss += 1
print("wins         : ",win)
print("loss         : ",loss)
print("win %        : ",(100 * win)/trails)
print("loss %       : ",(100 * loss)/trails)
