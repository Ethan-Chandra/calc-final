import helper

def midpointRiemann(x, y, ax):   
     
    axObject = ax[1,0]
    maxElements = len(x)
    area = 0
   
    helper.drawXAndYAxis(axObject)

    helper.plotGraph(x, y, axObject)

    # Create visual bars and add area
    for i in range(0, (maxElements-2), 2):
        width = (x[i+2] - x[i])
        height = y[i+1]

        # aligned with edge and start at current x point to allow for graphing uneven midpoints  
        # align center does not work     
        axObject.bar(x[i], height, width, align="edge", alpha=0.2, facecolor='C0', edgecolor='b')
        area += (width * height)
    
    axObject.set_title(f"Midpoint Riemann Sum (Area = {area})")