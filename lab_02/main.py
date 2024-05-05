import numpy as np
from Spline import *
from newton import *
from table import *
from draw import *

n = 3
file_name = "/home/andrey/SEM_04/CA/labs/lab_02/data/data_3.txt"
mat = read_table(file_name)

if n >= len(mat):
    print("Ньютон 3-й степени нельзя посчитать степени",
          n, ", так как точек всего", len(mat))
    exit()
print_table(mat)

user_x = float(input("Введите x: "))
mat_x = [p[0] for p in mat]
mat_y = [p[1] for p in mat]

start = deriative(mat, min(mat_x))
end = deriative(mat, max(mat_x))

print("Ньютон 3-й степени:          ", newton(mat, 3, user_x))
print("Cплайн 0 и 0:                ", Spline(mat, 0, 0).approximate(user_x))
print("Cплайн P''(x0) и 0:          ", Spline(mat, start, 0).approximate(user_x))
print("Cплайн P''(x0) и P''(xn):    ", Spline(mat, start, end).approximate(user_x))

#draw
# print(mat_x)
# print(mat_y)
dots_count = int(len(mat_x)) * 100
x_values = np.linspace(mat_x[0], mat_x[-1], dots_count)
y_values = [[], [], [], []]

for xi in x_values:
    y_values[0].append(newton(mat, 3, xi))
    y_values[1].append(Spline(mat, 0, 0).approximate(xi))
    y_values[2].append(Spline(mat, start, 0).approximate(xi))
    y_values[3].append(Spline(mat, start, end).approximate(xi))

# print(x_values)
# print(y_values)
draw(x_values, y_values)
