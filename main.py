from tkinter import *
from tkinter import filedialog as fd
from PIL import ImageTk, Image

window = Tk()
window.title("Image Watermarking Tool")
window.config(padx=0, pady=0, bg='#c0c0c0')
window.geometry('600x600')
window.maxsize(800, 800)

frame = Frame(window, bg='#a0c0c0')
frame.config()
frame.place(relx=.5, rely=.5, anchor=CENTER, relheight=1, relwidth=1)
# canvas = Canvas(frame, height=400, width=500)
# canvas.place(relx=.5, rely=.5, anchor=CENTER)

# Close Application
my_menu = Menu(window)
window.config(menu=my_menu)



# functions
def save():
    pass


def add_image():
    path = fd.askopenfilename()
    # filename
    image = ImageTk.PhotoImage(Image.open(path))
    my_image = Label(window, image=image)
    my_image.photo=image
    my_image.place(relx=.5, rely=.5, anchor=CENTER)
    # canvas.create_image(100, 100, image=image)
    # with Image.open(filename) as im:
    #     canvas.create_image(100, 100, image=im)

def clear_image():
    print('image cleared')


def add_text():
    print('text added')


def add_logo():
    print('logo added')


# Create menu item
file_menu = Menu(my_menu)
my_menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label='Save', command=save)
file_menu.add_separator()
file_menu.add_command(label='Close', command=window.quit)



# top row of buttons
add_image = Button(frame, text="Add Image", command=add_image)
add_image.place(relx=.4, rely=.9, anchor=CENTER)
clear_img = Button(frame, text="Clear", command=clear_image)
clear_img.place(relx=.6, rely=.9, anchor=CENTER)


# bottom row of buttons
add_button = Button(frame, text="Add Text", command=add_text)
add_button.place(relx=.4, rely=.1,anchor=CENTER)
add_logo = Button(frame, text="Add Logo", command=add_logo)
add_logo.place(relx=.6, rely=.1, anchor=CENTER)

window.mainloop()