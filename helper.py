"""
Function: Creates x and y axis on graph

Preconditions:
    - axObject: must be an axes object

Postconditions:
    - Draws x and y axis on graph
"""
def drawXAndYAxis(axObject):
    # Changing boundary lines (spine) positions to make x and y axis
    axObject.spines['left'].set_position('zero')

    axObject.spines['right'].set_color('none')
    axObject.yaxis.tick_left()
    axObject.spines['bottom'].set_position('zero')

    axObject.spines['top'].set_color('none')
    axObject.xaxis.tick_bottom()

"""
Function: Plots graph, points, and area bars

Preconditions:
    - x: 
        - must be a non-empty array with numerical types 
        - must have same amount of elements as y array
    - y: 
        - must be a non-empty array with numerical types 
        - must have same amount of elements as x array
    - axObject: must be an axes object

Postconditions:
    - Plots graph, points, and area bars
"""
def plotGraph(x, y, axObject):
    axObject.plot(x, y)
    axObject.plot(x, y, 'ro')