import helper

def plotRightRiemann(x, y, ax):   
     
    axObject = ax[0,1]
    maxIndex = (len(x) - 1)
    area = 0
    # [1:] returns a new array with all elements excluding the first
    rightX = x[1:]
    rightY = y[1:]

    helper.drawXAndYAxis(axObject)

    helper.plotGraph(x, y, axObject)

    # Create visual bars and add area
    for i in range(0, maxIndex):
        width = (x[i+1] - x[i])
        height = rightY[i]

        axObject.bar(rightX[i], height, (width * -1), align="edge", alpha=0.2, facecolor='C0', edgecolor='b')
        area += (width * height)
    
    axObject.set_title(f"Right Riemann Sum (Area = {area})")