import pygame
import random
import pygame.freetype

pygame.init()
win = pygame.display.set_mode((600,400))
pygame.display.set_caption("My first game")
img =pygame.image.load("artt.jpg")
pygame.display.set_icon(img)

walkRightLeft = [pygame.image.load('Run (2).png'), pygame.image.load('Run (3).png'), pygame.image.load('Run (4).png'), pygame.image.load('Run (5).png'), pygame.image.load('Run (6).png'), pygame.image.load('Run (7).png'), pygame.image.load('Run (8).png'), pygame.image.load('Run (9).png'), pygame.image.load('Run (10).png'),
               pygame.image.load('Run (11).png'), pygame.image.load('Run (12).png'), pygame.image.load('Run (13).png'), pygame.image.load('Run (14).png'), pygame.image.load('Run (15).png'), ]

playerJump = [pygame.image.load('Jump (9).png'), pygame.image.load('Jump (4).png')]

bg = pygame.image.load('BG.png')

bone = pygame.image.load('Bone (4).png')
tree = pygame.image.load('Tree.png')

sceleton = pygame.image.load('Skeleton.png')

playerStand = [pygame.image.load('Idle (1).png'), pygame.image.load('Idle (2).png'), pygame.image.load('Idle (3).png'), pygame.image.load('Idle (4).png'), pygame.image.load('Idle (5).png'), pygame.image.load('Idle (6).png'), pygame.image.load('Idle (7).png'), pygame.image.load('Idle (8).png'), pygame.image.load('Idle (9).png'), pygame.image.load('Idle (10).png'),
               pygame.image.load('Idle (11).png'), pygame.image.load('Idle (12).png'), pygame.image.load('Idle (13).png'), pygame.image.load('Idle (14).png'), pygame.image.load('Idle (15).png'), ]

earth = pygame.image.load('Tile (2).png')

falling = [pygame.image.load('Dead (1).png'), pygame.image.load('Dead (2).png'), pygame.image.load('Dead (3).png'), pygame.image.load('Dead (4).png'), pygame.image.load('Dead (5).png'), pygame.image.load('Dead (6).png'), pygame.image.load('Dead (7).png'), pygame.image.load('Dead (8).png'), pygame.image.load('Dead (9).png'), pygame.image.load('Dead (10).png')
                 , pygame.image.load('Dead (11).png'), pygame.image.load('Dead (12).png'), pygame.image.load('Dead (13).png'), pygame.image.load('Dead (14).png'), pygame.image.load('Dead (15).png')]

ArrowSign = pygame.image.load('ArrowSign.png')

TombStone = pygame.image.load('TombStone (1).png')
clock = pygame.time.Clock()

font = pygame.font.Font(None, 25)



x = 50
y = 300
width = 50
height = 46
speed = 5

isJump = False
JumpCount = 10

left = False
right = False
jump = False
fall = False
stand = True

frame_count = 0
frame_rate = 60
start_time = 90


snow_list =[]

for i in range(25):
    p = random.randrange(200, 300)
    d = random.randrange(0, 400)
    snow_list.append([p, d])

animcount = 0
lastMove = "right"



pygame.mixer.music.load('c26baac1db252bd.mp3')
pygame.mixer.music.play(-1)







class snaryad():
    def __init__(self, x, y, radius, color, facing):
        self.x = x
        self.y = y
        self.radius = radius
        self.facing = facing
        self. color = color
        self.vel = 8 * facing

    def draw(self, win):
        pygame.draw.circle(win, self.color, (self.x, self.y),
                           self.radius)






def drawWindow():
    global animcount
    win.blit(bg, (0, 0))
    win.blit(earth, (0, 400 - height - 15))
    win.blit(earth, (100, 400 - height - 15))
    win.blit(earth, (200, 400 - height - 15))
    win.blit(ArrowSign,(15, 254))
    win.blit(TombStone,(220, 285))
    win.blit(sceleton, (115, 370))
    win.blit(earth, (310, 400 - height - 15))
    win.blit(earth, (410, 400 - height - 15))
    win.blit(earth, (510, 400 - height - 15))
    win.blit(tree, (210, 101))
    win.blit(bone, (250, 320))
    if animcount + 1 >= 30:
        animcount = 0


    if left:
        win.blit(walkRightLeft[animcount // 3], (x, y))
        animcount += 1
    elif right:
        win.blit(walkRightLeft[animcount // 3], (x, y))
        animcount += 1
    elif jump:
        win.blit(playerJump[animcount // 15], (x, y))
        animcount += 1
    elif fall:
        win.blit(falling[animcount // 5], (x, y))
    else:
        win.blit(playerStand[animcount // 1], (x, y))
        animcount += 1

    for bullet in bullets:
        bullet.draw(win)

    pygame.display.update()

bullets = []
game = True
while game:
    clock.tick(frame_rate)

    total_seconds = frame_count // frame_rate
    minutes = total_seconds // 60
    seconds = total_seconds % 60
    output_string = "Time: {0:02}:{1:02}".format(minutes, seconds)

    text = font.render(output_string, True, (0, 0, 0))
    win.blit(text, [15, 15])

    total_seconds = start_time - (frame_count // frame_rate)
    if total_seconds < 0:
        total_seconds = 0

    frame_count += 1






    for bullet in bullets:
        if bullet.x < 600 and bullet.x > 0:
            bullet.x += bullet.vel
        else:
            bullets.pop(bullets.index(bullet))

    keys = pygame.key.get_pressed()

    if keys[pygame.K_f]:
        if lastMove == "right":
            facing = 1
        else:
            facing = -1

        if len(bullets) < 5:
            bullets.append(snaryad(round(x + width // 2), round(y + height // 2), 2, (255, 0, 0),
                                 facing))

    if keys[pygame.K_LEFT] and x>5:
        x -= speed
        left = True
        right = False
        jump = False
        lastMove = "left"
    elif keys[pygame.K_RIGHT] and x < 600 - width - 5:
        x += speed
        right = True
        left = False
        jump = False
        lastMove = "right"



    else:
        left = False
        right = False

        animcount = 0

    if not(isJump):
    
        if keys[pygame.K_SPACE]:
            isJump = True
            jump = True
            left = False
            right = False
    else:
        if JumpCount >= -10:
            left = False
            right = False
            jump = True
            if JumpCount < 0:
                left = False
                right = False
                jump = True
                y += (JumpCount ** 2) / 4
            else:
                left = False
                right = False
                jump = True
                y -= (JumpCount ** 2) / 4
            JumpCount -= 1
        else:
            isJump = False
            JumpCount = 10
            jump = False

    for i in range(len(snow_list)):


        pygame.draw.circle(win, (255, 255 , 255), snow_list[i], 2)


        if snow_list[i][1] + 2 == y and snow_list[i][0] >= x and snow_list[i][0] <= x + width:
            game = False
        else:
            snow_list[i][1] += 2


        if snow_list[i][1] > 600:

            p = random.randrange(-50, -10)
            snow_list[i][1] = p

            d = random.randrange(0, 600)
            snow_list[i][0] = d


        pygame.display.flip()


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
    drawWindow()

