from face import element
import pygame
import math
pygame.init()
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
size = [1080, 540]

screen = pygame.display.set_mode(size)
pygame.display.set_caption("Example code for the draw module")
done = False
clock = pygame.time.Clock()

left_eye = element("eye")
right_eye = element("eye")
left_eyebrow = element("eyebrow")
right_eyebrow = element("eyebrow")

face_xpos = 0
face_ypos = 0

count = 0

left_eyebrow_pos = [250.0,150.0,100.0, 20.0,0]
left_eye_pos = [250.0, 200.0, 100.0, 150.0,0]
right_eyebrow_pos = [500.0, 150.0, 100.0, 20.0,0]
right_eye_pos = [500.0, 200.0, 100.0, 150.0,0]

while not done:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                left_eyebrow_pos = [250.0-30, 150.0-30, 100.0, 20.0,0]
                left_eye_pos = [250.0-50, 200.0, 100.0*1.5, 150.0*1.5,0]
                right_eyebrow_pos = [500.0+50, 150.0-30, 100.0, 20.0,0]
                right_eye_pos = [500.0+30, 200.0, 100.0*1.5, 150.0*1.5,0]
            if event.key == pygame.K_RIGHT:
                left_eyebrow_pos = [250.0-30, 150.0+50, 100.0, 20.0,30]
                left_eye_pos = [250.0, 200.0+70, 100.0*0.8, 150.0*0.8,0]
                right_eyebrow_pos = [500.0+30, 150.0+50, 100.0, 20.0,-30]
                right_eye_pos = [500.0+10, 200.0+70, 100.0*0.8, 150.0*0.8,0]
            if event.key == pygame.K_DOWN:
                left_eyebrow_pos = [250.0, 150.0, 100.0, 20.0,0]
                left_eye_pos = [250.0, 200.0, 100.0, 150.0,0]
                right_eyebrow_pos = [500.0, 150.0, 100.0, 20.0,0]
                right_eye_pos = [500.0, 200.0, 100.0, 150.0,0]
            if event.key == pygame.K_UP:
                left_eyebrow_pos = [250.0+30, 150.0, 100.0, 20.0,-30]
                left_eye_pos = [250.0+30, 200.0, 100.0, 150.0,0]
                right_eyebrow_pos = [500.0-30, 150.0, 100.0, 20.0,30]
                right_eye_pos = [500.0-30, 200.0, 100.0, 150.0,0]
    count+=1
    face_xpos = 100 + math.sin(math.radians(count))*100
    face_ypos = math.sin(math.radians(count*3))*20

    screen.fill(BLACK)
    if left_eyebrow.draw(screen, face_xpos+left_eyebrow_pos[0], face_ypos+left_eyebrow_pos[1], left_eyebrow_pos[2], left_eyebrow_pos[3],left_eyebrow_pos[4], frame=30):
        print "done"
    if left_eye.draw(screen, face_xpos+left_eye_pos[0], face_ypos+left_eye_pos[1], left_eye_pos[2], left_eye_pos[3],left_eye_pos[4], frame=30):
        print "done"
    if right_eyebrow.draw(screen, face_xpos+right_eyebrow_pos[0], face_ypos+right_eyebrow_pos[1], right_eyebrow_pos[2], right_eyebrow_pos[3],right_eyebrow_pos[4], frame=30):
        print "done"
    if right_eye.draw(screen, face_xpos+right_eye_pos[0], face_ypos+right_eye_pos[1], right_eye_pos[2], right_eye_pos[3],right_eye_pos[4], frame=30):
        print "done"

    pygame.display.flip()

# Be IDLE friendly
pygame.quit()