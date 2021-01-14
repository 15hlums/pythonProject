# this is the code to create Jeff :)

import pygame

pygame.init()

DISPLAYSURFACE = pygame.display.set_mode([800, 600])

FPSCLOCK = pygame.time.Clock()

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()

    # this is the sky, Jeff's favourite colour
    DISPLAYSURFACE.fill((0,191,255))

    # this is the grass Jeff likes to stand on and eat
    pygame.draw.rect(DISPLAYSURFACE, (34,139,34), (0, 400, 800, 200), 0)

    # these are his legs, he uses them to run
    pygame.draw.rect(DISPLAYSURFACE, (255, 215, 0), (275, 410, 30, 125), 0)
    pygame.draw.rect(DISPLAYSURFACE, (255, 215, 0), (375, 410, 30, 125), 0)
    pygame.draw.rect(DISPLAYSURFACE, (255, 215, 0), (325, 350, 30, 150), 0)
    pygame.draw.rect(DISPLAYSURFACE, (255, 215, 0), (425, 350, 30, 150), 0)

    # this is his body, hes doesnt like body shaming
    pygame.draw.rect(DISPLAYSURFACE, (255, 215, 0), (255, 300, 225, 125), 0)
    pygame.draw.circle(DISPLAYSURFACE, (255, 215, 0),(265, 375),50)

    # this is his neck, with only 7 bones in it
    pygame.draw.rect(DISPLAYSURFACE, (255, 215, 0), (225, 100, 50, 250), 0)

    # this is his head, he uses it to think
    pygame.draw.ellipse(DISPLAYSURFACE, (255, 215, 0), (125, 50, 150, 100), 0)

    # these are his eyes, he likes seeing stuff
    pygame.draw.circle(DISPLAYSURFACE, (0, 0, 0), (200, 90), 5)
    pygame.draw.circle(DISPLAYSURFACE, (0, 0, 0), (225, 90), 5)

    # this is his mouth, nom nom
    pygame.draw.arc(DISPLAYSURFACE, (0, 0, 0), (150, 100, 20, 20), 3, 6, 50)

    # these are his horns, or whatever you call them
    pygame.draw.rect(DISPLAYSURFACE, (255, 215, 0), (200, 10, 10, 40), 0)
    pygame.draw.rect(DISPLAYSURFACE, (255, 215, 0), (225, 10, 10, 50), 0)
    pygame.draw.circle(DISPLAYSURFACE, (218,165,32), (205, 10), 10)
    pygame.draw.circle(DISPLAYSURFACE, (218, 165, 32), (230, 10), 10)

    # this is his cape, he protecc, he attacc
    pygame.draw.rect(DISPLAYSURFACE, (255, 0, 0), (275, 225, 400, 20), 0)

    # these are his spots, because his ambition is to become a ladybird
    pygame.draw.circle(DISPLAYSURFACE, (218, 165, 32), (245, 300), 15)
    pygame.draw.circle(DISPLAYSURFACE, (218, 165, 32), (250, 250), 15)
    pygame.draw.circle(DISPLAYSURFACE, (218, 165, 32), (245, 200), 15)
    pygame.draw.circle(DISPLAYSURFACE, (218, 165, 32), (250, 150), 15)
    pygame.draw.circle(DISPLAYSURFACE, (218, 165, 32), (300, 400), 15)

    pygame.display.update()

    FPSCLOCK.tick(30)