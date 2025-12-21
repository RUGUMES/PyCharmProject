import math
def calculate_rectangle_area(width, height):
    return width * height

def calculate_circle_area(radius):
    return math.pi * radius * radius

print("Площадь прямоугольника")
w, h = map(float, input("введите ширину и высоту прямоугольник: ").split())
rect_area = calculate_rectangle_area(w, h)
print(f"Площадь прямоугольника: {rect_area:.2f}")

r = float(input("Введите радиус круга: "))
circle_area = calculate_circle_area(r)
print(f"Площадь круга: {circle_area:.2f}")