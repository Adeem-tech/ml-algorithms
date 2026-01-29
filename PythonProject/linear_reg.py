import numpy as np
import matplotlib.pyplot as plot

x = np.array([1, 2, 3, 4, 5])
y = np.array([1.1, 1.8, 2.5, 3.2, 3.8])

x_mean = np.mean(x)
y_mean = np.mean(y)

numerator = np.sum((x - x_mean) * (y - y_mean))
denominator = np.sum((x - x_mean) ** 2)
m = numerator / denominator

c = y_mean - m * x_mean

y_pred = m * x + c

print(f"Slope (m):{m:.3f}")
print(f"Intercept (c):{c:.3f}")
print(f"Regression Equation: y = {m:.3f}x + {c:.3f}")

x_new = float(input("Enter a new value of X: "))
y_new = m * x_new + c
print(f"Predicted value of Y for X = {x_new} is Y = {y_new:.3f}")

x_line = np.linspace(min(x) - 1, max(x) + 1, 100)
y_line = m * x_line + c

plot.scatter(x, y, label="Actual Data")
plot.plot(x_line, y_line, label="Regression Line")
plot.scatter(x_new, y_new, marker='x', s=60, label="Predicted Point")

plot.xlabel("X")
plot.ylabel("Y")
plot.title("Linear Regression")
plot.legend()
plot.grid(True)
plot.show()