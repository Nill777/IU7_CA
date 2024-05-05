from matplotlib import pyplot as plt

def draw(x_values, y_values):
    plt.plot(x_values, y_values[0], ':', color='blue', label="Newton")
    plt.plot(x_values, y_values[1], ':', color='red', label="Spline 0 0")
    plt.plot(x_values, y_values[2], ':', color='#fff314', label="Spline P''(x0) 0")
    plt.plot(x_values, y_values[3], ':', color='#b734eb', label="Spline P''(x0)  P''(xn)")
    plt.legend()
    plt.show()
    