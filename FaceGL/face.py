import pygame

class element:
    def __init__(self,str):
        self.xsize = 0.0
        self.ysize = 0.0
        self.xpos = 0.0
        self.ypos = 0.0
        self.angle = 0.0
        self.eye_image = pygame.image.load(str+".png").convert_alpha()

    def draw(self, screen, target_x, target_y, target_xsize, target_ysize, target_angle, frame=60):

        count = [False,False,False,False,False]

        vector1 = abs(self.xpos - target_x) / frame
        vector2 = abs(self.ypos - target_y) / frame
        vector3 = abs(self.xsize - target_xsize) / frame
        vector4 = abs(self.ysize - target_ysize) / frame
        vector5 = abs(self.angle - target_angle) / frame

        if abs(self.xpos - target_x) < 0.00000001:
            count[0]=True
        elif self.xpos > target_x:
            self.xpos -= vector1
        elif self.xpos < target_x:
            self.xpos += vector1

        if abs(self.ypos - target_y) < 0.00000001:
            count[1] = True
        elif self.ypos > target_y:
            self.ypos -= vector2
        elif self.ypos < target_y:
            self.ypos += vector2

        if abs(self.xsize - target_xsize) < 0.00000001:
            count[2] = True
        elif self.xsize > target_xsize:
            self.xsize -= vector3
        elif self.xsize < target_xsize:
            self.xsize += vector3

        if abs(self.ysize - target_ysize) < 0.00000001:
            count[3]=True
        elif self.ysize > target_ysize:
            self.ysize -= vector4
        elif self.ysize < target_ysize:
            self.ysize += vector4

        if abs(self.angle - target_angle) < 0.00000001:
            count[4]=True
        elif self.angle > target_angle:
            self.angle -= vector5
        elif self.angle < target_angle:
            self.angle += vector5

        eye = pygame.transform.scale(self.eye_image,(int(self.xsize),int(self.ysize)))
        eye = pygame.transform.rotate(eye, self.angle)
        screen.blit(eye, (self.xpos, self.ypos))

        if False in count:
            return False
        return True