from tkinter import *
from PIL import ImageTk, Image

root = Tk()

canv = Canvas(root, width=622, height=800, bg='white')
canv.grid(row=5, column=5)

img = ImageTk.PhotoImage(Image.open("containers1.jpg").resize((600, 800)))
canv.create_image(10, 10, anchor=NW, image=img)


mainloop()
