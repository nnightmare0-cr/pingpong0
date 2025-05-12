

import pygame
import time

 
pygame.init()
 
back = (200, 255, 255)

window = pygame.display.set_mode((500, 500)) 
window.fill(back) 
clock = pygame.time.Clock() 




class Area():

    def __init__(self, x=0, y=0, width=10, height=10, color=None):
        self.rect = pygame.Rect(x, y, width, height) 
        self.fill_color = back
        if color:
            self.fill_color = color
 

    def color(self,new_color):
        self.fill_color = new_color
 
    def fill(self):
        pygame.draw.rect(window, self.fill_color, self.rect)
 

    def collidepoint(self, x, y):
        return self.rect.collidepoint(x, y)


    def colliderect(self, rect):
        return self.rect.colliderect(rect)

class Picture(Area):
    def __init__(self, image1, x=0, y=0, width=10, height=10):
        Area.__init__(self, x=x, y=y, width=width, height=height, color=None)
        self.image=pygame.image.load(image1)

    def draw(self, shift_x=0, shift_y=0):
        window.blit(self.image,(self.rect.x + shift_x, self.rect.y + shift_y))

class Label(Area):
    def set_text(self, text, fsize=12, color=(0,0,0)):
        self.font = pygame.font.SysFont('verdana', fsize) 
        self.image = self.font.render(text,True, color)
 

    def draw(self, shift_x=0, shift_y=0):
        self.fill() 
        window.blit(self.image,(self.rect.x + shift_x, self.rect.y + shift_y)) 
 


image_ball = ""
ball = Picture(image_ball, 250, 250, 50, 50)
image_platform = ""
platform = Picture(image_platform, 300, 300, 100, 100)

start_x = 5
start_y = 5
count = 9
monsters = []
for i in range(3):
    y = start_y + (55 * i)
    x = start_x + (27.5 * i)
    for i in range(count):
        d = Picture('', x, y, 50, 50)
        monsters.append(d)
        x = x + 55
    count = count - 1

game_over = False

speed_x = 3
speed_y = 3
move_right = False
move_left = False
while game_over != True:
    ball.fill()
    platform.fill()
    

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                move_right = True
            if event.key == pygame.K_LEFT:
                move_left = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                move_right = False
            if event.key == pygame.K_LEFT:
                move_left = False

    if move_right:
        platform.rect.x += 3

    if move_left:
        platform.rect.x -= 3  

    if ball.colliderect(platform.rect):
        speed_y *= -1
        sound4.play()


    if ball.rect.y < 0:
        speed_y *= -1

    if ball.rect.x >450 or ball.rect.x < 0:
        speed_x *= -1
    
    if ball.rect.y > (platform.rect.y + 20):
        time_text = Label(150, 150, 50, 50, back)
        time_text.set_text('YOU LOSE', 60, (255, 0, 0))
        time_text.draw(10, 10)
        game_over = True


    if len(monsters) == 0:
        time_text = Label(150, 150, 50, 50, back)
        time_text.set_text('YOU WIN', 60, (0, 200, 0))
        time_text.draw(10, 10)
        game_over = True


    ball.rect.x += speed_x
    ball.rect.y += speed_y

    for m in monsters:
        m.draw()
        if m.rect.colliderect(ball.rect):
            monsters.remove(m)
            m.fill()
            speed_y *= -1
            speed_y += 1
            speed_x += 1
            sound3.play()






    platform.draw()
    ball.draw()




    pygame.display.update()
    clock.tick(40)



