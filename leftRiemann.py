import matplotlib.pyplot as plt
import numpy as np
import helper

def plotLeftRiemann(x, y, ax):    

    axObject = ax[0,0]
    maxIndex = (len(x) - 1)
    area = 0
    # [:-1] creates a new array with all elements of the mentioned array excluding its last element
    leftX = x[:-1] 
    leftY = y[:-1]

    helper.drawXAndYAxis(axObject)

    helper.plotGraph(x, y, axObject)

    # Create visual bars and add area
    for i in range(0, maxIndex):
        width = x[i+1] - x[i]
        height = y[i]

        axObject.bar(leftX[i], leftY[i], width, align="edge", alpha=0.2, facecolor='C0', edgecolor='b')
        area += (width * height)
    
    axObject.set_title(f"Left Riemann Sum (Area = {area})")
