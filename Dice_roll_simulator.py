import numpy as np
import matplotlib.pyplot as plt
import random

dices_amount = int(input("How many dices do you want to throw? "))
dices_thrown_amount = int(input(f"How many times do yo want to throw the {dices_amount} dices? "))

dice_values = np.zeros((dices_amount,dices_thrown_amount))

def diceRoller(amount,throw):
    """Creates a"amount" of dices
    and "throw" them an amount of time
    returning the values as list
    """
    diceVals = np.zeros((amount,throw))
    
    for i in range(amount):
        for j in range(throw):
            diceVals[i,j] = random.randrange(1,7)
        
    return diceVals


def diceFrequencyCalculator(diceList):
        """Calculates the amount
        of each number, and the frequency
        """
        resultOfThrowDict = {
            "1": 0,
            "2": 0,
            "3": 0,
            "4": 0,
            "5": 0,
            "6": 0,
            } 
        for i in range(len(diceList)):
            for j in range(len(diceList[0])):
                if diceList[i,j] == 1:
                    resultOfThrowDict["1"] += 1
                elif diceList[i,j] == 2:
                    resultOfThrowDict["2"] += 1
                elif diceList[i,j]  == 3:
                    resultOfThrowDict["3"] += 1
                elif diceList[i,j]  == 4:
                    resultOfThrowDict["4"] += 1
                elif diceList[i,j]  == 5:
                    resultOfThrowDict["5"]+= 1
                elif diceList[i,j]  == 6:
                    resultOfThrowDict["6"] += 1
        return resultOfThrowDict

def PlotHistogram(resultOfThrow):
    for i in range(len(resultOfThrow)):
        plt.bar(resultOfThrow[i],resultOfThrow[i][i] )

dice_values =  diceRoller(dices_amount, dices_thrown_amount)
resultOfThrow = diceFrequencyCalculator(dice_values)

# print(dice_values)
# print(f"We got:\t\n{resultOfThrow['1']} 1s,\t\n{resultOfThrow['2']} 2s,\t\n{resultOfThrow['3']} 3s,\t\n{resultOfThrow['4']} 4s, \t\n{resultOfThrow['5']} 5s, \t\n{resultOfThrow['6']} 6s")

x = np.array(list(resultOfThrow.keys()))
y = np.array(list(resultOfThrow.values()))

plt.hist(x,y)