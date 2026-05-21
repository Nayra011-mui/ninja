from pygame import *

class GameSprite(sprite.Sprite):
    def __init__ (self, player_image, player_x, player_y, player_speed, weight, height):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (weight, height))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
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
        
back = (200, 255, 255)
win_width = 600
win_height = 500
window = display.set_mode((win_width, win_height))
window.fill(back)

ninja1 = Player('ninja kiri.png', 25, 200, 4, 85, 150)
ninja2 = Player('ninja.png', 490, 200, 4, 85, 150)
ball = GameSprite('shuriken.png', 200, 200, 4, 50, 50)

font.init()
font = font.Font(None, 35)
lose1 = font.render('PLAYE 1 LOSE!', True, (180, 0, 0))
lose2 = font.render('PLAYER 2 LOSE!', True, (180, 0 , 0))

speed_x = 5
speed_y = 5


game = True
finish = False
clock = time.Clock()
FPS = 60

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

        if finish and e.type == KEYDOWN and e.key == K_r:
            ball.rect.x = 200
            ball.rect.y = 200
            speed_x = 5
            speed_y = 5
            ninja1.rect.y = 200
            ninja2.rect.y = 200
            finish = False

    if finish != True:
        window.fill(back)
        ninja1.update_l()
        ninja2.update_r()

        ninja1.reset()
        ninja2.reset()
        ball.reset()

        ball.rect.x += speed_x
        ball.rect.y += speed_y

        if sprite.collide_rect(ninja1, ball) or sprite.collide_rect(ninja2, ball):
            speed_x *= -1
            speed_y *= 1

        if ball.rect.y > win_height-5 or ball.rect.y <0:
            speed_y *= -1

        if ball.rect.x < 0:
            finish = True
            window.blit(lose1, (200, 200))
            restart_text = font.render ('Tekan T untu restart', true, (0, 0, 0))
            window.blit(restart_text, (180, 250))
            game_oveer = True

        if ball.rect.x > win_width:
            finish = True
            window.blit(lose2, (200, 200))
            restart_text = font.render('Tekan R untuk restart', True, (0, 0, 0))
            window.blit(restart_text, (180, 250))
            game_over = True

        
    display.update()
    clock.tick(FPS)