
import pygame
import time

pygame.init()

#Dimensions de la fenetre
window_resolution=(640,480)

#couleur du rectangle
red=(255,0,0)

#couleur du contenu de la fenetre qd on veut l'effacer
black=(0,0,0)

pygame.display.set_caption("Animation rectangle")#titre de la fenetre

window_surface= pygame.display.set_mode(window_resolution)#fenetre pour l'affichage

#initialisation du rectangle
myrect=pygame.Rect(50,50,200,100)

pygame.draw.rect(window_surface,red,myrect)

#changement de l'affichage de l'ecran
pygame.display.flip()

launched=True
backx=0
backy=0
while launched:
    for event in pygame.event.get():
        if event.type ==pygame.QUIT:
            launched=False
    
    while 1:
    # while myrect.x < window_surface.get_width()-myrect.width:
        time.sleep(0.020)
        window_surface.fill(black)
         
        #si le rectangle atteint le bord en bas mais qu'il n'est tjrs pas arriver a droite il doit rebondir
        if myrect.x>=window_surface.get_width()-myrect.width:
                backx+=1
        if myrect.y>= window_surface.get_height()-myrect.height:
                backy+=1
        if myrect.x<=0:
                backx=0
        if myrect.y<=0:
                backy=0
        
        if backx:
                myrect.x-=1
        else:
                myrect.x+=1
        if backy:
                myrect.y-=1
        else:
                myrect.y+=1
                                                
                
        pygame.draw.rect(window_surface,red,myrect)
        #changement de l'affichage de l'ecran
        pygame.display.flip()
        
    # while myrect.y< window_surface.get_height()-myrect.height:
    #     time.sleep(0.050)
    #     window_surface.fill(black)
    #     myrect.y+=1
    #     pygame.draw.rect(window_surface,red,myrect)
    #     #changement de l'affichage de l'ecran
    #     pygame.display.flip()    