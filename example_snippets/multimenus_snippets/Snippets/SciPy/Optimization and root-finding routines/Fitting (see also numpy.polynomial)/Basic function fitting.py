def fitting_function(x, a, b, c):
    return a * np.exp(-b * x) + c
xdata = np.linspace(0, 4, 50)
ydata = fitting_function(xdata, 2.5, 1.3, 0.5) + 0.2 * np.random.normal(size=len(xdata))
optimal_parameters, estimated_covariance = optimize.curve_fit(fitting_function, xdata, ydata)
estimated_std_dev = np.sqrt(np.diag(estimated_covariance))