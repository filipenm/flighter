import pygame
import random
import math

pygame.init()

display_width = 950
display_height = 600

white = (255, 255, 255)
grey = (200, 200, 200)
light_grey = (230, 230, 230)
black = (50, 50, 50)
red = (229, 57, 90)
dark_red = (202, 51, 80)
green = (188, 213, 128)
dark_green = (150, 172, 98)
yellow = (255, 199, 48)
dark_yellow = (232, 187, 66)
blue = (38, 207, 255)
dark_blue = (37, 170, 226)

gameDisplay = pygame.display.set_mode((display_width, display_height))


bgImg1 = pygame.image.load('view1.jpg')
bgImg_scaled1 = pygame.transform.scale(bgImg1, (800, 600))

bgImg2 = pygame.image.load('view2.jpg')
bgImg_scaled2 = pygame.transform.scale(bgImg2, (800, 600))

bgImg3 = pygame.image.load('view4.jpg')
bgImg_scaled3 = pygame.transform.scale(bgImg3, (800, 600))

bgImg_scaled = random.choice((bgImg_scaled1,bgImg_scaled2,bgImg_scaled3))

mmImg = pygame.image.load('main_menu.png')
mmImg_scaled = pygame.transform.scale(mmImg, (950, 600))

manImg = pygame.image.load('instructions.png')
manImg_scaled = pygame.transform.scale(manImg, (950, 600))

planeImg = pygame.image.load('plane.png')
pvoImg = pygame.image.load('pvo1.png')
pvoImg_scaled = pygame.transform.scale(pvoImg, (20, 20))
tankImg = pygame.image.load('tank.png')
tankImg_scaled = pygame.transform.scale(tankImg, (20, 20))


class Target:
    def __init__(self, pos=(0, 0), size=(0, 0)):
        self.x = pos[0]
        self.y = pos[1]
        self.w = size[0]
        self.h = size[1]
        self.bg = bg
        self.rect = self._get_rect()

    def _get_rect(self):
        rect = self.surf.get_rect()
        rect.center = ((self.x + (self.w / 2)), (self.y + (self.h / 2)))
        return rect

    def draw(self, screen):
        pygame.draw.rect(screen, self.bg, (self.x, self.y, self.w, self.h))
        screen.blit(self.surf, self.rect)


targets = []

pygame.display.set_caption('YOU MUST TRAIN!')

font = pygame.font.SysFont("calibri.ttf", 30)
font_small = pygame.font.SysFont("calibri.ttf", 20)

plane_x = random.randrange(10, 720)
plane_y = random.randrange(5, 480)

clock = pygame.time.Clock()


def main_menu(x, y):
    gameDisplay.blit(mmImg_scaled, (x, y))


def instructions(x, y):
    gameDisplay.blit(manImg_scaled, (x, y))

def change_bg(bg):
    bx = choice([True, False])
    by = choice([True, False])

    if bx == by:
        bx, by = True, True
    return pygame.transform.flip(bg, bx, by)

def new_bg():
    bgx = random.choice([True, False])
    bgy = random.choice([True, False])

    global bgImg_scaled
    global planeImg
    planeImg = random.choice((planeImg, pvoImg_scaled, tankImg_scaled))
    bgImg_scaled = random.choice((bgImg_scaled1, bgImg_scaled2, bgImg_scaled3))
    bgImg_scaled = pygame.transform.flip(bgImg_scaled, bgx, bgy)


def bg(x, y):
    gameDisplay.blit(bgImg_scaled, (x, y))


def plane(x, y):
    gameDisplay.blit(planeImg, (x, y))

def new_level():
    new_bg()

    global plane_x, plane_y

    plane_x = random.randrange(20, 785)
    plane_y = random.randrange(10, 600)


def time(sec, mints):
    font = pygame.font.SysFont("calibri.ttf", 30)
    displaytext = "%s:%s" % (mints, sec)
    text = font.render("Time : " + str(displaytext), True, black)
    gameDisplay.blit(text, (820, 80))


