from pygame import *

win_width = 700 
win_height = 500
window = display.set_mode((win_width, win_height))
display.set_caption('ping_pong')
window.fill((100, 200, 200))

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
        if keys[K_UP] and self.rect.Y > 5:
            self.rect.x -= self.speed
        if keys[K_DOWN] and self.rect.Y < win_height - 80:
            self.rect.x += self.speed
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_W] and self.rect.Y > 5:
            self.rect.x -= self.speed
        if keys[K_S] and self.rect.Y < win_height - 80:
            self.rect.x += self.speed

rocket_r = Player('rocket.jpg', 5, win_height - 100, 80, 100, 10)


game =True
finish = False
clock = time.Clock()
FPS = 60
while game : 
   
    for e in event.get():
        if e.type == QUIT:
            game = False
    
    if finish != True:

        rocket_r.update_r()
        rocket_r.reset()


        display.update()

    clock.tick(FPS)
