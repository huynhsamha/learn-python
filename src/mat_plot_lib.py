import math, random
import numpy as np
import matplotlib.pyplot as plt

# ===============================================
# draw by y axis
# default value x = [0, 1, 2, 3, 4]
# -----------------------------------------------
# plt.plot([4, 6, 9, 15, 23])
# plt.ylabel('some numbers')
# ...............................................


# ===============================================
# default is 'b-': solid blue line
# 'ro': circle with red
# axin([xmin, xmax, ymin, ymax] )
# -----------------------------------------------
# plt.plot([1, 2, 3, 4, 7, 9], [1, 4, 9, 16, 49, 81], 'ro')
# plt.axis([0, 10, 0, 100])
# ...............................................


# ===============================================
# t: range [0:5:0.2]
# 'r--': red dash
# 'bs': blue square (t, t^2)
# 'g^': green triangle up (t, t**3)
# 'k-.': black dash dot
# -----------------------------------------------
# t = np.arange(0., 5., 0.2)
# plt.plot(t, t, 'r--',
#          t, t**2, 'bs',
#          t, t**3, 'g^',
#          t, np.sqrt(t), 'k-.')
# ...............................................


# ===============================================

# -----------------------------------------------
# age = np.random.randint(low = 18, high = 40, size = 500)
# salary = np.random.randint(low = 200, high=10000, size = 500)
# plt.plot(age, salary, 'r.')
# ...............................................


# ===============================================
# setp(): set multiple property on list of lines
# -----------------------------------------------
# x = np.arange(0, 100, 0.1)
# line = plt.plot(x, x**2, 'b:')
# plt.setp(line, lineWidth=2.0)
# ...............................................


# ===============================================
# figure(i): go to figure i, default figure 1
# subplot(rci): figure used is divided into r rows, c cols, and we go to part i
# title(): title figure
# -----------------------------------------------
# def f(t):
#     return np.exp(-t) * np.cos(2*np.pi*t)

# t1 = np.arange(0.0, 5.0, 0.1)
# t2 = np.arange(0.0, 5.0, 0.02)

# plt.figure(1)
# plt.subplot(221)
# plt.plot(t1, f(t1), 'bo', t2, f(t2), 'k')
# plt.subplot(222)
# plt.plot(t2, np.cos(2*np.pi*t2), 'r--')
# plt.subplot(223)
# plt.plot(t2, np.sin(np.pi*t2), 'gh')

# plt.figure(2)
# plt.plot(t2, np.log2(t2), 'b.')
# plt.title('Log 2 function')
# ...............................................


# ===============================================

# -----------------------------------------------
# Fixing random state for reproducibility
np.random.seed(19680801)

mu, sigma = 100, 15
x = mu + sigma * np.random.randn(10000)

# the histogram of the data
n, bins, patches = plt.hist(x, 50, normed=1, facecolor='g', alpha=0.75)

plt.xlabel('Smarts')
plt.ylabel('Probability')
plt.title('Histogram of IQ')
plt.text(60, .025, r'$\mu=100,\ \sigma=15$')
plt.axis([40, 160, 0, 0.03])
plt.grid(True)
# ...............................................


# ===============================================

# -----------------------------------------------

# ...............................................


# ===============================================

# -----------------------------------------------

# ...............................................


# ===============================================

# -----------------------------------------------

# ...............................................


# ===============================================

# -----------------------------------------------

# ...............................................

plt.show()
