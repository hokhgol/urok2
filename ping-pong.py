from pygame import *
from time import sleep
font.init()

win_width = 700 
win_height = 500
window = display.set_mode((win_width, win_height))
display.set_caption('ping_pong')
window.fill((100, 200, 200))
speed_x = 3
speed_y = 3
font1 = font.Font(None, 35)
lose1 = font1.render('PLAYER 1 LOSE!', True, (180, 0, 0))
lose2 = font1.render('PLAYER 2 LOSE!', True, (180, 0, 0))
wins_r = 0
wins_l = 0



class GameSprite(sprite.Sprite):
    def __init__ (self, player_image, player_x, player_y, size_x, size_y, player_speed):
        super(). __init__() 
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player (GameSprite):
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height - 80:
            self.rect.y += self.speed
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_height - 80:
            self.rect.y += self.speed

rocket_l = Player('rocket3.png', 5, win_height - 250, 20, 100, 10)
rocket_r = Player('rocket3.png', 675, win_height - 250, 20, 100, 10)
ball = GameSprite('ball3.png', 350, win_height - 250, 75, 75, 10)

game =True
finish = False
clock = time.Clock()
FPS = 60
while game : 
   
    for e in event.get():
        if e.type == QUIT:
            game = False
    
    if finish != True:
        window.fill((100, 200, 200))
        ball.rect.x += speed_x
        ball.rect.y += speed_y
        if ball.rect.y > 425 or ball.rect.y < 0:
            speed_y *= -1
        if sprite.collide_rect(rocket_l, ball) or sprite.collide_rect(rocket_r, ball):
            speed_x *= -1

        player_l = font1.render(str(wins_l),  True, (255, 255, 255))
        player_r = font1.render(str(wins_r), True, (255, 255, 255))
        rocket_l.update_l()
        rocket_r.update_r()      
        rocket_l.reset()
        rocket_r.reset()
        ball.reset()
        window.blit(player_l, (10, 10))
        window.blit(player_r, (650, 10))

        if ball.rect.x < 0 :
            finish = True
            window.blit(lose1, (200, 200))
            wins_r += 1

        if ball.rect.x > 700 :
            finish = True
            window.blit(lose2, (200, 200))
            wins_l += 1 

        display.update()
    else :
        if ((wins_l % 5) == 0 or (wins_r % 5) == 0) and ((wins_l > 0) or (wins_l > 0)):
            if speed_x > 0:
                speed_x += 1
            else:
                speed_x -= 1

            if speed_y > 0:
                speed_y += 1
            else:
                speed_y -= 1


        sleep(2)
        ball.rect.x = win_width/2
        ball.rect.y = win_height/2
        rocket_l.rect.x = 5
        rocket_l.rect.y = win_height -250
        rocket_r.rect.x = 675
        rocket_r.rect.y = win_height - 250  
        finish = False

    clock.tick(FPS)
