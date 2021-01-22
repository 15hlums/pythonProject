# this is the code to create Jeff :)

import pygame

pygame.init()

DISPLAYSURFACE = pygame.display.set_mode([800, 600])

FPSCLOCK = pygame.time.Clock()

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()

    # this is the sky
    DISPLAYSURFACE.fill((0,191,255))

    # this is the grass
    pygame.draw.rect(DISPLAYSURFACE, (34,139,34), (0, 400, 800, 200), 0)

    # these are his legs
    pygame.draw.rect(DISPLAYSURFACE, (255, 215, 0), (275, 410, 30, 125), 0)
    pygame.draw.rect(DISPLAYSURFACE, (255, 215, 0), (375, 410, 30, 125), 0)
    pygame.draw.rect(DISPLAYSURFACE, (255, 215, 0), (325, 350, 30, 150), 0)
    pygame.draw.rect(DISPLAYSURFACE, (255, 215, 0), (425, 350, 30, 150), 0)

    # this is his body
    pygame.draw.rect(DISPLAYSURFACE, (255, 215, 0), (255, 300, 225, 125), 0)
    pygame.draw.circle(DISPLAYSURFACE, (255, 215, 0),(265, 375),50)

    # this is his neck
    pygame.draw.rect(DISPLAYSURFACE, (255, 215, 0), (225, 100, 50, 250), 0)

    # this is his head
    pygame.draw.ellipse(DISPLAYSURFACE, (255, 215, 0), (125, 50, 150, 100), 0)

    # these are his eyes
    pygame.draw.circle(DISPLAYSURFACE, (0, 0, 0), (200, 90), 5)
    pygame.draw.circle(DISPLAYSURFACE, (0, 0, 0), (225, 90), 5)

    # this is his mouth
    pygame.draw.arc(DISPLAYSURFACE, (0, 0, 0), (150, 100, 20, 20), 3, 6, 50)

    # these are his horns
    pygame.draw.rect(DISPLAYSURFACE, (255, 215, 0), (200, 10, 10, 40), 0)
    pygame.draw.rect(DISPLAYSURFACE, (255, 215, 0), (225, 10, 10, 50), 0)
    pygame.draw.circle(DISPLAYSURFACE, (218,165,32), (205, 10), 10)
    pygame.draw.circle(DISPLAYSURFACE, (218, 165, 32), (230, 10), 10)

    # this is hair
    for x in range(100, 299, 2):
        pygame.draw.rect(DISPLAYSURFACE, (139, 69, 19), (275, x, 15, 1), 0)

    # these are his spots
    pygame.draw.circle(DISPLAYSURFACE, (218, 165, 32), (245, 300), 15)
    pygame.draw.circle(DISPLAYSURFACE, (218, 165, 32), (250, 250), 15)
    pygame.draw.circle(DISPLAYSURFACE, (218, 165, 32), (245, 200), 15)
    pygame.draw.circle(DISPLAYSURFACE, (218, 165, 32), (250, 150), 15)
    pygame.draw.circle(DISPLAYSURFACE, (218, 165, 32), (300, 400), 15)
    pygame.draw.circle(DISPLAYSURFACE, (218, 165, 32), (240, 380), 15)
    pygame.draw.circle(DISPLAYSURFACE, (218, 165, 32), (280, 340), 15)
    pygame.draw.circle(DISPLAYSURFACE, (218, 165, 32), (250, 300), 15)
    pygame.draw.circle(DISPLAYSURFACE, (218, 165, 32), (335, 325), 15)
    pygame.draw.circle(DISPLAYSURFACE, (218, 165, 32), (350, 375), 15)
    pygame.draw.circle(DISPLAYSURFACE, (218, 165, 32), (400, 400), 15)
    pygame.draw.circle(DISPLAYSURFACE, (218, 165, 32), (387, 340), 15)
    pygame.draw.circle(DISPLAYSURFACE, (218, 165, 32), (440, 325), 15)
    pygame.draw.circle(DISPLAYSURFACE, (218, 165, 32), (445, 375), 15)
    pygame.draw.circle(DISPLAYSURFACE, (218, 165, 32), (290, 500), 15)
    pygame.draw.circle(DISPLAYSURFACE, (218, 165, 32), (290, 450), 15)
    pygame.draw.circle(DISPLAYSURFACE, (218, 165, 32), (340, 430), 15)
    pygame.draw.circle(DISPLAYSURFACE, (218, 165, 32), (340, 480), 15)
    pygame.draw.circle(DISPLAYSURFACE, (218, 165, 32), (390, 445), 15)
    pygame.draw.circle(DISPLAYSURFACE, (218, 165, 32), (390, 495), 15)
    pygame.draw.circle(DISPLAYSURFACE, (218, 165, 32), (440, 440), 15)
    pygame.draw.circle(DISPLAYSURFACE, (218, 165, 32), (440, 480), 15)

    # this is his tail
    pygame.draw.rect(DISPLAYSURFACE, (255, 215, 0), (490, 300, 10, 100), 0)
    pygame.draw.rect(DISPLAYSURFACE, (255, 215, 0), (475, 300, 20, 10), 0)
    for x in range (490, 501, 2):
        pygame.draw.rect(DISPLAYSURFACE, (139,69,19), (x, 400, 1, 15), 0)

    # this is a tree
    pygame.draw.rect(DISPLAYSURFACE, (139,69,19), (600, 250, 50, 300), 0)
    pygame.draw.circle(DISPLAYSURFACE, (85,107,47), (600, 225), 50)
    pygame.draw.circle(DISPLAYSURFACE, (85,107,47), (650, 200), 50)
    pygame.draw.circle(DISPLAYSURFACE, (85,107,47), (550, 250), 50)
    pygame.draw.circle(DISPLAYSURFACE, (85,107,47), (575, 190), 50)
    pygame.draw.circle(DISPLAYSURFACE, (85,107,47), (600, 170), 50)
    pygame.draw.circle(DISPLAYSURFACE, (85,107,47), (620, 150), 50)
    pygame.draw.circle(DISPLAYSURFACE, (85,107,47), (650, 155), 50)
    pygame.draw.circle(DISPLAYSURFACE, (85,107,47), (540, 230), 50)
    pygame.draw.circle(DISPLAYSURFACE, (85,107,47), (620, 225), 50)
    pygame.draw.circle(DISPLAYSURFACE, (85,107,47), (650, 240), 50)
    pygame.draw.circle(DISPLAYSURFACE, (85,107,47), (700, 225), 50)
    pygame.draw.circle(DISPLAYSURFACE, (85,107,47), (695, 200), 50)

    # these are the apples
    pygame.draw.rect(DISPLAYSURFACE, (160,82,45), (520, 210, 3, 20), 0)
    pygame.draw.circle(DISPLAYSURFACE, (255,0,0), (522, 230), 10)
    pygame.draw.rect(DISPLAYSURFACE, (160,82,45), (545, 250, 3, 20), 0)
    pygame.draw.circle(DISPLAYSURFACE, (255,0,0), (547, 270), 10)
    pygame.draw.rect(DISPLAYSURFACE, (160,82,45), (575, 225, 3, 20), 0)
    pygame.draw.circle(DISPLAYSURFACE, (255,0,0), (577, 245), 10)
    pygame.draw.rect(DISPLAYSURFACE, (160,82,45), (625, 240, 3, 20), 0)
    pygame.draw.circle(DISPLAYSURFACE, (255,0,0), (627, 260), 10)
    pygame.draw.rect(DISPLAYSURFACE, (160,82,45), (666, 220, 3, 20), 0)
    pygame.draw.circle(DISPLAYSURFACE, (255,0,0), (668, 240), 10)
    pygame.draw.rect(DISPLAYSURFACE, (160,82,45), (715, 228, 3, 20), 0)
    pygame.draw.circle(DISPLAYSURFACE, (255,0,0), (717, 248), 10)

    # these are flowers
    pygame.draw.rect(DISPLAYSURFACE, (0,100,0), (100, 500, 10, 50), 0)
    pygame.draw.circle(DISPLAYSURFACE, (139,0,139), (100, 499), 10)
    pygame.draw.circle(DISPLAYSURFACE, (139,0,139), (110, 490), 10)
    pygame.draw.circle(DISPLAYSURFACE, (139,0,139), (101, 488), 10)
    pygame.draw.circle(DISPLAYSURFACE, (139,0,139), (108, 500), 10)
    pygame.draw.circle(DISPLAYSURFACE, (255,69,0), (105, 495), 2)

    pygame.draw.rect(DISPLAYSURFACE, (0,100,0), (150, 500, 10, 50), 0)
    pygame.draw.circle(DISPLAYSURFACE, (139,0,139), (150, 499), 10)
    pygame.draw.circle(DISPLAYSURFACE, (139,0,139), (160, 490), 10)
    pygame.draw.circle(DISPLAYSURFACE, (139,0,139), (151, 488), 10)
    pygame.draw.circle(DISPLAYSURFACE, (139,0,139), (158, 500), 10)
    pygame.draw.circle(DISPLAYSURFACE, (255,69,0), (155, 495), 2)

    pygame.draw.rect(DISPLAYSURFACE, (0,100,0), (50, 500, 10, 50), 0)
    pygame.draw.circle(DISPLAYSURFACE, (139,0,139), (50, 499), 10)
    pygame.draw.circle(DISPLAYSURFACE, (139,0,139), (60, 490), 10)
    pygame.draw.circle(DISPLAYSURFACE, (139,0,139), (51, 488), 10)
    pygame.draw.circle(DISPLAYSURFACE, (139,0,139), (58, 500), 10)
    pygame.draw.circle(DISPLAYSURFACE, (255,69,0), (55, 495), 2)

    pygame.draw.rect(DISPLAYSURFACE, (0,100,0), (200, 500, 10, 50), 0)
    pygame.draw.circle(DISPLAYSURFACE, (139,0,139), (200, 499), 10)
    pygame.draw.circle(DISPLAYSURFACE, (139,0,139), (210, 490), 10)
    pygame.draw.circle(DISPLAYSURFACE, (139,0,139), (201, 488), 10)
    pygame.draw.circle(DISPLAYSURFACE, (139,0,139), (208, 500), 10)
    pygame.draw.circle(DISPLAYSURFACE, (255,69,0), (205, 495), 2)

    # this is the sun
    pygame.draw.circle(DISPLAYSURFACE, (255,223,0), (0, 0), 85)

    pygame.display.update()

    FPSCLOCK.tick(30)