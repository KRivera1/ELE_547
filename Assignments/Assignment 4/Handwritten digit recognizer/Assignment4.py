# Script: Assignment4.py
# Description: This is a program to practice utilizing artificial
#			   neural networks. Hand written numerical digits between
#			   0 - 9 can be recognized by utilizing a model derived
#			   from a training list program. For best results, draw the
#			   number at the center of the drawing canvas and make it large
#			   enough to cover the majority of the drawing canvas.
#			   
# Author: Kevin Rivera, DataFlair website
# Version: 1.0
# Date: 10-16-2020
# ELE 547 Assignment 3

from keras.models import load_model
from tkinter import *
import tkinter as tk
#from PIL import Image
import pyscreenshot as ImageGrab
import numpy as np

model = load_model('mnist.h5')
#model = load_model('mnist.sig')


def predict_digit(img):
    #resize image to 28x28 pixels
    img = img.resize((28,28))
    #convert rgb to grayscale
    img = img.convert('L')
    img = np.array(img)
    #reshaping to support our model input and normalizing
    img = img.reshape(1,28,28,1)
    img = 1-(img/255.0)
    #predicting the class
    res = model.predict([img])[0]
    return np.argmax(res), max(res)
class App(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.x = self.y = 0
        # Creating elements
        self.canvas = tk.Canvas(self, width=300, height=300, bg = 'white', cursor="cross")
        self.label = tk.Label(self, text="Thinking..", font=("Helvetica", 48))
        self.classify_btn = tk.Button(self, text = "Recognise", command = self.classify_handwriting) 
        self.button_clear = tk.Button(self, text = "Clear", command = self.clear_all)
        # Grid structure
        self.canvas.grid(row=0, column=0, pady=2, sticky=W, )
        self.label.grid(row=0, column=1,pady=2, padx=2)
        self.classify_btn.grid(row=1, column=1, pady=2, padx=2)
        self.button_clear.grid(row=1, column=0, pady=2)
        #self.canvas.bind("<Motion>", self.start_pos)
        self.canvas.bind("<B1-Motion>", self.draw_lines)
    def clear_all(self):
        self.canvas.delete("all")
    def classify_handwriting(self):
		#Utilizing the tkinter built in tools to get the drawing canvas window information.
        box = (self.canvas.winfo_rootx(), self.canvas.winfo_rooty(), self.canvas.winfo_rootx() + self.canvas.winfo_width(), self.canvas.winfo_rooty() + self.canvas.winfo_height())
        im = ImageGrab.grab(bbox = box)
        digit, acc = predict_digit(im)
        self.label.configure(text= str(digit)+', '+ str(int(acc*100))+'%')
    def draw_lines(self, event):
        self.x = event.x
        self.y = event.y
        r=8
        self.canvas.create_oval(self.x-r, self.y-r, self.x + r, self.y + r, fill='black')
app = App()
mainloop()