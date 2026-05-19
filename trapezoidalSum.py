import helper

def trapezoidalSum(x, y, ax):   
     
    axObject = ax[1,1]
    maxIndex = len(x) - 1
    area = 0
   
    helper.drawXAndYAxis(axObject)

    helper.plotGraph(x, y, axObject)

    # Create visual bars and add area
    for i in range(0, maxIndex):
        # x and y points for vertices of trapezoid
        xs = [x[i], x[i], x[i+1], x[i+1]]
        ys = [0, y[i], y[i+1], 0]

        heightSum = y[i] + y[i+1]
        width = x[i+1] - x[i]

        # fill in shape from vertices
        axObject.fill(xs, ys, alpha=0.2, facecolor='C0', edgecolor='b')
        area += (heightSum * width)

    area /= 2
    
    axObject.set_title(f"Trapezoidal Sum (Area = {area})")