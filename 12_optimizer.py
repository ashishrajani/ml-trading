import  pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import scipy.optimize as spo


def f(x):
    y = (x - 1.5)**2 + 0.5
    print('x = {}, y = {}'.format(x, y))
    return y


def find_min():
    x_init = np.array(2.0)
    min_res = spo.minimize(f, x_init, method='SLSQP', options={'disp': True})
    print("Minima found at: ")
    print('x = {}, y = {}'.format(min_res.x, min_res.fun))

    x_plot = np.linspace(0.5, 2.5, 21)
    y_plot = f(x_plot)
    plt.plot(x_plot, y_plot)
    plt.plot(min_res.x, min_res.fun, 'ro')
    plt.title("Minima of an objective function")
    plt.show()


def error(line, data):
    return np.sum((data[:,1] - (line[0] * data[:, 0] + line[1])) ** 2)


def fit_line(data, error_func):
    l = np.float32([0, np.mean(data[:, 1])])

    x_ends = np.float32([-5, 5])
    plt.plot(x_ends, l[0] * x_ends + l[1], 'm--', linewidth=2.0)

    result = spo.minimize(error_func, l, args=(data,), method='SLSQP', options={'disp': True})
    return result.x


def find_line():
    line_orig = np.float32([4, 2])
    print('Original Line C0 = {}, C1 = {}'.format(line_orig[0], line_orig[1]))
    x_orig = np.linspace(0, 10, 21)
    y_orig = line_orig[0] * x_orig + line_orig[1]
    plt.plot(x_orig, y_orig, 'b--', linewidth=2.0)

    noise_sigma = 3.0
    noise = np.random.normal(0, noise_sigma, y_orig.shape)
    data = np.asarray([x_orig, y_orig + noise]).T
    plt.plot(data[:, 0], data[:, 1], 'go')

    l_fit = fit_line(data, error)
    print("Fitted line: C0 = {}, C1 = {}".format(l_fit[0], l_fit[1]))
    plt.plot(data[:, 0], l_fit[0] * data[:, 0] + l_fit[1], 'r--', linewidth=2.0)

    plt.legend(['Original line', 'Data points', 'Initial guess', 'Fitted Line'])
    plt.show()


def error_poly(C, data):
    return np.sum((data[:,1] - np.polyval(C, data[:,0])) ** 2)


def fit_poly(data, error_func, degree=3):
    Cguess = np.poly1d(np.ones(degree + 1, dtype=np.float32))
    x = np.linspace(-5, 5, 21)
    plt.plot(x, np.polyval(Cguess, x), 'm--', linewidth=2.0)
    result = spo.minimize(error_poly, Cguess, args=(data,), method='SLSQP', options={'disp': True})
    return np.poly1d(result.x)


def find_poly():
    poly_orig = np.float32([4, 2, 5, 1])
    print('Original Line C0 = {}, C1 = {}, C2 = {}, C3 = {}'.format(poly_orig[0], poly_orig[1], poly_orig[2], poly_orig[3]))
    x_orig = np.linspace(-5, 5, 21)
    y_orig = np.polyval(poly_orig, x_orig)
    plt.plot(x_orig, y_orig, 'b--', linewidth=2.0)

    noise_sigma = 70.0
    noise = np.random.normal(0, noise_sigma, y_orig.shape)
    data = np.asarray([x_orig, y_orig + noise]).T
    plt.plot(data[:, 0], data[:, 1], 'go')

    ploy_fit = fit_poly(data, error)
    print("Fitted line: C0 = {}, C1 = {}, C2 = {}, C3 = {}".format(ploy_fit[0], ploy_fit[1], ploy_fit[2], ploy_fit[3]))
    plt.plot(data[:, 0], np.polyval(ploy_fit, x_orig), 'r--', linewidth=2.0)

    plt.legend(['Original line', 'Data points', 'Initial guess', 'Fitted Line'])
    plt.show()


if __name__ == "__main__":
    # find_min()
    # find_line()
    find_poly()