import csv
import matplotlib.pyplot as plt

filename = "new_output.csv"
data = []
sums = []
ranges = []
with open(filename, 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    next(csvreader)
    for row in csvreader:
        if row[0] and row[1] and row[4]:  # check if the strings are not empty
            data.append([float(row[0]), float(row[1]), float(row[4])])
    # print(data)

max_value = data[-1][1]
range_size = 400
for i in range(0, int(max_value), range_size):
    current_sum = 0
    current_data_sum = 0
    for item in data:
        if i <= item[0] <= i + range_size:
            current_sum += item[1] - item[0]
            current_data_sum += item[2]
    sums.append(current_data_sum)
    ranges.append(i)
    if i + range_size >= max_value:
        break

plt.plot(ranges, sums)
plt.xlabel('Ranges')
plt.ylabel('Sum of Column 5')
plt.show()