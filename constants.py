import pygame

window_width = 600
window_height = 499
elevation = window_height * 0.8
framepersecond = 32

pipeimage = 'Assets/pipe.png'
background_image = 'Assets/background.jpg'
birdplayer_image = 'Assets/bird.png'
sealevel_image = 'Assets/base.jfif'

game_images = {}

window = pygame.display.set_mode((window_width, window_height))

def load_game_images():
    global game_images
    game_images['scoreimages'] = (
        pygame.image.load('Assets/0.png').convert_alpha(),
        pygame.image.load('Assets/1.png').convert_alpha(),
        pygame.image.load('Assets/2.png').convert_alpha(),
        pygame.image.load('Assets/3.png').convert_alpha(),
        pygame.image.load('Assets/4.png').convert_alpha(),
        pygame.image.load('Assets/5.png').convert_alpha(),
        pygame.image.load('Assets/6.png').convert_alpha(),
        pygame.image.load('Assets/7.png').convert_alpha(),
        pygame.image.load('Assets/8.png').convert_alpha(),
        pygame.image.load('Assets/9.png').convert_alpha()
    )
    game_images['flappybird'] = pygame.image.load(birdplayer_image).convert_alpha()
    game_images['sea_level'] = pygame.image.load(sealevel_image).convert_alpha()
    game_images['background'] = pygame.image.load(background_image).convert_alpha()
    game_images['pipeimage'] = (
        pygame.transform.rotate(pygame.image.load(pipeimage).convert_alpha(), 180),
        pygame.image.load(pipeimage).convert_alpha()
    )
