from face import element

class Face:
    def __init__(self):
        self.xpos = 300
        self.ypos = 300

        self.left_eye = element("eye")
        self.right_eye = element("eye")
        self.left_eyebrow = element("eyebrow")
        self.right_eyebrow = element("eyebrow")

        self.animation1 = [[],[],[],[],[]]

    def draw(self,emotion):
        if emotion == "normal":
            self.left_eye.draw(screen, target_x, target_y, target_xsize, target_ysize, frame=0.1)
            self.right_eye.draw(screen, target_x, target_y, target_xsize, target_ysize, frame=0.1)
            self.left_eyebrow.draw(screen, target_x, target_y, target_xsize, target_ysize, frame=0.1)
            self.right_eyebrow.draw(screen, target_x, target_y, target_xsize, target_ysize, frame=0.1)

        elif emotion == "sad":
            pass
        elif emotion == "suprise":
            pass
        elif emotion == "angery":
            pass
