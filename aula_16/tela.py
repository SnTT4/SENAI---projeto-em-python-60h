import pygame


pygame.init()
tamanho  =  300,150
screen = pygame.display.set_mode(tamanho)


run = True
while run:
     for event in pygame.event.get():
         if event.type == pygame.QUIT:
            run = False
         screen.fill('LightSkyBlue')
         
         pygame.draw.rect(screen,'black',(125,50,50,50) ) 
         pygame.draw.circle(screen,'green',(90 , 35), 35)
         pygame.draw.line(screen, 'blue', (60, 40), (10, 50), 5) 
         pygame.draw.ellipse(screen, 'yellow', [40, 15, 30, 25], 2)
         pygame.display.update()
         
pygame.quit()               
         
         
    


  



