import ctypes, pygame, pymunk
TITLE_STRING = 'Minionball'
FPS = 60

#  keeping resolution despite scaling of windows
ctypes.windll.user32.SetProcessDPIAware()

WIDTH = 1920
HEIGHT = 1080

#  minionball config

BG_COLOR = (16, 32, 45)
MULTI_HEIGHT = int(HEIGHT / 19)
MULTI_COLLISION = HEIGHT - (MULTI_HEIGHT * 2)

SCORE_RECT = int(WIDTH / 16)
OBSTACLE_COLOR = "White"
OBSTACLE_RAD = int(WIDTH / 240)
OBSTACLE_PAD = int(HEIGHT / 19)

OBSTACLE_START = (int((WIDTH /2) - OBSTACLE_PAD), int((HEIGHT - (HEIGHT *.9))))
segmentA_2 = OBSTACLE_START

BALL_RAD = 16

# Score Dictionary
multipliers = {
    "1000":0,
    "130":0,
    "26":
    "9"
}


