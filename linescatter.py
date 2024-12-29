# import matplotlib.pyplot as plt

# x = [1, 2, 3, 4, 5]  
# y_line = [2, 4, 6, 8, 10]  
# y_scatter = [2.1, 3.9, 6.2, 7.8, 10.1]  


# plt.figure(figsize=(10, 5))
# plt.subplot(1, 2, 1)  
# plt.plot(x, y_line, marker='o', linestyle='-', color='b', label='Line Chart')
# plt.title("Line Chart Example")
# plt.xlabel("X-axis")
# plt.ylabel("Y-axis")
# plt.legend()
# plt.grid(True)


# plt.subplot(1, 2, 2)  
# plt.scatter(x, y_scatter, color='r', label='Scatterplot')
# plt.title("Scatterplot Example")
# plt.xlabel("X-axis")
# plt.ylabel("Y-axis")
# plt.legend()
# plt.grid(True)


# plt.tight_layout()
# plt.show()
import matplotlib.pyplot as plt

# Example data
x = [1, 2, 3, 4, 5]
y_line = [2, 4, 6, 8, 10]
y_scatter = [2.1, 3.9, 6.2, 7.8, 10.1]

# Line Chart
plt.plot(x, y_line, label="Line Chart")
plt.scatter(x, y_scatter, color="red", label="Scatterplot")

# Add labels and legend
plt.title("Line Chart and Scatterplot")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.legend()

# Show the plot
plt.show()
