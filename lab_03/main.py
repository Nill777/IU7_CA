from table import *
from interpolation_3D import *

def choose_alg():
    print("Выберите алгоритм:\n1) Ньютон\n2) Сплайн")
    type = int(input("Введите номер алгоритма: "))
    return algorithms[type - 1]

algorithms = ["newton", "spline"]
algo_list = ['', '', '']

def f(x, y, z):
    # return 1/(x+y) -z                 # гиперболическую функцию точнее интерполировать ньютоном
    return np.exp(2*x-y) *z**3          # экспоненциальную функцию точнее интерполировать сплайнами
x_start, x_end, x_counts = -5, 5, 20
y_start, y_end, y_counts = -3, 4, 50
z_start, z_end, z_counts = -1, 2, 30
data = generateData(f, x_start, x_end, x_counts,
                      y_start, y_end, y_counts,
                      z_start, z_end, z_counts)
newton_ns = [3, 2, 5]
# data = read_data("/home/andrey/SEM_04/CA/lab_03/data/data_1.txt")
print_data(data)

point = [-1.152, 1.1412, 1.43]


print("Выберите алгоритм:\n1) Ньютон\n2) Сплайн\n3) Комбинация")
c = int(input("Введите номер алгоритма: "))
if c == 1:
    algo_list = [algorithms[0] for _ in range(3)]
elif c == 2:
    algo_list = [algorithms[1] for _ in range(3)]
else:
    for i in range(3):
        algo_list[i] = choose_alg()

print("\nf(x, y, z) = ", interpolation_3D(data, point, algo_list, newton_ns))
