import numpy as np
def sigmoid(z):
    return 1 / (1 + np.exp(-z))
def cost_function(y, y_pred):
    m = len(y)
    cost = -(1/m) * np.sum(y * np.log(y_pred) + (1 - y) * np.log(1-y_pred))
    return cost
X = np.array([0.2, 0.4, 0.6])
y = np.array([0, 1, 1])
theta = 0.5
z = X * theta
y_pred = sigmoid(z)
print(f"Predicted probablities: {y_pred}")
print(f"Cost function Value: {cost_function(y, y_pred)}")