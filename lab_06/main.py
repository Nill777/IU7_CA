from data_func import *
from integration import integrate_region, integrate_simpson, integrate_gauss, get_legendre_polynomial_roots
from derivative import *
import numpy as np
from tabulate import tabulate

21pi/8
result_eta1= 8.24668
EPS = 0.000001
# task №1
def table_fn(x: list, y: list, z: list, x_: float, y_: float, use_eta=True):
    x_ind = list(x).index(x_)
    y_ind = list(y).index(y_)
    if use_eta:
        eta = np.array([[np.log(i) for i in zi] for zi in z])
    result = eta[y_ind][x_ind] if use_eta else z[y_ind][x_ind]
    return result

def f(x, y):
    # return -x**2 - y**2 + 10
    return x**2 + y**2

def region(x: float, y: float):
    return x >= 0 and y >= 0 and (x + y) <= 1
def region1(x: float, y: float):
    return x >= 0 and x<=1 and y >= 0 and y <=1 and y >= x and x >= y**2
def region2(x: float, y: float):
    return x**2 + y**2 >= 1 and x**2 + y**2 <= 4

print(get_legendre_polynomial_roots(30))
print("-------------task_01-------------")
x, y, z = read_data('./data/data_0.txt')

points = [(x_, y_) for y_ in y for x_ in x if region(x_, y_)]
points_dict_eta = dict(zip(points, [table_fn(x, y, z, *p) for p in points]))
points_dict = dict(zip(points, [table_fn(x, y, z, *p, use_eta=False) for p in points]))
result_eta = integrate_region(integrate_simpson, integrate_gauss, points_dict_eta)
result = integrate_region(integrate_simpson, integrate_gauss, points_dict, use_eta=False)
print("Calc with η:             ", result_eta)
print("Calc without η:          ", result)

x, y, z = gen_data(f, 1, 2, 0.01, 1, 2, 0.01)

points = [(x_, y_) for y_ in y for x_ in x if region2(x_, y_)]
points_dict_eta = dict(zip(points, [table_fn(x, y, z, *p) for p in points]))
points_dict = dict(zip(points, [table_fn(x, y, z, *p, use_eta=False) for p in points]))
result_eta = integrate_region(integrate_simpson, integrate_gauss, points_dict_eta)
result = integrate_region(integrate_simpson, integrate_gauss, points_dict, use_eta=False)
print("Calc with η(gen data)    ", result_eta_1)
print("Calc without η(gen data) ", result_1)
# task №1

# task №2
print("\n-------------task_02-------------")
x = [1, 2, 3, 4, 5, 6]
y = [0.571, 0.889, 1.091, 1.231, 1.333, 1.412]
# односторонняя разностная производная
left = [get_left_derivative(y[i], y[i + 1]) for i in range(len(y) - 1)] + [None]
# центральная разностная производная
center = [None] + [get_center_derivative(y[i - 1], y[i + 1]) for i in range(1, len(y) - 1)] + [None]

# 2-я формула Рунге с использованием односторонней производной
runge = [None] + [None] + [second_Runge_formula(
    y[i - 2], y[i-1], y[i + 1], y[i+2]) for i in range(2, len(y) - 2)] + [None]+ [None]
# введены выравнивающие переменные
align_vars = [get_alignment_variables_derivative(
    y[i], y[i+1], x[i], x[i+1]) for i in range(len(y) - 1)] + [None]
# вторую разностную производную
second = [None] + [get_second_derivative(y[i - 1], y[i], y[i + 1])
                 for i in range(1, len(y) - 1)] + [None]

table = np.column_stack([np.arange(len(x)), x, y, left, center, runge, align_vars, second])
headers = ["№", "x", "y", "left", "center", "runge", "align_vars", "second"]
print(tabulate(table, headers=headers, floatfmt=".6f", missingval="NaN", stralign="left"))
# task №2