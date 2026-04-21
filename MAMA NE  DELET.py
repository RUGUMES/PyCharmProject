import turtle
# --- Настройки экрана ---
t = turtle.Turtle()
t.speed(0)
t.hideturtle()
screen = turtle.Screen()
screen.bgcolor("lightblue")
screen.setup(width=800, height=700)


# =====================================================
# ПАРА 1 — СОЛНЫШКО
# =====================================================




SUN_RAY_COLOR='orange'
SUN_COLOR='yellow'
SUN_RAYS= 16
SUN_LENGTH=90
SUN_WIDTH=6
SUN_RADIUS=60
SUN_X = 300
SUN_Y = 250
SUN_CENT_X = 350
SUN_CENT_Y = 190

def sun(x,y):
    t.color(SUN_RAY_COLOR)
    t.width(SUN_WIDTH)

    for i in range(SUN_RAYS):
        t.penup()
        t.goto(SUN_X, SUN_Y)
        t.pendown()
        t.setheading(i * 22.5)
        t.forward(SUN_LENGTH)
    t.width(1)
    t.penup()
    t.goto(SUN_CENT_X - 65, SUN_CENT_Y)
    t.pendown()
    t.color(SUN_COLOR)
    t.begin_fill()
    t.circle(SUN_RADIUS)
    t.end_fill()
sun(300,250)


# =====================================================
# ПАРА 2 — ОБЛАКО
# =====================================================


COLOR_CLOUD='white'
coords = [
    (100, 280, 40),
    (70, 290, 30),
    (130, 290, 30),
    (50, 270, 25),
    (150, 270, 25),
    (100, 260, 35)
]
def cloud(x,y):
    t.color(COLOR_CLOUD)

    for circle_x, circle_y, radius in coords:
        t.penup()
        t.goto(circle_x + x, y+circle_y  - radius)
        t.pendown()
        t.begin_fill()
        t.circle(radius)
        t.end_fill()

cloud(0,0)
cloud(-300,-50)
cloud(-150,-100)

# =====================================================
# ПАРА 3 — ЦВЕТОК
# =====================================================


STEAM_COLOR = 'darkgreen'
STEAM_WIDTH = 4
CENTER_COLOR = "yellow"
PETAL_COLOR = "pink"
STEAM_LENGTH = 120
PENTAL_COUNT= 8
PENTAL_RADIUS = 30
CENTER_RADIUS = 20

def flour(x,y,color,xcolor):
    t.penup()
    t.goto(x,y)
    t.setheading(90)
    t.pendown()

    t.color(STEAM_COLOR)
    t.width(STEAM_WIDTH)
    t.forward(STEAM_LENGTH)

    t.color(color)
    t.width(1)
    center_y = y + STEAM_LENGTH - 20
    for i in range(PENTAL_COUNT):
        t.penup()
        t.goto(x,center_y)
        t.pendown()
        t.setheading(i*(360/PENTAL_COUNT))

        t.begin_fill()
        t.circle(PENTAL_RADIUS,180)
        t.circle(PENTAL_RADIUS,180)
        t.end_fill()


    t.penup()
    t.goto(x,center_y - CENTER_RADIUS)
    t.setheading(0)
    t.pendown()
    t.color(xcolor)
    t.begin_fill()
    t.circle(CENTER_RADIUS)
    t.end_fill()
flour(0,-300,"yellow","pink")
flour(200,-300,"green","pink")
flour(-200,-300,"pink","yellow")
# =====================================================
# ПАРА 3 — ТРАВА
# =====================================================


GRASS_COLOR = "green"
BLADE_COUNT = 24
BLADE_HEIGHT = 70
START_X = -300
START_Y = -300
COUNT = 25

def grass(x,y):
    t.color(GRASS_COLOR)

    for i in range(BLADE_COUNT):
        t.penup()
        t.goto(START_X + i * COUNT, START_Y)
        t.pendown()
        d = 1 if i % 2 == 0 else -1
        t.setheading(75 + (i % 5) * 10)
        t.width(3 - (i % 2))
        n = BLADE_HEIGHT + (i % 30)
        for j in range(int(n / 10)):
            t.forward(10)
            t.left(5 * d)
        t.width(1)
grass(-300,-300)


# =====================================================
# ПАРА 4 — СЕРДЕЧКО
# =====================================================


HEART_COLOR = 'red'
HEART_SIZE = 62
HEART_RADIUS = 35

def heart(x,y):

    t.penup()
    t.goto(-300, 50)
    t.pendown()
    t.color(HEART_COLOR)
    t.begin_fill()
    t.setheading(140)
    t.forward(HEART_SIZE)
    t.circle(-HEART_RADIUS,200)
    t.setheading(60)
    t.circle(-HEART_RADIUS, 200)
    t.forward(HEART_SIZE)
    t.end_fill()
heart(-300,50)

# =====================================================
# НАДПИСЬ
# =====================================================


MANI_FONT_SIZE = 36
SUB_TEXT = 20
MIN_TEXT = 14
COLOR_MAIN_FONT = "purple"
COLOR_SUB_TEXT = "deeppink"
COLOR_MIN_TEXT = "blue"

def text(x,y):

    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color(COLOR_MAIN_FONT)
    t.write("С 8 Марта!", align="center", font=("Arial", MANI_FONT_SIZE, "bold"))
    t.penup()
    t.goto(x, y - 24)
    t.pendown()
    t.color(COLOR_SUB_TEXT)
    t.write("Дорогие женщины!", align="center", font=("Arial", SUB_TEXT, "italic"))
    t.penup()
    t.goto(x, y - 56)
    t.pendown()
    t.color(COLOR_MIN_TEXT)
    t.write("Пусть каждый день будет ярким!", align="center", font=("Arial", MIN_TEXT, "normal"))
text(0,50)

turtle.done()