import turtle
import random


"""
==================================================================
                              Константы
==================================================================
"""


# ---------- СОЛНЫШКО ----------

SUN_LINE_COUNT = 16
SUN_ANGLE = 22.5
SUN_CENTR_X = 300
SUN_CENTR_Y = 250
SUN_RAY_DLINNA = 90
SUN_RAY_TOLSHINA = 6
SUN_RAY_COLOR = "orange"
SUN_CIRCLE_CENTR_X = 277
SUN_CIRCLE_CENTR_Y = 195
SUN_CIRCLE_RADIUS = 60
SUN_CIRCLE_COLOR = "yellow"


# ---------- ОБЛАКИ (3 шт.) ----------

CLOUD_COLOR = "white"
CLOUD_SHMOKE = [
    (100, 280, 40),
    (70, 290, 30),
    (130, 290, 30),
    (50, 270, 25),
    (150, 270, 25),
    (100, 260, 35)
]


# ---------- ЦВЕТИКИ (общие параметры) ----------

STEBL_COLOR = "darkgreen"
STEBL_SHIRINA = 4
STEBL_LENGTH = 200
PETAL_COUNT = 8
PETAL_RADIUS = 30
CENTER_RADIUS = 20
CENTER_COLOR = "yellow"

# Параметры трёх цветков: (x_основания, y_основания, цвет_лепестков)
CVETIKI = [
    (0, -330, "pink"),       # центральный – розовый
    (-180, -350, "cyan"),    # левый – голубой
    (180, -350, "gold")      # правый – жёлтый
]


# ---------- СЕРДЕЧКИ (два симметричных) ----------

HEART_START_X_LEFT = -300
HEART_START_X_RIGHT = 300
HEART_START_Y = -36
HEART_COLOR = "red"
HEART_HEADING_LEFT = 140
HEART_HEADING_RIGHT = -140      # зеркальный угол
HEART_FORWARD = 62
HEART_CIRCLE_RADIUS = 35
HEART_CIRCLE_EXTENT = 200
HEART_SETHEADING_AFTER_LEFT = 60
HEART_SETHEADING_AFTER_RIGHT = -60


# ---------- НАДПИСИ ----------

TEXT_MAIN = "С 8 Марта!"
TEXT_MAIN_COLOR = "purple"
TEXT_MAIN_FONT = ("Arial", 36, "bold")
TEXT_MAIN_X = 0
TEXT_MAIN_Y = 30

POD_TEXT = "Дорогие женщины!"
POD_TEXT_COLOR = "deeppink"
POD_TEXT_FONT = ("Arial", 20, "italic")
POD_TEXT_X = 0
POD_TEXT_Y = 0

TEXT_EXTRA = "Пусть каждый день будет ярким!"
TEXT_EXTRA_COLOR = "blue"
TEXT_EXTRA_FONT = ("Arial", 14, "normal")
TEXT_EXTRA_X = 0
TEXT_EXTRA_Y = -27


# ---------- ТРАВКА (вся нижняя часть) ----------

GRASS_COLOR = "green"
GRASS_BLADE_COUNT = 65
GRASS_START_X = -380
GRASS_END_X = 380
GRASS_START_Y = -345
GRASS_BASE_HEIGHT = 60
GRASS_MAX_HEIGHT_VAR = 50
GRASS_ANGLE_VERTICAL = 90
GRASS_ANGLE_VAR = 25
GRASS_WIDTH_MAX = 4
GRASS_WIDTH_MIN = 1


"""
==================================================================
                              Функции
==================================================================
"""


def narisovat_sun():
    tur.color(SUN_RAY_COLOR)
    tur.width(SUN_RAY_TOLSHINA)

    for col_vo_liniy in range(SUN_LINE_COUNT):
        tur.penup()
        tur.goto(SUN_CENTR_X, SUN_CENTR_Y)
        tur.pendown()
        tur.setheading(col_vo_liniy * SUN_ANGLE)
        tur.forward(SUN_RAY_DLINNA)
    tur.width(1)
    tur.penup()
    tur.goto(SUN_CIRCLE_CENTR_X, SUN_CIRCLE_CENTR_Y)
    tur.pendown()
    tur.color(SUN_CIRCLE_COLOR)
    tur.begin_fill()
    tur.circle(SUN_CIRCLE_RADIUS)
    tur.end_fill()


def narisovat_oblako(x,y):
    tur.color(CLOUD_COLOR)
    for circle_x, circle_y, radius in CLOUD_SHMOKE:
        tur.penup()
        tur.goto(circle_x + x, y + circle_y - radius)
        tur.pendown()
        tur.begin_fill()
        tur.circle(radius)
        tur.end_fill()


