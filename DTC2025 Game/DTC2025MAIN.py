###########                Imports Start                ###########
import subprocess
import sys


def install_os():
    try:
        import os
        print("os is already installed")
    except ImportError:
        print("os not found. Installing...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "os"])
        print("os installed successfully")



def install_pygame():
    try:
        import pygame
        print("pygame is already installed")
    except ImportError:
        print("pygame not found. Installing...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "pygame"])
        print("pygame installed successfully")


install_pygame()
install_os()
install_json()
install_random()

import pygame

###########                Imports end                               ###########



###########                keyboard presses                          ###########


###########                keyboard presses                          ###########

def handle_key_press(event, sprites):
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            for sprite in sprites:
                sprite.x -= 5  
        elif event.key == pygame.K_RIGHT:
            for sprite in sprites:
                sprite.x += 5  
        elif event.key == pygame.K_UP:
            for sprite in sprites:
                sprite.y -= 5  
        elif event.key == pygame.K_DOWN:
            for sprite in sprites:
                sprite.y += 5  
        elif event.key == pygame.K_1 and len(sprites) >= 1:
            sprites[0].change_image("pixilart-sprite (1).png")
        elif event.key == pygame.K_2 and len(sprites) >= 2:
            sprites[1].change_image("pixilart-sprite (1).png")
        elif event.key == pygame.K_3 and len(sprites) >= 3:
            sprites[2].change_image("pixilart-sprite (1).png")
        elif event.key == pygame.K_SPACE:
            

            new_sprite = Sprite(300, 300, image_path="pixilart-sprite (1).png")
            sprites.append(new_sprite)

###########                sprite definition and const               ###########

WIDTH, HEIGHT = 800, 600
blue = (0, 0, 255)
red = (255, 0, 0)
green = (0, 255, 0)

class Sprite:
    def __init__(self, x=0, y=0, width=50, height=50, color=(0, 0, 0), image_path=None, 
                 ground_y=0, gravity=0, jump_strength=0):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.velocity_y = 0
        self.ground_y = ground_y if ground_y is not None else HEIGHT - 100
        self.gravity = gravity
        self.jump_strength = jump_strength
        
        if image_path:
            self.image = pygame.image.load(image_path)
            self.image = pygame.transform.scale(self.image, (self.width, self.height))
            self.use_image = True
        else:
            self.use_image = False

    def change_image(self, new_image_path):
        self.image = pygame.image.load(new_image_path)
        self.image = pygame.transform.scale(self.image, (self.width, self.height))
        self.use_image = True
    
    def update(self):
        self.velocity_y += self.gravity
        self.y += self.velocity_y
        
        if self.y >= self.ground_y:
            self.y = self.ground_y
            self.velocity_y = self.jump_strength
    
    def draw(self, surface):
        if self.use_image:
            surface.blit(self.image, (self.x, self.y))
        else:
            pygame.draw.rect(surface, self.color, (self.x, self.y, self.width, self.height))

###########                Game Startup                ###########
def main():
    pygame.init()

    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("DTC2025")

    BACKGROUND_COLOR = (255, 255, 255)
    CIRCLE_COLOR = (0, 0, 255)
    CIRCLE_RADIUS = 20

    sprite1 = Sprite(x=100, y=HEIGHT-150, width=50, height=50, color=red)
    sprite2 = Sprite(x=200, y=HEIGHT-150, width=50, height=50, color=blue, image_path="")
    sprite3 = Sprite(x=300, y=HEIGHT-250, width=50, height=50, color=green, image_path="ball.png")

    sprites = [sprite1, sprite2, sprite3]

    running = True
    clock = pygame.time.Clock()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            handle_key_press(event, sprites)

        for sprite in sprites:
            sprite.update()

        mouse_x, mouse_y = pygame.mouse.get_pos()

        screen.fill(BACKGROUND_COLOR)

        for sprite in sprites:
            sprite.draw(screen)

        pygame.draw.circle(screen, CIRCLE_COLOR, (mouse_x, mouse_y), CIRCLE_RADIUS)

        pygame.display.flip()

        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":

    main()
