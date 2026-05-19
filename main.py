import matplotlib.pyplot as plt
import numpy as np
from leftRiemann import plotLeftRiemann
from rightRiemann import plotRightRiemann
from midpointRiemann import midpointRiemann
from trapezoidalSum import trapezoidalSum

# x and y arrays will always have the same number of elements
fig, ax = plt.subplots(2, 2)
plt.get_current_fig_manager().full_screen_toggle()

# Left Riemann
xLeft = [1, 3, 5, 9, 11, 14, 15]
yLeft = [-5, -10, 3, 2, 5, 7, 6]
# xLeft = [0, 2, 5, 7, 10]
# yLeft = [2, 3, 5, 7, 8]
plotLeftRiemann(xLeft, yLeft, ax)

# Right Riemann
xRight = [0, 4, 9, 10, 12, 19]
yRight = [-3, -5, -4, -2, -1, 1]
plotRightRiemann(xRight, yRight, ax)

# Midpoint Riemann (Must have an odd number of points)
# xMid = [0, 1, 2, 3, 4, 5, 6]
# yMid = [0, 5.3, 8.8, 11.2, 12.8, 13.8, 14.5]
xMid = [1, 3, 4, 7, 8, 13, 15, 18, 22]
yMid = [3, 5, 7, 10, 12, 17, 20, 24, 28]
midpointRiemann(xMid, yMid, ax)

# Trapezoidal Sum
# xTrap = [1, 4, 7, 10]
# yTrap = [2, 5, 3, 8]
xTrap = [0, 2, 5, 7, 8]
yTrap = [0, 4, 13, 21, 23]
trapezoidalSum(xTrap, yTrap, ax)

plt.show()