def time_seg(sec, mints):
    font = pygame.font.SysFont("calibri.ttf", 30)
    displaytext = "%s:%s" % (mints, sec)
    text = font.render("Segm : " + str(displaytext), True, black)
    gameDisplay.blit(text, (820, 110))


def text_objects(text, font, color):
    textSurface = font.render(text, True, color)
    return textSurface, textSurface.get_rect()


def scoreboard(x, y, w, h, color):
    pygame.draw.rect(gameDisplay, color, [x, y, w, h])


def score(count):
    font = pygame.font.SysFont("calibri.ttf", 30)
    text = font.render("Score : " + str(count), True, black)
    gameDisplay.blit(text, (820, 20))


def misses(count):
    font = pygame.font.SysFont("calibri.ttf", 30)
    text = font.render("Misses : " + str(count), True, black)
    gameDisplay.blit(text, (820, 50))


def start_button(x, y, w, h):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    pygame.draw.rect(gameDisplay, dark_green, [x, y, w, h])
    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, green, [x, y, w, h])
        if click[0] == 1:
            game_loop()

    textSurf, textRect = text_objects("Start", font, black)
    textRect.center = (x + (w / 2), y + (h / 2))
    gameDisplay.blit(textSurf, textRect)


def back_button(x, y, w, h):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    pygame.draw.rect(gameDisplay, dark_blue, [x, y, w, h])
    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, blue, [x, y, w, h])
        if click[0] == 1:
            game_main()

    textSurf, textRect = text_objects("Back", font, black)
    textRect.center = (x + (w / 2), y + (h / 2))
    gameDisplay.blit(textSurf, textRect)


def instruction():
    gameExit = False

    while not gameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        instructions(0, 0)
        back_button(270, 400, 80, 60)

        pygame.display.update()


def instruction_button(x, y, w, h):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    pygame.draw.rect(gameDisplay, dark_yellow, [x, y, w, h])
    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, yellow, [x, y, w, h])
        if click[0] == 1:
            instruction()

    textSurf, textRect = text_objects("Instructions", font_small, black)
    textRect.center = (x + (w / 2), y + (h / 2))
    gameDisplay.blit(textSurf, textRect)


def quit_button(x, y, w, h):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    pygame.draw.rect(gameDisplay, dark_red, [x, y, w, h])
    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, red, [x, y, w, h])
        if click[0] == 1:
            pygame.quit()
            quit()

    textSurf, textRect = text_objects("Quit", font, black)
    textRect.center = (x + (w / 2), y + (h / 2))
    gameDisplay.blit(textSurf, textRect)


def game_main():
    gameExit = False

    while not gameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        main_menu(0, 0)
        start_button(200, 510, 80, 60)
        instruction_button(425, 525, 80, 60)
        quit_button(650, 510, 80, 60)

        pygame.display.update()


def game_loop():
    score_c = 0
    misses_c = 0
    timer_s = 0
    timer_m = 0
    timer_seg = 0
    timer_m_seg = 0

    plane_w = 20
    plane_h = 15

    gameExit = False

    while not gameExit:
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        scoreboard(800, 0, 150, display_height, grey)
        score(score_c)
        misses(misses_c)

        seconds = clock.tick() / 1000
        timer_s += seconds
        timer_seg += seconds

        display_timer_s = math.trunc(timer_s)
        if display_timer_s == 60:
            timer_s = 0
            timer_m += 1

        display_timer_seg = math.trunc(timer_seg)
        if display_timer_seg == 60:
            timer_s = 0
            timer_m_seg += 1

        bg(0, 0)
        plane(plane_x, plane_y)
        time(display_timer_s, timer_m)
        time_seg(display_timer_seg, timer_m_seg)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if plane_x < mouse[0] < plane_x + plane_w and plane_y < mouse[1] < plane_y + plane_h:
                if click[0] == 1:
                    score_c += 1
                    new_level()
                    timer_m_seg = 0
                    timer_seg = 0
            elif 0 < mouse[0] < 800 and 0 < mouse[1] < 600:
                if click[0] == 1:
                    misses_c += 1


game_main()
pygame.quit()
quit()
