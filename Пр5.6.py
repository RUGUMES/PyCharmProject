import math

def calculate_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
def calculate_triangle_area(a, b, c):
    s = (a + b + c) / 2
    return math.sqrt(s * (s - a) * (s - b) * (s - c))

print("Введите координаты трех точек (A, B, C).")
x1, y1 = map(float, input("Координаты точки A (x y): ").split())
x2, y2 = map(float, input("Координаты точки B (x y): ").split())
x3, y3 = map(float, input("Координаты точки C (x y): ").split())

a = calculate_distance(x2, y2, x3, y3)
b = calculate_distance(x1, y1, x3, y3)
c = calculate_distance(x1, y1, x2, y2)
area = calculate_triangle_area(a, b, c)

print(f"Площадь треугольника: {area:.3f}")