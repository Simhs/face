# -*- coding: utf-8 -*-
from Tkinter import *
import pygame
from face import element
import math
from Tkinter import *
from PIL import ImageTk, Image
import Tkinter, Tkconstants, tkFileDialog
import os
import classify

cf = classify.Image()
images = []
g_index = 0
left_eyebrow_pos = [250.0, 150.0, 100.0, 20.0, 0]
left_eye_pos = [250.0, 200.0, 100.0, 150.0, 0]
right_eyebrow_pos = [500.0, 150.0, 100.0, 20.0, 0]
right_eye_pos = [500.0, 200.0, 100.0, 150.0, 0]
mouse_pos = [370.0,400.0,100.0,30.0,0]
def select_image_dir():
    global images,g_index
    g_index = 0
    images_dir = tkFileDialog.askdirectory(initialdir = "/home/sim/Desktop",title = "Select DIR")
    images_dir_entry.delete(0, 'end')
    images_dir_entry.insert(END,str(images_dir))
    print (images_dir)
    path = images_dir_entry.get()
    if path == "":
        return
    images = os.listdir(path)
    openimg = Image.open(path+"/"+images[0])
    img = openimg.resize((200, 200), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img)

    image.configure(image=img)
    image.image = img
    answer, labels, predictions =cf.run_inference_on_image(path+"/"+images[0])
    graph_done = False
    changeGraph(answer, labels, predictions)


def left_classify():
    global images,g_index
    g_index -= 1
    path = images_dir_entry.get()
    if path == "":
        return
    images = os.listdir(path)
    openimg = Image.open(path+"/"+images[g_index%len(images)])
    img = openimg.resize((200, 200), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img)

    image.configure(image=img)
    image.image = img
    answer, labels, predictions = cf.run_inference_on_image(path+"/"+images[g_index%len(images)])

    graph_done = False
    changeGraph(answer, labels, predictions)

def right_classify():
    global images,g_index
    g_index +=1
    path = images_dir_entry.get()
    if path == "":
        return
    images = os.listdir(path)
    openimg = Image.open(path+"/"+images[g_index%len(images)])
    img = openimg.resize((200, 200), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img)

    image.configure(image=img)
    image.image = img
    answer, labels, predictions = cf.run_inference_on_image(path+"/"+images[g_index%len(images)])

    graph_done = False
    changeGraph(answer, labels, predictions)



def changeGraph(answer,labels,predictions):
    global left_eyebrow_pos,left_eye_pos,right_eyebrow_pos,right_eye_pos,mouse_pos
    p1 = int(predictions[0] * 999)
    p2 = int(predictions[1] * 999)
    p3 = int(predictions[2] * 999)
    p4 = int(predictions[3] * 999)

    c.create_arc((2, 2, 300, 300), fill="#FF0000", outline="#000000", start=prop(0), extent=prop(p1))
    c.create_arc((2, 2, 300, 300), fill="#FF8000", outline="#000000", start=prop(p1), extent=prop(p2))
    c.create_arc((2, 2, 300, 300), fill="#FFFF00", outline="#000000", start=prop(p1+p2), extent=prop(p3))
    c.create_arc((2, 2, 300, 300), fill="#80FF00", outline="#000000", start=prop(p1+p2+p3), extent=prop(p4))

    if answer == "surprised emotion":  # 놀람
        left_eyebrow_pos = [250.0 - 30, 150.0 - 30, 100.0, 20.0, 0]
        left_eye_pos = [250.0 - 50, 200.0, 100.0 * 1.5, 150.0 * 1.5, 0]
        right_eyebrow_pos = [500.0 + 50, 150.0 - 30, 100.0, 20.0, 0]
        right_eye_pos = [500.0 + 30, 200.0, 100.0 * 1.5, 150.0 * 1.5, 0]
        mouse_pos = [420.0, 400.0, 1.0, 1.0, 0]
    elif answer == "sad emotion":  # 슬픔
        left_eyebrow_pos = [250.0 - 30, 150.0 + 50, 100.0, 20.0, 30]
        left_eye_pos = [250.0, 200.0 + 70, 100.0 * 0.8, 150.0 * 0.8, 0]
        right_eyebrow_pos = [500.0 + 30, 150.0 + 50, 100.0, 20.0, -30]
        right_eye_pos = [500.0 + 10, 200.0 + 70, 100.0 * 0.8, 150.0 * 0.8, 0]
        mouse_pos = [420.0, 400.0, 1.0, 1.0, 0]
    elif answer == "happy emotion":  # 일반
        left_eyebrow_pos = [250.0, 150.0, 100.0, 20.0, 0]
        left_eye_pos = [250.0, 200.0, 100.0, 150.0, 0]
        right_eyebrow_pos = [500.0, 150.0, 100.0, 20.0, 0]
        right_eye_pos = [500.0, 200.0, 100.0, 150.0, 0]
        mouse_pos = [370.0, 400.0, 100.0, 30.0, 0]
    elif answer == "angery emotion":  # 화난
        left_eyebrow_pos = [250.0 + 30, 150.0, 100.0, 20.0, -30]
        left_eye_pos = [250.0 + 30, 200.0, 100.0, 150.0, 0]
        right_eyebrow_pos = [500.0 - 30, 150.0, 100.0, 20.0, 30]
        right_eye_pos = [500.0 - 30, 200.0, 100.0, 150.0, 0]
        mouse_pos = [370.0, 400.0, 100.0, 30.0, 20]


