from cmath import nan
import csv
from dataclasses import replace
from math import prod
from re import L 
import numpy as np
from sqlalchemy import column
import statsmodels.formula.api as smf
import statsmodels.api as sm
from collections import Counter
import matplotlib.pyplot as plt
import pandas as pd
from fpdf import FPDF
import random 

data = list(csv.reader(open("/Users/matthewzhang/Desktop/Data/ashit.csv"))) 
# print(str(data[0][0]))
# print(data)


def randomSelect():
    list = []
    x = random.randint(0, 7)
    y = random.randint(0, 13) 
    list.append(x)
    list.append(y)
    return list 

def method(seen, houses, number):
    for i in range(number):
        random = randomSelect()
        if random not in seen and data[random[1]][random[0]] != '':
            seen.append(random)
            houses.append(data[random[1]][random[0]])
        if data[random[1]][random[0]] == '':
            return i 

def randomlySelecting(number):
    houses = []
    seen = []
    num  = number 
    while len(houses) < num:
        method(seen, houses, 1)
    return houses

def getProportionsSample(houses):
    numerator = 0
    denominator = len(houses)
    for item in houses:
        if int(item) == 1:
            numerator += 1 
    i = numerator / denominator
    return float(i)

def getProportionzSample(houses, bouses):
    summedProportions = (getProportionsSample(houses) + getProportionsSample(bouses)) / 2 
    return summedProportions 

def populationProportion():
    rows = len(data)
    cols = len(data[0])
    numerator = 0
    denominator = 0 
    for x in range(rows):
        for y in range(cols):
            # print(data[x][y])
            if data[x][y] != '':
                denominator += 1 
                if int(data[x][y]) == 1:
                    numerator += 1
    i = numerator / denominator
    return float(i)

def notPopProp(arr):
    not_pop = []
    for item in arr:
        if(item != 0.5):
            not_pop.append(item)
    return len(not_pop)/len(arr)

def getProportionsListSingles(x, y):
    bob = []
    for i in range(x):
        bob.append(getProportionsSample(randomlySelecting(y)))
    return bob 

def getProportionsListDuols(x, y):
    bob = []
    for i in range(x):
        bob.append(getProportionzSample(randomlySelecting(y), randomlySelecting(y)))
    return bob     

def getProportionsMore(x, y, z):
    bob = []
    k = 0
    for i in range(x):
        for o in range(z):
            list = randomlySelecting(y)
            k += getProportionsSample(list)
        proportion = k / z
        # print(k)
        bob.append(proportion)
        k = 0 
    return bob 

def percetiles(arr):
    quarter = np.percentile(arr,25)
    three_quarter = np.percentile(arr,75)
    range = three_quarter - quarter
    percetiles.getQuarter3 = three_quarter
    percetiles.getQuarter = quarter 
    return range

def inRange(arr):
    i = 0 
    for item in arr:
        if item > 0.4 and item < 0.6:
            i +=1 
    return i / len(arr)
def inRangeIncrements(arr):
    i = 0 
    increment = 0.5
    incrementBottom = 0.5
    proportions = []
    range = [] 
    while float(increment) != float(0.55):
        for item in arr:
            if item <= increment and item >= incrementBottom:
                i += 1 
        proportions.append(i / len(arr))
        range.append(increment - incrementBottom)
        increment += 0.01
        incrementBottom = incrementBottom - 0.01 
        i = 0 
    plt.xlabel("Acceptable Range")
    plt.ylabel("Proportion of samples in Range")
    plt.plot(range, proportions)
    plt.show() 

def getNumbercorrect(arr):
    num = 0 
    for item in arr:
        if float(round(item, 1)) == float(0.50):
            num += 1 
    return num 


def getProportionsListMultiple(x):
    proportions = []
    j = 0
    list = []
    t = 1
    for i in range(1, x, 1):
        list = getProportionsMore(2000, 30, t)
        # print(list)
        j = getNumbercorrect(list)
        print(j)
        # print(j/200)
        proportions.append(j / 2000)
        t += 1
        
    return proportions 

def graphAllZeroFives(times):
    len = []
    i = 0
    for x in range(times):
        i += 1
        len.append(i)
    plt.plot(len, getProportionsListMultiple(times + 1))
    plt.xlabel("Number of Times Sampled")
    plt.ylabel("Proportion of samples with distrbution the exact same as population")
    plt.show()

graphAllZeroFives(20)

# plt.hist(pop, edgecolor ="red", bins=20)
# print(inRange(bob))
# print(inRange(pop)) 

# print(percetiles(bob))
# print(percetiles.getQuarter3)
# print(percetiles.getQuarter)
# print(percetiles(pop))
# plt.hist(bob, edgecolor ="red", bins=20)
# plt.show()
# print(inRange(bob))
# print(inRange(pop))
# print(notPopProp(bob))
# print(percetiles(bob))
# print(notPopProp(pop))
# print(percetiles(pop))
# plt.hist(bob)
# plt.show()
# print(populationProportion())
# bob = getProportionsListDuols(20000, 30) 
# pop = getProportionsListSingles(20000, 30) 
# inRangeIncrements(bob)
# inRangeIncrements(pop)

            