import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# ===== Training datasets
# input - data:
# [[height (cm)], [], ...]
X = np.array([[147, 150, 153, 158, 163, 165, 168, 170, 173, 175, 178, 180, 183]]).T

# outcome - label: 
# [[weight (kg)], [], ...]
y = np.array([[ 49, 50, 51,  54, 58, 59, 60, 62, 63, 64, 66, 67, 68]]).T

# print('X =', X)
# print('y =', y)

# ===== Visualize data
# plt.plot(X, y, 'ro')
# plt.axis([120, 190, 30, 100])


# ===== Initial Xbar
# X.shape[0] => size: n = 13
# np.one((nrow, ncol)): matrx value 1, size n x 1
# xbar = [[1, x1], [1, x2], ...]
one = np.ones((X.shape[0], 1))
Xbar = np.concatenate((one, X), axis = 1)

# print(one)
# print('Xbar =', Xbar)


# ===== Calculate w[]
# np.linalg.pinv: Pseudo Inverse
A = np.dot(Xbar.T, Xbar)
b = np.dot(Xbar.T, y)
w = np.dot(np.linalg.pinv(A), b)

print('w = ', w)

w_0 = w[0][0]
w_1 = w[1][0]

# Use package skylearn
skl = LinearRegression(fit_intercept=False)
skl.fit(Xbar, y)
print('Skyclea use', skl.coef_)


# ===== test set with new data
def test_data(h, rw):
    w = w_1 * h + w_0
    print( u'Predict weight of height %d cm: %.2f (kg), real number: %.2f (kg)'  %(h, w, rw))

test_data(155, 52)
test_data(160, 56)


# ===== pyplot
x0 = np.linspace(120, 190, 2)
y0 = w_0 + w_1 * x0

plt.plot(x0, y0)
plt.plot(X.T, y.T, 'ro')
plt.axis([120, 190, 30, 100])
plt.xlabel('Height (cm)')
plt.ylabel('Weight (kg)')


# Draw figure
plt.grid()
plt.show()
