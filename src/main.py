import pygame
from screen import Screen
from camera import Camera
from object import Object

pygame.init()

icon = pygame.image.load("Assets/simple-3d.ico")
pygame.display.set_icon(icon)

screen = Screen(900, 640, bgcolor=(50, 50, 50))
model = Object("Models/test.obj", position=[0.0, 0.0, 10.0], color=[200, 200, 200])
camera = Camera(position=[0.1, 0.1, 0.1])
clock = pygame.time.Clock()

# Set mouse to FP mode
pygame.event.set_grab(True)
pygame.mouse.set_visible(False)

running = True
while running:
    fps = clock.get_fps()
    pygame.display.set_caption(str(int(clock.get_fps())))
    
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            if event.key == pygame.K_f:
                pygame.display.toggle_fullscreen()
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.VIDEORESIZE:
            screen.update_size(event.w, event.h)
    
    if fps : camera.control(1/fps)        
    screen.render(camera, [model])
    
    pygame.display.flip()
    clock.tick(60)
         
pygame.quit 