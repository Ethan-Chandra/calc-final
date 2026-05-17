import matplotlib.pyplot as plt
import numpy as np

# x and y arrays will always have the same number of elements
x = [1, 3, 5, 9, 11, 14, 15]
y = [-5, -10, 3, 2, 5, 7, 6]
fig, ax = plt.subplots()
# plt.get_current_fig_manager().full_screen_toggle()

maxIndex = (len(x) - 1)
area = 0
# [:-1] creates a new array with all elements of an array except its last element
leftX = x[:-1] 
leftY = y[:-1]

# Create visual bars and add area
for i in range(0, maxIndex):
    width = x[i+1] - x[i]
    height = y[i]

    ax.bar(leftX[i], leftY[i], width, align="edge", alpha=0.2, facecolor='C0', edgecolor='b')
    area += (width * height)

# Changing boundary lines (spine) positions to make x and y axis
ax.spines['left'].set_position('zero')

ax.spines['right'].set_color('none')
ax.yaxis.tick_left()
ax.spines['bottom'].set_position('zero')

ax.spines['top'].set_color('none')
ax.xaxis.tick_bottom()

# Setting y-axis ticks
plt.minorticks_on()

# Graphing and points
ax.set_title("Left Riemann Sum")
ax.plot(x, y)
ax.plot(x, y, 'ro')

# TODO: change to make this rescalable with page
plt.figtext(0.47, 0.03, f"Area = {area}", fontsize=10)

plt.show()


