import pygame
from sys import exit

pygame.init()
screen=pygame.display.set_mode((800,400))
pygame.display.set_caption('Runner')
clock=pygame.time.Clock()
test_font=pygame.font.Font('font/Pixeltype.ttf',100)



sky_surface=pygame.image.load('graphics/Sky.png')
ground_surface=pygame.image.load('graphics/ground.png')
text_surface=test_font.render("hello world",False,'Black')
snail_surface=pygame.image.load('graphics/snail/snail1.png').convert_alpha()
snail_x_pos=600

player_surface=pygame.image.load('graphics/player/player_walk_1.png')
player_rect=player_surface.get_rect(midbottom=(80,300))
while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            exit()
    screen.blit(sky_surface,(0,0))
    screen.blit(ground_surface,(0,300))
    screen.blit(text_surface, (250,50))
    snail_x_pos-=4
    if snail_x_pos<0:
        snail_x_pos=800
    screen.blit(snail_surface,(snail_x_pos,250))
    player_rect.left+=1
    screen.blit(player_surface, player_rect)
    pygame.display.update()
    clock.tick(60) 