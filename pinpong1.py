from pygame import *

class GameSprite(sprite.Sprite):
    def __init__(self,player_image,player_x,player_y,player_speed,width,height):
        super().__init__()
        self.image = transform.scale(image.load(player_image),(width,height))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image , (self.rect.x , self.rect.y))

racket1 = GameSprite("racket.png",30,200,4,50,150)
racket2 = GameSprite("racket.png",520,200,4,50,150)
ball = GameSprite("tenis_ball.png",200,200,4,50,50)


back = (200,255,255) 
win_width = 600
win_height = 500
window = display.set_mode((win_width,win_height))
window.fill(back)
game = True
finish = False
clock = time.Clock()
FPS = 100


while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    ball.reset()
    racket1.reset()
    racket2.reset()
    display.update()
    clock.tick(FPS)