from scipy.interpolate import CubicSpline as Spline
import numpy as np
from typing import Callable as Fn, Dict, Tuple
# from main import f
IntegrationFn = Fn[[Fn[[float], float], float, float], float]
Point = Tuple[float, float]
RegionDict = Dict[Point, float]

def get_gauss_rhs_coefs_for_system_of_equations(k):
    return 2 / (k + 1) if k % 2 == 0 else 0

# Возвращает корни полинома Лежандра степени n.
def get_legendre_polynomial_roots(n):
    # Начальные значения для рекуррентного соотношения
    p_prev = np.poly1d([1])
    p_curr = np.poly1d([1, 0])

    # Используем рекуррентное соотношение для вычисления коэффициентов
    for i in range(2, n+1):
        p_next = ((2*i - 1) * np.poly1d([1, 0]) * p_curr - (i - 1) * p_prev) / i
        p_prev = p_curr
        p_curr = p_next

    # Находим корни полинома Лежандра
    roots = p_curr.r
    return roots

def get_coefficients(legendre_polynomial_roots):
    roots = legendre_polynomial_roots
    n = len(roots)

    matrix = np.array([[t ** t_power for t in roots] for t_power in range(n)])
    values = np.array([get_gauss_rhs_coefs_for_system_of_equations(k) for k in range(n)])
    coefs = np.linalg.solve(matrix, values)

    return coefs

def integrate_gauss(func: Fn[[float], float], a: float, b: float, n=8):
    roots = get_legendre_polynomial_roots(n)
    # print(roots)
    coefs = get_coefficients(roots)

    xs = np.array(list(map(lambda t: (b - a) / 2 * t + (a + b) / 2, roots)))

    result = (b - a) / 2 * sum([coefs[i] * func(xs[i])
                                for i in range(len(roots))])

    return result

def integrate_simpson(func: Fn[[float], float], a: float, b: float, n=16):
    h = (b - a) / n
    x = np.linspace(a, b, n+1)
    y = [func(xi) for xi in x]

    summ = 0
    for i in range(1, n, 2):
        summ += y[i-1] + 4*y[i] + y[i+1]
    result = h/3 * summ
    return result
def f(x, y):
    # return -x**2 - y**2 + 10
    return x - y**2
def integrate_region(integrate_main: IntegrationFn,
                     integrate_Fs: IntegrationFn,
                     region_dict: RegionDict,
                     use_eta=True
                     ):
    xs = np.unique(list(map(lambda p: p[0], region_dict.keys())))
    ys = np.unique(list(map(lambda p: p[1], region_dict.keys())))

    def points_by_y(y): return [p for p in region_dict.keys() if p[1] == y]

    Fs = []
    Ys = []

    for k in ys:
        points = points_by_y(k)
        xs = [p[0] for p in points]
        fn = [region_dict[p] for p in points]

        if len(xs) > 1:
            spline = Spline(xs, fn)

            if use_eta:
                def func(x): return np.e ** spline(x)
            else:
                def func(x): return spline(x)

            x_min = min(xs)
            x_max = max(xs)

            Fk = integrate_Fs(func, x_min, x_max)

            Fs.append(Fk)
            Ys.append(k)

    func = Spline(Ys, Fs)

    y_min = min(Ys)
    y_max = max(Ys)

    return integrate_main(func, y_min, y_max)

