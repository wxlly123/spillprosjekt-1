import pygame
from sys import exit

def display_score():
    current_time = int(pygame.time.get_ticks() / 1000) - start_time
    score_surf = test_font.render(f'Score: {current_time}', False, (64,64,64))
    score_rect = score_surf.get_rect(center = (400, 50))
    screen.blit(score_surf, score_rect)


pygame.init()
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption('Runner')
clock = pygame.time.Clock()
FPS = 60
test_font = pygame.font.Font('Font/Pixeltype.ttf', 50)
game_active = True
start_time = 0

sky_surface = pygame.image.load('Graphics/Sky.png').convert()
ground_surface = pygame.image.load('Graphics/ground.png').convert()

game_over_surf = test_font.render('Game over', False, 'black')
game_over_rect = game_over_surf.get_rect(center = (400, 200))

# score_surf = test_font.render('My game', False, (64,64,64))
# score_rect = score_surf.get_rect(center = (400,50))

snail_surf = pygame.image.load('Graphics/snail1.png').convert_alpha()
snail_rect = snail_surf.get_rect(bottomright = (600,300))

player_surf = pygame.image.load ('Graphics/player_walk_1.png').convert_alpha()
player_rect = player_surf.get_rect(midbottom = (80,300))

player_gravity = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if game_active:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and player_rect.bottom >= 300:
                        player_gravity = -20
        else:
             if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                  game_active = True
                  snail_rect.left = 800
                  start_time = int(pygame.time.get_ticks() / 1000)
        
    if game_active:        
        screen.blit(sky_surface,(0,0))
        screen.blit(ground_surface,(0,300))
        # pygame.draw.rect(screen,'#c0e8ec',score_rect)
        # pygame.draw.rect(screen,'#c0e8ec',score_rect,10)
        # screen.blit(score_surf, score_rect)
        display_score()

        snail_rect.x -= 5
        if snail_rect.x <= -10: snail_rect.x = 800
        screen.blit(snail_surf, snail_rect)

        player_gravity += 1
        player_rect.y += player_gravity
        if player_rect.bottom >= 300: player_rect.bottom = 300
        screen.blit(player_surf, player_rect)

        if snail_rect.colliderect(player_rect):
            game_active = False
    else:
         screen.fill('Red')
         screen.blit(game_over_surf, game_over_rect)

   # keys = pygame.key.get_pressed()
    #if keys[pygame.K_SPACE]:
    #    print('jump')

    pygame.display.update()
    clock.tick(FPS)
