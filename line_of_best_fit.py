import pandas as pd
import matplotlib.pyplot as plt

dataset = pd.read_csv('\\Users\\hamza\\Documents\\VS Code\\Python\\Line of Best Fit\\data.csv')
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, -1].values

def mean(d): return sum(d)/len(d)

def std_dev(d):
    d_mean = mean(d)
    numerator = 0
    for e in d:
        numerator += (e-d_mean)**2
    return (numerator/(len(d)-1))**(1/2)

def corr_coeff(X, y):
    n = len(X)
    Xy = []
    for i in range(n):
        Xy.append(X[i]*y[i])
    X_sq = [e**2 for e in X]
    y_sq = [e**2 for e in y]
    numerator = n*sum(Xy)-sum(X)*sum(y)
    denominator = ((n*sum(X_sq)-sum(X)**2)*(n*sum(y_sq)-sum(y)**2))**(1/2)
    return numerator/denominator

def slope(r, std_dev_X, std_dev_y): return r*(std_dev_y/std_dev_X)

def y_intercept(slope, X_mean, y_mean): return y_mean-(slope*X_mean)

def equation_coeffs(X, y):
    X_mean = mean(X)
    y_mean = mean(y)
    b1 = slope(corr_coeff(X, y), std_dev(X), std_dev(y))[0]
    b0 = y_intercept(b1, mean(X), mean(y))[0]
    return b0, b1

def estimate(e_X):
    return b0 + b1*e_X

def equation():
    return 'y=' + str(b0) + ('+' if b1 >= 0 else '') + str(b1) + 'x'

def plot(eq):
    plt.title(eq)
    plt.xlabel('INDEPENDANT')
    plt.ylabel('DEPENDANT')
    plt.scatter(X, y, color='red')
    plt.plot(X, [estimate(e) for e in X], color='blue')
    plt.show()

b0, b1 = equation_coeffs(X, y)

plot(equation())
