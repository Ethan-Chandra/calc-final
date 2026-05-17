import matplotlib.pyplot as plt
import numpy as np
from leftRiemann import plotLeftRiemann

# x and y arrays will always have the same number of elements
fig, ax = plt.subplots(2, 2)
plt.get_current_fig_manager().full_screen_toggle()
plt.minorticks_on() # Set small y-axis ticks

# Left Riemann
xLeft = [1, 3, 5, 9, 11, 14, 15]
yLeft = [-5, -10, 3, 2, 5, 7, 6]
plotLeftRiemann(xLeft, yLeft, ax)

# Right Riemann


plt.show()