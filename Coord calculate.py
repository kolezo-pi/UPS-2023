from math import sin, cos, radians

delta = radians(25) # Угол поворота - 25 градусов
phi = radians(90)   # Угол в начальном положении - 90 градусов (вверх, вдоль оси ординат)
m = 5               # Длина движения

x0 = 0      # Предыдущая координата x
y0 = 0      # Прудыдущая координата y

x_max = 0  # Максимальная координата x
y_max = 0  # Максимальная координата y
x_min = 0  # Минимальная координата x
y_min = 0  # Минимальная координата y

print("Координаты вершин:")
print("------------------")
for i in range(36):
    print(round(x0, 3), round(y0, 3))

    phi -= delta            # Поворот вправо на 25 градусов

    x1 = x0 + m*cos(phi)    # Вычисление текущей координаты по x
    y1 = y0 + m*sin(phi)    # Вычисление текущей координаты по y

    phi -= delta            # Поворот вправо на 25 градусов

    # Вычисление максимальной и минимальной координаты x и y |
    #------------------
    if x1 > x_max: # |
        x_max = x1 # |
    if y1 > y_max: # |
        y_max = y1 # |
                    # |
    if x1 < x_min: # |
        x_min = x1 # |
    if y1 < y_min: # |
        y_min = y1 # |
    #------------------

    x0 = x1
    y0 = y1
print(round(x0, 3), round(y0, 3))
print("------------------")

print(f"X max: {round(x_max, 5)}, Y max: {round(y_max, 5)}")
print(f"X min: {round(x_min, 5)}, Y min: {round(y_min, 5)}")
print(f"Square_x^2: {x_max**2}")
print(f"Square_x*y: {(x_max-x_min)*(y_max-y_min)}")
