import numpy as np 
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt 
# Sample data: hours studied vs. scores obtained
x = np.array([1, 2, 3, 4, 5]).reshape(-1, 1)  # Hours studied
y = np.array([45, 50, 60,68, 75])  # Scores obtained

# Create and train the module
model = LinearRegression()
model.fit(x, y)

# Make Predictions
pred = model.predict([[6]]) # predict score for 6 hours of study 
print(f"Predicted Value of study: ", pred[0])
# Visualize the results(matplotlib)
plt.scatter(x, y, color = "blue")
plt.xlabel("Study Hours")
plt.ylabel("Score(Result)")
plt.title("Linear Regression(Study Hours vs Score)")
plt.plot(x, model.predict(x), color = "red")
plt.show()
