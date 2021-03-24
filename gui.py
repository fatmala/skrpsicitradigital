from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog
import copy
import cv2
import numpy as np
import csv
from matplotlib import pyplot as plt
from numpy import genfromtxt
import tkinter as tk

import matplotlib
matplotlib.use('TkAgg')

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt

HEIGHT = 700
WIDTH = 1700

root = Tk()
root.title('Image Viewer')
#root.iconbitmap('icon.co')

def open():
    global img, my_image
    root.filename = filedialog.askopenfilename(initialdir="\image", title="Select A file",filetypes=(("jpg files", "*.jpg"), ("all files", "*.*")))
    my_label = Label(root, text=root.filename).grid(row=0, column=0)
    #my_label = Label(root, text=root.filename).pack()
    image_ory = Image.open(root.filename)
    img = cv2.imread(root.filename)
    image = copy.copy(image_ory)
    image = image.resize((550, 350), Image.ANTIALIAS)  ## The (250, 250) is (height, width)
    my_image = ImageTk.PhotoImage(image)
    my_image_label = Label(image_ori, image=my_image).grid(row=0, column=0)
    # my_image_label = Label(image_ori, image=my_image).pack()

def proses():
    # cv2.imshow('GoldenGate',img)
    # img = cv2.imread(image_ory)
    query = cv2.calcHist([img],[1],None,[151],[0,151])
    fig = plt.figure(figsize=(3.5,3.5))
    plt.plot(query)
    canvas = FigureCanvasTkAgg(fig, master=root)
    plot_widget = canvas.get_tk_widget()
    plot_widget.place(relx=0.43, rely=0.18, relwidth=0.25, relheight=0.4)

    img_scaled = cv2.resize(img, None, fx=0.1, fy=0.1)
    img_gray = cv2.cvtColor(img_scaled, cv2.COLOR_BGR2GRAY)
    fig = plt.figure(figsize=(1, 1))
    plt.imshow(img_gray)
    # cv2.imshow('Gambar gray', img_gray)
    # cv2.waitKey(2)
    canvas = FigureCanvasTkAgg(fig, master=root)
    plot_widget = canvas.get_tk_widget()
    plot_widget.place(relx=0.04, rely=0.62, relwidth=0.15, relheight=0.25)

    img_canny2 = cv2.Canny(img_gray, 200, 300)
    imgGrey = img_canny2[::1]
    imgtk = Image.fromarray(imgGrey)
    imgTk = ImageTk.PhotoImage(imgtk)
    my_image_label = Label(canny, image=imgTk).place(relx=0.22, rely=0.62, relwidth=0.15, relheight=0.25)
    # cv2.imshow('Gambar Canny from Gray', img_canny2)
    # cv2.waitKey(1)

    # Put it in the display window
    # my_image_label = Label(canny, image=imgtk).place( relwidth=3, relheight=2)
    # plt.plot(query)
    # plt.show()
    # print(img)



my_btn = Button(root, text="Open File",  command=open).place(relx=0.02, rely=0.1)
# proses = Button(root, text="Proses",  command=proses).pack( side = TOP)
proses = Button(root, text="Proses",  command=proses).place(relx=0.08, rely=0.1)
my_canvas = Canvas(root, height=HEIGHT, width=WIDTH)
# my_canvas = Canvas(root, height=HEIGHT, width=WIDTH).pack()
L1 = Label(root, text='Gambar Original :').place(relx=0.02, rely=0.15)
image_ori = Frame(root, bg='#cad0db')
image_ori.place(relx=0.02, rely=0.18, relwidth=0.4, relheight=0.4)
L2 = Label(root, text='Histogram :').place(relx=0.43, rely=0.15)
histogram = Frame(root, bg='#aeb5c2')
histogram.place(relx=0.43, rely=0.18, relwidth=0.25, relheight=0.4)
L3 = Label(root, text='Grayscale :').place(relx=0.04, rely=0.59)
grayscale = Frame(root, bg='#aeb5c2')
grayscale.place(relx=0.04, rely=0.62, relwidth=0.15, relheight=0.25)
L4 = Label(root, text='Canny :').place(relx=0.22, rely=0.59)
canny = Frame(root, bg='#aeb5c2')
canny.place(relx=0.22, rely=0.62, relwidth=0.15, relheight=0.25)
L5 = Label(root, text='Morfologi Closing :').place(relx=0.40, rely=0.59)
closing = Frame(root, bg='#aeb5c2')
closing.place(relx=0.40, rely=0.62, relwidth=0.15, relheight=0.25)
L6 = Label(root, text='Area :').place(relx=0.58, rely=0.59)
closing = Frame(root, bg='#aeb5c2')
closing.place(relx=0.58, rely=0.62, relwidth=0.15, relheight=0.25)
L7 = Label(root, text='Perimeter :').place(relx=0.76, rely=0.59)
closing = Frame(root, bg='#aeb5c2')
closing.place(relx=0.76, rely=0.62, relwidth=0.15, relheight=0.25)
L8 = Label(root, text='Hasil :').place(relx=0.69, rely=0.15)
hasil = Frame(root, bg='#cad0db')
hasil.place(relx=0.69, rely=0.18, relwidth=0.25, relheight=0.4)
root.attributes("-fullscreen", True)
root.bind("<F11>", lambda event: root.attributes("-fullscreen",
                                    not root.attributes("-fullscreen")))
root.bind("<Escape>", lambda event: root.attributes("-fullscreen", False))
root.mainloop()