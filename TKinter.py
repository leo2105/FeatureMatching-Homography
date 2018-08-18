from tkinter import *
from PIL import Image, ImageTk
import cv2
import numpy as np

H_low, S_low, V_low = 0, 100, 100
H_high, S_high, V_high = 10, 255, 255

load = Image.open('containers1.jpg').resize((300,400))

class Window(Frame):
    
    def __init__(self, master = None):
        Frame.__init__(self, master)
        self.master = master   
        self.init_window()
    
    def init_window(self):
        self.master.title('GUI')
        self.pack(fill=BOTH, expand=1)
        
        leftButton1_low = Button(self, text='Less H', command=combine_funcs(self.showImg, self.lessHlow))
        leftButton1_low.place(x=100, y=500)
        rightButton1_low = Button(self, text='More H', command=combine_funcs(self.showImg, self.moreHlow))
        rightButton1_low.place(x=250, y=500)
        leftButton2_low = Button(self, text='Less S', command=combine_funcs(self.showImg, self.lessSlow))
        leftButton2_low.place(x=100, y=550)
        rightButton2_low = Button(self, text='More S', command=combine_funcs(self.showImg, self.moreSlow))
        rightButton2_low.place(x=250, y=550)
        leftButton3_low = Button(self, text='Less V', command=combine_funcs(self.showImg, self.lessVlow))
        leftButton3_low.place(x=100, y=600)
        rightButton3_low = Button(self, text='More V', command=combine_funcs(self.showImg, self.moreVlow))
        rightButton3_low.place(x=250, y=600)
            
        leftButton1_high = Button(self, text='Less H', command=combine_funcs(self.showImg, self.lessHhigh))
        leftButton1_high.place(x=450, y=500)
        rightButton1_high = Button(self, text='More H', command=combine_funcs(self.showImg, self.moreHhigh))
        rightButton1_high.place(x=600, y=500)
        leftButton2_high = Button(self, text='Less S', command=combine_funcs(self.showImg, self.lessShigh))
        leftButton2_high.place(x=450, y=550)
        rightButton2_high = Button(self, text='More S', command=combine_funcs(self.showImg, self.moreShigh))
        rightButton2_high.place(x=600, y=550)
        leftButton3_high = Button(self, text='Less V', command=combine_funcs(self.showImg, self.lessVhigh))
        leftButton3_high.place(x=450, y=600)
        rightButton3_high = Button(self, text='More V', command=combine_funcs(self.showImg, self.moreVhigh))
        rightButton3_high.place(x=600, y=600)
        
        render = ImageTk.PhotoImage(load)
        img = Label(self, image=render)
        img.image = render
        img.place(x=375, y=50)
        
        #plot = Button(self, text='Image', command=self.showImg)
        #plot.place(x=350, y=470)
        
        #menu = Menu(self.master)
        #self.master.config(menu=menu)
        
        #file = Menu(menu)
        #file.add_command(label="Save", command=self.client_exit)
        #file.add_command(label="Exit", command=self.destroy)
        #menu.add_cascade(label='File', menu=file)
        
        #edit = Menu(menu)
        #edit.add_command(label='Show Image', command=self.plotImage())
        #edit.add_command(label='Show Text', command=self.showTxt)
        #menu.add_cascade(label='Edit', menu=edit)
        
    def client_exit(self):
        Frame.destroy()
        
    def showImg(self):        
        cv2_im = cv2.imread('containers1.jpg')
        cv2_im = cv2.resize(cv2_im, (300,400))
        hsv = cv2.cvtColor(cv2_im,cv2.COLOR_BGR2HSV)
        ###
        lower_blue = np.array([H_low,S_low,V_low])
        upper_blue = np.array([H_high,S_high,V_high])
        
        mask = cv2.inRange(hsv, lower_blue, upper_blue)
        cv2_im = cv2.bitwise_and(cv2_im,cv2_im, mask= mask)     
        ###
        pil_im = Image.fromarray(cv2_im)
        
        render = ImageTk.PhotoImage(pil_im)
        img = Label(self, image=render)
        img.image = render
        img.place(x=75, y=50)
        
    def plotImage(self):
        load = Image.open('containers1.jpg').resize((300,400))
        render = ImageTk.PhotoImage(load)
        
        
    def showTxt(self):
        text = Label(self, text='HSV Colorspace!')
        text.pack()
        
    ## Low Boundaries
        
    def lessHlow(self):
        text = Label(self)
        text.pack()
        text.place(x=200,y=500)
        dec_label_H_low(text) 
        showImg(self)
        
    def moreHlow(self):
        text = Label(self)
        text.pack()
        text.place(x=200,y=500)
        inc_label_H_low(text)
        
    def lessSlow(self):
        text = Label(self)
        text.pack()
        text.place(x=200,y=550)
        dec_label_S_low(text)
             
    def moreSlow(self):
        text = Label(self)
        text.pack()
        text.place(x=200,y=550)
        inc_label_S_low(text)
        
    def lessVlow(self):
        text = Label(self)
        text.pack()
        text.place(x=200,y=600)
        dec_label_V_low(text)
        
    def moreVlow(self):
        text = Label(self)
        text.pack()
        text.place(x=200,y=600)
        inc_label_V_low(text)
        
    ## High Boundaries
    
    def lessHhigh(self):
        text = Label(self)
        text.pack()
        text.place(x=550,y=500)
        dec_label_H_high(text) 
        
    def moreHhigh(self):
        text = Label(self)
        text.pack()
        text.place(x=550,y=500)
        inc_label_H_high(text)
        
    def lessShigh(self):
        text = Label(self)
        text.pack()
        text.place(x=550,y=550)
        dec_label_S_high(text)
             
    def moreShigh(self):
        text = Label(self)
        text.pack()
        text.place(x=550,y=550)
        inc_label_S_high(text)
        
    def lessVhigh(self):
        text = Label(self)
        text.pack()
        text.place(x=550,y=600)
        dec_label_V_high(text)
        
    def moreVhigh(self):
        text = Label(self)
        text.pack()
        text.place(x=550,y=600)
        inc_label_V_high(text)
   
