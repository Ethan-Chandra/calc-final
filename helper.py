def drawXAndYAxis(axObject):
    # Changing boundary lines (spine) positions to make x and y axis
    axObject.spines['left'].set_position('zero')

    axObject.spines['right'].set_color('none')
    axObject.yaxis.tick_left()
    axObject.spines['bottom'].set_position('zero')

    axObject.spines['top'].set_color('none')
    axObject.xaxis.tick_bottom()

def plotGraph(x, y, axObject):
    # Graphing and points
    axObject.plot(x, y)
    axObject.plot(x, y, 'ro')