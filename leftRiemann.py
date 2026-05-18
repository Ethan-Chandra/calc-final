import helper

"""
Function: Plots left riemann sum

Preconditions:
    - x: 
        - must be a non-empty array with numerical types 
        - must have same amount of elements as y array
    - y: 
        - must be a non-empty array with numerical types 
        - must have same amount of elements as x array
    - ax: must be an axes object

Postconditions:
    - Plots the left riemann sum
"""
def plotLeftRiemann(x, y, ax):   
     
    axObject = ax[0,0]
    maxIndex = (len(x) - 1)
    area = 0

    helper.drawXAndYAxis(axObject)

    helper.plotGraph(x, y, axObject)

    # Create visual bars and add area
    for i in range(0, maxIndex):
        width = x[i+1] - x[i]
        height = y[i]

        axObject.bar(x[i], height, width, align="edge", alpha=0.2, facecolor='C0', edgecolor='b')
        area += (width * height)
    
    axObject.set_title(f"Left Riemann Sum (Area = {area})")
