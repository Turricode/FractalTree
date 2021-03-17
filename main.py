import math
import random
import pygame

GR = 1.618

ANGLE = math.pi / 2
ROTATION = math.pi / 4
LEN_MULTIPLIER = 1 / GR

MAX_ANGLE_MODIFIER = 0

BACKGROUND_COLOR = (220, 220, 220)
BRANCH_COLOR = (14, 14, 14)

FIRST_POS = (300, 800)
LEN_INIT = 220

ITERATION_COUNT = 13

window = pygame.display.set_mode((600, 800))
running = True

lines = []

def branch(n, spos, len, angle):
    if n == 0:
        return 0

    angle_distortion = random.uniform(-MAX_ANGLE_MODIFIER, MAX_ANGLE_MODIFIER)

    epos1 = (spos[0] - len * math.cos(angle + angle_distortion), spos[1] - len * math.sin(angle + angle_distortion))
    epos2 = (spos[0] - len * math.cos(angle + angle_distortion), spos[1] - len * math.sin(angle + angle_distortion))

    lines.append((spos, epos1))
    lines.append((spos, epos2))

    branch(n - 1, epos1, len * LEN_MULTIPLIER, angle + ROTATION)
    branch(n - 1, epos2, len * LEN_MULTIPLIER, angle - ROTATION)


branch(ITERATION_COUNT, FIRST_POS, LEN_INIT, ANGLE)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    window.fill(BACKGROUND_COLOR)

    for line in lines:
        pygame.draw.aaline(window, BRANCH_COLOR, line[0], line[1])

    pygame.display.flip()
