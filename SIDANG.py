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
from operator import itemgetter
from heapq import merge
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
    my_label = Label(root, text=root.filename).place(relx=0.13, rely=0.105)
    #my_label = Label(root, text=root.filename).pack()
    image_ory = Image.open(root.filename)
    img = cv2.imread(root.filename)
    image = copy.copy(image_ory)
    image = image.resize((550, 350), Image.ANTIALIAS)  ## The (250, 250) is (height, width)
    my_image = ImageTk.PhotoImage(image)
    my_image_label = Label(image_ori, image=my_image).grid(row=0, column=0)
    # my_image_label = Label(image_ori, image=my_image).pack()

def proses():
    global can, gray, clos, peri, ar
    # cv2.imshow('GoldenGate',img)
    # img = cv2.imread(image_ory)
    warna_pre = cv2.calcHist([img],[1],None,[151],[0,151])
    fig = plt.figure(figsize=(3.5,3.5))
    plt.plot(warna_pre,color='g')
    canvas = FigureCanvasTkAgg(fig, master=root)
    plot_widget = canvas.get_tk_widget()
    plot_widget.place(relx=0.43, rely=0.18, relwidth=0.25, relheight=0.4)

    shape = []
    img_scaled = cv2.resize(img, None, fx=0.1, fy=0.1)
    img_gray = cv2.cvtColor(img_scaled, cv2.COLOR_BGR2GRAY)
    cv2.imwrite("grayscale.jpg", img_gray)
    img_gr=Image.open("grayscale.jpg")
    img_gr = img_gr.resize((200, 300), Image.ANTIALIAS)
    gray = ImageTk.PhotoImage(img_gr)
    my_image_gray = Label(grayscale, image=gray).place(relwidth=1, relheight=1)


    img_canny2 = cv2.Canny(img_gray, 200, 300)
    cv2.imwrite("canny.jpg", img_canny2)
    img_canny=Image.open("canny.jpg")
    img_canny= img_canny.resize((200, 300), Image.ANTIALIAS)
    can = ImageTk.PhotoImage(img_canny)
    my_image_canny = Label(canny, image=can).place(relwidth=1, relheight=1)


    kernel = np.ones((5,5),np.uint8)
    morclosing = cv2.morphologyEx(img_canny2, cv2.MORPH_CLOSE, kernel)
    cv2.imwrite("closing.jpg", morclosing)
    img_cl=Image.open("closing.jpg")
    img_cl = img_cl.resize((200, 300), Image.ANTIALIAS)
    clos = ImageTk.PhotoImage(img_cl)
    my_image_closing = Label(closing, image=clos).place(relwidth=1, relheight=1)

    _, contours, hierarchy = cv2.findContours(morclosing,
      cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE) 
    area=0
    equi_diameter=0
    for x in range(len(contours)):
        area += cv2.contourArea(contours[x]) 
        equi_diameter = np.sqrt(4*area/np.pi)  
    shape.append(area)
    shape.append(equi_diameter)
    img_scaled1 = copy.copy(img_scaled)
    cv2.drawContours(img_scaled1, contours, -1, (0, 255, 0), 3) 
    cv2.imwrite("area.jpg", img_scaled1)
    img_area=Image.open("area.jpg")
    img_area = img_area.resize((200, 300), Image.ANTIALIAS)
    ar = ImageTk.PhotoImage(img_area)
    my_image_area = Label(area_, image=ar).place(relwidth=1, relheight=1)     


    perimeter = 0
    for x in range(len(contours)):
      peri = cv2.arcLength(contours[x], True)
      approx = cv2.approxPolyDP(contours[x], 0.02 * peri, True)
      perimeter += peri 
    shape.append(perimeter)   
    img_scaled2 = copy.copy(img_scaled)
    cv2.drawContours(img_scaled2, [approx], -1, (0, 0, 255), 2)
    cv2.imwrite("perimeter.jpg", img_scaled2)
    img_perimeter=Image.open("perimeter.jpg")
    img_perimeter = img_perimeter.resize((200, 300), Image.ANTIALIAS)
    peri = ImageTk.PhotoImage(img_perimeter)
    my_image_perimeter = Label(perimeters, image=peri).place(relwidth=1, relheight=1)

    # hasil
    hasil ="Area : "+str(area)+"\n Equivalent Diameter : "+str(equi_diameter)+"\n Perimeter : "+str(perimeter)
    my_hasil = Label(root, text=hasil).place(relx=0.73, rely=0.20)

    label = genfromtxt('label.csv', delimiter=',')
    warna_training = genfromtxt('warna_training.csv', delimiter=',')
    shape_training = genfromtxt('shape_training.csv', delimiter=',')
    all_training = genfromtxt('all_training.csv', delimiter=',')

    distance_warna = euclidean_distance(warna_pre,warna_training)
    comb_warna = np.column_stack((distance_warna, label))
    sort_warna = sorted(comb_warna, key=itemgetter(0))

    distance_shape = euclidean_distance(shape,shape_training)
    comb_shape = np.column_stack((distance_shape, label))
    sort_shape = sorted(comb_shape, key=itemgetter(0))

    # print(distance_shape)
    all_ = list(merge(warna_pre , shape))
    distance_all = euclidean_distance(all_,all_training)
    comb_all = np.column_stack((distance_all, label))
    sort_all = sorted(comb_all, key=itemgetter(0))
    # print(len(all_))
    
    if (sort_warna[0][1]==1):
        hasil_warna ="Hasil Pendekatan Warna : \n Distance : "+str(sort_warna[0][0])+"\n(Terdeteksi Penyakit) "
    else:
        hasil_warna ="Hasil Pendekatan Warna : \n Distance : "+str(sort_warna[0][0])+"\n(Tidak Terdeteksi Penyakit) "
    hsl_warna = Label(root, text=hasil_warna, font=('Helvetica', 9, 'bold')).place(relx=0.73, rely=0.30)    

    if (sort_shape[0][1]==1):
        hasil_shape ="Hasil Pendekatan Bentuk : \n Distance : "+str(sort_shape[0][0])+"\n(Terdeteksi Penyakit) "
    else:
        hasil_shape ="Hasil Pendekatan Bentuk : \n Distance : "+str(sort_shape[0][0])+"\n(Tidak Terdeteksi Penyakit) "
    hsl_bentuk = Label(root, text=hasil_shape, font=('Helvetica', 9, 'bold')).place(relx=0.73, rely=0.4)    

    if (sort_all[0][1]==1):
        hasil_all ="Hasil Pendekatan Warna dan Bentuk : \n Distance : "+str(sort_all[0][0])+"\n(Terdeteksi Penyakit) "
    else:
        hasil_all ="Hasil Pendekatan Warna dan Bentuk : \n Distance : "+str(sort_all[0][0])+"\n(Tidak Terdeteksi Penyakit) "
    hsl_all = Label(root, text=hasil_all, font=('Helvetica', 9, 'bold')).place(relx=0.73, rely=0.5)    


def euclidean_distance(query, myArray):
    euclidean_distance = []
    for x in range(len(myArray)):
        sume = 0
        for y in range(len(myArray[0])):
            sume += (query[y]-myArray[x][y])**2
        euclidean_distance.append(np.sqrt(sume))
    return euclidean_distance




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
area_ = Frame(root, bg='#aeb5c2')
area_.place(relx=0.58, rely=0.62, relwidth=0.15, relheight=0.25)
L7 = Label(root, text='Perimeter :').place(relx=0.76, rely=0.59)
perimeters = Frame(root, bg='#aeb5c2')
perimeters.place(relx=0.76, rely=0.62, relwidth=0.15, relheight=0.25)
L8 = Label(root, text='Hasil :').place(relx=0.69, rely=0.15)
hasil = Frame(root, bg='#cad0db')
hasil.place(relx=0.69, rely=0.18, relwidth=0.25, relheight=0.4)
root.attributes("-fullscreen", True)
root.bind("<F11>", lambda event: root.attributes("-fullscreen",
                                    not root.attributes("-fullscreen")))
root.bind("<Escape>", lambda event: root.attributes("-fullscreen", False))
root.mainloop()