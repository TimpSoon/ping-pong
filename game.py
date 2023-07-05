from pygame import *
window = display.set_mode((700, 500))
display.set_caption('Ping Pong')
background = transform.scale(image.load('sunnyday.png'), (700, 500))
win_width = 700
win_height = 500
game =  True
FPS = 60
clock = time.Clock()

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (75, 75))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def move(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys_pressed[K_DOWN] and self.rect.y < win_height - 70:
            self.rect.y += self.speed 
    def move2(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys_pressed[K_s] and self.rect.y < win_height - 70:
            self.rect.y += self.speed 

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def move(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys_pressed[K_DOWN] and self.rect.y < win_height - 70:
            self.rect.y += self.speed 
    def move2(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys_pressed[K_s] and self.rect.y < win_height - 70:
            self.rect.y += self.speed 
class Ball(GameSprite):
    def polet(self):
        if Rect.colliderect(player1,self):
            self.rect.x += self.speed
        elif Rect.colliderect(player2,self):
            self.rect.x -= self.speed


player1 = GameSprite('racketka.png',10,50,3)
player2 = GameSprite('racketka.png',620,50,3)
ball = Ball('ball.png',player1.rect.x,player1.rect.y,4)

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    window.blit(background,(0,0))


    player1.reset()
    player1.move()
    player2.reset()
    player2.move2()
    ball.reset()
    ball.polet()
    
    clock.tick(FPS)
    display.update()