def narisovat_flower_at(base_x, base_y, petal_color):
    # Стебель
    tur.color(STEBL_COLOR)
    tur.width(STEBL_SHIRINA)
    tur.penup()
    tur.goto(base_x, base_y)
    tur.pendown()
    tur.setheading(90)
    tur.forward(STEBL_LENGTH)

    # Центр цветка (верх стебля)
    center_x = base_x
    center_y = base_y + STEBL_LENGTH

    # Лепестки
    tur.width(1)
    tur.color(petal_color)
    for i in range(PETAL_COUNT):
        tur.penup()
        tur.goto(center_x, center_y)   # перемещаемся в центр
        tur.pendown()
        tur.setheading(i * (360 / PETAL_COUNT))
        tur.begin_fill()
        tur.circle(PETAL_RADIUS, 180)
        tur.circle(PETAL_RADIUS, 180)
        tur.end_fill()

    # Жёлтая серединка (рисуем ТОЧНО в том же центре)
    tur.penup()
    tur.goto(center_x, center_y)
    tur.pendown()
    tur.color(CENTER_COLOR)
    tur.begin_fill()
    tur.circle(CENTER_RADIUS)
    tur.end_fill()


def narisovat_vse_cvetiki():
    for x, y, color in CVETIKI:
        narisovat_flower_at(x, y, color)


def narisovat_heart():
    # Левое сердечко
    tur.penup()
    tur.goto(HEART_START_X_LEFT, HEART_START_Y)
    tur.pendown()
    tur.color(HEART_COLOR)
    tur.begin_fill()
    tur.setheading(HEART_HEADING_LEFT)       # 140
    tur.forward(HEART_FORWARD)
    tur.circle(-HEART_CIRCLE_RADIUS, HEART_CIRCLE_EXTENT)
    tur.setheading(HEART_SETHEADING_AFTER_LEFT)  # 60
    tur.circle(-HEART_CIRCLE_RADIUS, HEART_CIRCLE_EXTENT)
    tur.forward(HEART_FORWARD)
    tur.end_fill()

    # Правое сердечко (такое же, не зеркальное)
    tur.penup()
    tur.goto(HEART_START_X_RIGHT, HEART_START_Y)   # x = 300
    tur.pendown()
    tur.color(HEART_COLOR)
    tur.begin_fill()
    tur.setheading(HEART_HEADING_LEFT)       # 140 (тот же угол)
    tur.forward(HEART_FORWARD)
    tur.circle(-HEART_CIRCLE_RADIUS, HEART_CIRCLE_EXTENT)   # тот же минус
    tur.setheading(HEART_SETHEADING_AFTER_LEFT)  # 60
    tur.circle(-HEART_CIRCLE_RADIUS, HEART_CIRCLE_EXTENT)
    tur.forward(HEART_FORWARD)
    tur.end_fill()


def narisovat_text():
    tur.penup()
    tur.goto(TEXT_MAIN_X, TEXT_MAIN_Y)
    tur.pendown()
    tur.color(TEXT_MAIN_COLOR)
    tur.write(TEXT_MAIN, align="center", font=TEXT_MAIN_FONT)

    tur.penup()
    tur.goto(POD_TEXT_X, POD_TEXT_Y)
    tur.pendown()
    tur.color(POD_TEXT_COLOR)
    tur.write(POD_TEXT, align="center", font=POD_TEXT_FONT)

    tur.penup()
    tur.goto(TEXT_EXTRA_X, TEXT_EXTRA_Y)
    tur.pendown()
    tur.color(TEXT_EXTRA_COLOR)
    tur.write(TEXT_EXTRA, align="center", font=TEXT_EXTRA_FONT)


def narisovat_travka():
    """Рисует много травинок со случайными параметрами"""
    tur.color(GRASS_COLOR)
    for i in range(GRASS_BLADE_COUNT):
        x = random.randint(GRASS_START_X, GRASS_END_X)
        tur.penup()
        tur.goto(x, GRASS_START_Y)
        tur.pendown()
        height = GRASS_BASE_HEIGHT + random.randint(0, GRASS_MAX_HEIGHT_VAR)
        angle = GRASS_ANGLE_VERTICAL + random.randint(-GRASS_ANGLE_VAR, GRASS_ANGLE_VAR)
        tur.setheading(angle)
        thickness = random.randint(GRASS_WIDTH_MIN, GRASS_WIDTH_MAX)
        tur.width(thickness)
        direction = random.choice([-1, 1])
        steps = int(height / 8)
        for _ in range(steps):
            tur.forward(8)
            tur.left(3 * direction)
        tur.width(GRASS_WIDTH_MIN)


"""
==================================================================
                        Основная программа
==================================================================
"""

screen = turtle.Screen()
screen.bgcolor("lightblue")
screen.setup(width=800, height=700)

tur = turtle.Turtle()
tur.speed(0)
tur.hideturtle()

# Рисуем всё
narisovat_sun()
narisovat_oblako(0,0)
narisovat_oblako(-300,-50)
narisovat_oblako(-150,-100)
narisovat_vse_cvetiki()
narisovat_heart()
narisovat_text()
narisovat_travka()          # сплошная трава внизу

turtle.done()