def prop(n):
    return 360.0 * n / 1000

root = Tk()
embed = Frame(root)

images_dir_entry = Entry(root,width = 40)
images_dir_entry.grid(row=1,column=0)

playpausebutton = Button(root, command=select_image_dir, text="select images dir")
playpausebutton.grid(row=1, column=1)

playpausebutton = Button(root, command=left_classify, text="Left")
playpausebutton.grid(row=2, column=0)

playpausebutton = Button(root, command=right_classify, text="Right")
playpausebutton.grid(row=2, column=1)

c = Canvas(root,width=320, height=320)
c.create_arc((2,2,300,300), fill="#FF0000", outline="#000000", start=prop(0), extent = prop(0))
c.create_arc((2,2,300,300), fill="#FF8000", outline="#000000", start=prop(0), extent = prop(0))
c.create_arc((2,2,300,300), fill="#FFFF00", outline="#000000", start=prop(0), extent = prop(0))
c.create_arc((2,2,300,300), fill="#80FF00", outline="#000000", start=prop(0), extent = prop(999))
c.grid(row=3,column=0)

openimg = Image.open("./NoImage.png")
img = openimg.resize((200,200), Image.ANTIALIAS)
img = ImageTk.PhotoImage(img)

image = Label(root, image = img)
image.grid(row=3, column=1)

root.update()
pygame.display.init()
screen = pygame.display.set_mode((1080, 540))

pygame.display.flip()
BLACK = (0, 0, 0)

left_eye = element("eye")
right_eye = element("eye")
left_eyebrow = element("eyebrow")
right_eyebrow = element("eyebrow")
mouse = element("eyebrow")


face_xpos = 0
face_ypos = 0
count = 0

clock = pygame.time.Clock()

while True:
    # your code here
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    count += 1
    face_xpos = 100 + math.sin(math.radians(count)) * 100
    face_ypos = math.sin(math.radians(count * 3)) * 20

    screen.fill(BLACK)
    if left_eyebrow.draw(screen, face_xpos + left_eyebrow_pos[0], face_ypos + left_eyebrow_pos[1],
                         left_eyebrow_pos[2], left_eyebrow_pos[3], left_eyebrow_pos[4], frame=30):
        print "done"
    if left_eye.draw(screen, face_xpos + left_eye_pos[0], face_ypos + left_eye_pos[1], left_eye_pos[2],
                     left_eye_pos[3], left_eye_pos[4], frame=30):
        print "done"
    if right_eyebrow.draw(screen, face_xpos + right_eyebrow_pos[0], face_ypos + right_eyebrow_pos[1],
                          right_eyebrow_pos[2], right_eyebrow_pos[3], right_eyebrow_pos[4], frame=30):
        print "done"
    if right_eye.draw(screen, face_xpos + right_eye_pos[0], face_ypos + right_eye_pos[1], right_eye_pos[2],
                      right_eye_pos[3], right_eye_pos[4], frame=30):
        print "done"
    if mouse.draw(screen, face_xpos + mouse_pos[0], face_ypos + mouse_pos[1], mouse_pos[2],
                      mouse_pos[3], mouse_pos[4], frame=30):
        print "done"

    pygame.display.flip()
    root.update()