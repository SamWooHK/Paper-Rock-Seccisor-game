import pygame
import random

#parameters
WIDTH=500
HEIGHT=500
CAPTION="Rock Paper Scissors"
FPS=30
player_choice=""
com_choice=""

#color
RED=(255,0,0)
GREEN=(0,255,0)
BLUE=(0,0,255)

#img
icon_img="icon.png"
choki="janken_choki.png"
gu="janken_gu.png"
pa="janken_pa.png"
pick={choki:"",
            gu:"",
            pa:""}

class Btn:
    def __init__(self,text,color,top,left):
        self.text=text
        self.color=color
        self.top=top
        self.left=left

    def draw(self,screen):
        x=WIDTH//3
        y=HEIGHT//10
        rect=pygame.draw.rect(screen,self.color,(self.top,self.left,x,y))
        font=pygame.font.Font(None,30)
        text=font.render(self.text,True,"black")
        text_center=text.get_rect(center=((rect.x+rect.w)-rect.w//2,(rect.y+rect.h)-rect.h//2))
        screen.blit(text,text_center)
    
        for event in pygame.event.get():

            if event.type == pygame.MOUSEBUTTONDOWN:
                # Set the x, y postions of the mouse click
                x, y = event.pos

                if pygame.Rect.collidepoint(rect,(x,y)):

                    return main(com_pick(pick))

def com_pick(pick):
    com_choice=random.choice(list(pick.keys()))
    return com_choice

def main(com_choice):
    scene=0

    pygame.init()
    clock = pygame.time.Clock()
    screen=pygame.display.set_mode((WIDTH,HEIGHT))
    pygame.display.set_caption(CAPTION)
    pygame.display.set_icon(icon=pygame.image.load(icon_img))

    running=True
    while running:
        screen.fill("white")

        #key events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running=False

            #scene 0 key effect
            if event.type == pygame.MOUSEBUTTONDOWN and scene==0:
                # Set the x, y postions of the mouse click
                x, y = event.pos

                for key,value in pick.items():
                    if pygame.Rect.collidepoint(value,(x,y)):
                        player_choice=key

                        scene=1
        
        if scene==0:
            #Show choices
            for i,img in enumerate(pick):
                choice = pygame.image.load(img).convert()
                choice=pygame.transform.scale(choice,(80,80))
                x=WIDTH//4*(i+1)-choice.get_width()//2
                y=HEIGHT//3
                # Draw rectangle around the image
                rect=pygame.draw.rect(screen,"black",(x,y,80,80))
                screen.blit(choice,(x,y))
                pick[img]=rect

            # pygame.display.flip()

        elif scene==1:
            bg_color="WHITE"
            alert_color=""
            alert_txt=""
            btn_color=""

            font=pygame.font.Font(None,30)
            result={
                "You use":player_choice,
                "COM use":com_choice
            }

            #player win case
            if (player_choice==choki and com_choice==pa) or (player_choice==pa and com_choice==gu) or (player_choice==gu and com_choice==choki):
                bg_color=GREEN
                alert_color="yellow"
                alert_txt="You Win!"
                btn_color="white"
                
            #draw case    
            elif player_choice==com_choice:
                bg_color="black"
                alert_color="white"
                alert_txt="DRAW"
                btn_color="white"
            #lose case
            else:
                bg_color="RED"
                alert_color="gray"
                alert_txt="DRAW"
                btn_color="gray"

            screen.fill(bg_color)
            alert=font.render(alert_txt,True,alert_color)
            alert_center=alert.get_rect(center=(WIDTH//2,HEIGHT//2+50))
            screen.blit(alert,alert_center)

            pos=1
            for txt,img in result.items():
                text=font.render(txt,True,alert_color)
                x=WIDTH//3*pos-text.get_width()//2
                y=100
                screen.blit(text,(x,y))

                img=pygame.image.load(img).convert()
                img=pygame.transform.scale(img,(80,80))
                screen.blit(img,(x,y+50))
                pos+=1
           
            Btn("Play again",btn_color,WIDTH//3,HEIGHT//4*3).draw(screen)

        pygame.display.update()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main(com_pick(pick))
