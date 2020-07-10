import pandas as pd

dataset = pd.read_csv('data.csv')
x = dataset.iloc[:, :-1].values
y = dataset.iloc[:, -1].values

def mean(d): return sum(d)/len(d)

def std_dev(d):
    d_mean = mean(d)
    numerator = 0
    for e in d:
        numerator += (e-d_mean)**2
    return (numerator/(len(d)-1))**(1/2)

def corr_coeff(x, y):
    n = len(x)
    xy = []
    for i in range(n):
        xy.append(x[i]*y[i])
    x_sq = [e**2 for e in x]
    y_sq = [e**2 for e in y]
    numerator = n*sum(xy)-sum(x)*sum(y)
    denominator = ((n*sum(x_sq)-sum(x)**2)*(n*sum(y_sq)-sum(y)**2))**(1/2)
    return numerator/denominator

def slope(r, std_dev_x, std_dev_y): return r*(std_dev_y/std_dev_x)

def y_intercept(slope, x_mean, y_mean): return y_mean-(slope*x_mean)

def equation_coeffs(x, y):
    x_mean = mean(x)
    y_mean = mean(y)
    b1 = slope(corr_coeff(x, y), std_dev(x), std_dev(y))[0]
    b0 = y_intercept(b1, mean(x), mean(y))[0]
    return b0, b1

def estimate(e_x):
    return b0 + b1*e_x

def equation():
    return 'y = ' + str(b0) + ' + ' + str(b1) + 'x'

b0, b1 = equation_coeffs(x, y)

print('The equation of the line of best fit for the given data is', equation())
print('A student with GPA 4.5 can be estimated to obtain an SAT score of', int(estimate(4.5)))