## Low Boundaries

def dec_label_H_low(label):
    def count():
        global H_low
        H_low = min(max(0, H_low-1), H_high)
        label.config(text=str(H_low))
        label.after(func=count)
    count()
    
def inc_label_H_low(label):
    def count():
        global H_low
        H_low = min(min(255, H_low+1), H_high)
        label.config(text=str(H_low))
        label.after(func=count)
    count()

def dec_label_S_low(label):
    def count():
        global S_low
        S_low = min(max(0, S_low-1), S_high)
        label.config(text=str(S_low))
        label.after(func=count)
    count()
    
def inc_label_S_low(label):
    def count():
        global S_low
        S_low = min(min(255, S_low+1), S_high)
        label.config(text=str(S_low))
        label.after(func=count)
    count()
    
def dec_label_V_low(label):
    def count():
        global V_low
        V_low = min(max(0, V_low-1), V_high)
        label.config(text=str(V_low))
        label.after(func=count)
    count()
    
def inc_label_V_low(label):
    def count():
        global V_low
        V_low = min(min(255, V_low+1), V_high)
        label.config(text=str(V_low))
        label.after(func=count)
    count()

## High Boundaries

def dec_label_H_high(label):
    def count():
        global H_high
        H_high = max(max(0, H_high-1), H_low)
        label.config(text=str(H_high))
        label.after(func=count)
    count()
    
def inc_label_H_high(label):
    def count():
        global H_high
        H_high = max(min(255, H_high+1), H_low)
        label.config(text=str(H_high))
        label.after(func=count)
    count()

def dec_label_S_high(label):
    def count():
        global S_high
        S_high = max(max(0, S_high-1), S_low)
        label.config(text=str(S_high))
        label.after(func=count)
    count()
    
def inc_label_S_high(label):
    def count():
        global S_high
        S_high = max(min(255, S_high+1), S_low)
        label.config(text=str(S_high))
        label.after(func=count)
    count()
    
def dec_label_V_high(label):
    def count():
        global V_high
        V_high = max(max(0, V_high-1), V_low)
        label.config(text=str(V_high))
        label.after(func=count)
    count()
    
def inc_label_V_high(label):
    def count():
        global V_high
        V_high = max(min(255, V_high+1), V_low)
        label.config(text=str(V_high))
        label.after(func=count)
    count()
    
def combine_funcs(*funcs):
    def combined_func(*args, **kwargs):
        for f in funcs:
            f(*args, **kwargs)
    return combined_func

root = Tk()
root.geometry("750x700")
app = Window(root)
root.mainloop()
