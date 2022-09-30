import matplotlib.pyplot as plt
import numpy as np
from sklearn import linear_model
from sklearn.metrics import r2_score


# Enter data - OD595 reading for x; BSA concentration (mg/ml) for y
x_0 = np.array([0.94, 0.5, 0.27, 0.1, 0.01])
x_1 = np.array([0.722, 0.548, 0.260, 0.119])
x_2 = np.array([0.905, 0.704, 0.504, 0.294])
x_3 = np.array([0.940, 0.776, 0.634, 0.436, 0.244])
x = np.array([])
x_modified = np.reshape(x, (-1, 1))
y = np.array([20, 16, 12, 8, 4])
y_0 = np.array([20, 10, 5, 2, 0.2])

# Create linear regression object
regr = linear_model.LinearRegression(fit_intercept=False)

# Train the model
regr.fit(x_modified, y)

# Predicition
y_pred = regr.predict(x_modified)

slope = regr.coef_
r2 = r2_score(y, y_pred)
a = np.linspace(0, 1, 10)
b = slope[0] * a + regr.intercept_

plt.plot(x, y, '.')
plt.plot(a, b)
plt.xlabel('OD595')
plt.ylabel('[P](mg/ml)')
slope = round(slope[0], 2)
r2 = round(r2, 3)
plt.text(0, 18, 'slope={}\n\nr^2={}'.format(slope, r2))
plt.show()
