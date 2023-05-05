import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Read CSV file
df = pd.read_csv('count.csv')

# Set x and y columns
x_col = 0  # First column
y_col = 1  # Second column

# Extract x and y values
x = df.iloc[:, x_col]
y = df.iloc[:, y_col]

# Set figure size and spacing
fig, ax = plt.subplots(figsize=(8, 6))  # Set figure size
ax.tick_params(axis='both', which='major', pad=10)  # Set tick spacing
ax.xaxis.set_major_locator(plt.MaxNLocator(7))  # Set x-axis tick spacing
ax.yaxis.set_major_locator(plt.MaxNLocator(8))  # Set y-axis tick spacing

# Plot the graph
ax.scatter(x, y, s = 0.01) # Change value of s to change size of dots
ax.set_xlabel("Size of protein", labelpad=15)  # Set x-axis label to column name
ax.set_ylabel(df.columns[y_col], labelpad=15)  # Set y-axis label to column name
ax.set_title('CSV Data')  # Set title

# # Set the range of the x-axis and y-axis
# ax.set_xlim([0, 100])  # Set x-axis range to 0-10
# ax.set_ylim([0, 100])  # Set y-axis range to 0-8


# Fill regions between x tick spacing with alternating colors
colors = ['blue', 'red', 'green', 'yellow','orange', 'violet', 'indigo']  # Customize the list of colors
for i in range(len(ax.get_xticks())-1):
    start_x = ax.get_xticks()[i]
    end_x = ax.get_xticks()[i+1]
    if start_x < 0:
        start_x = 0
    if end_x < 0:
        continue
    ax.axvspan(start_x, min(end_x, max(x)), alpha=0.2, color=colors[i%len(colors)])


plt.show()
