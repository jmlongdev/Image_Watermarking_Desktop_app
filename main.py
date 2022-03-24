from tkinter import *
from tkinter import ttk
from PIL import ImageTk,Image

window = Tk()
window.title("Image Watermarking Tool")
window.config(padx=0, pady=0, bg='#c0c0c0')
window.geometry('400x400')

frame = Frame(window)
frame.pack()
# canvas = Canvas(width=400, heigh=400)
# canvas.grid(column=0, row=0)

# top row of buttons
add_image = Button(frame, text='Add Image')
add_image.grid(column=1, row=0)
clear_img = Button(frame,text='Clear')
clear_img.grid(column=2, row=0)


#bottom row of buttons
add_button = Button(frame, text="Add Text")
add_button.grid(column=1, row=2, pady=(325,0), padx=(0,0))
add_logo = Button(frame, text='Add Logo')
add_logo.grid(column=2, row=2, pady=(325,0))

# Close Application
close_button = Button(frame, text='Close App')
close_button.grid(column=0, row=0, padx=(0, 150), )

window.mainloop()