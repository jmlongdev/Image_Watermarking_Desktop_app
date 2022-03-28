from tkinter import *
from tkinter import filedialog as fd
from tkinter.filedialog import asksaveasfile, SaveAs
from PIL import ImageTk, Image, ImageFont, ImageDraw

global image_marked, imageTk

window = Tk()
window.title("Image Watermarking Tool")
window.config(padx=0, pady=0, bg='#c0c0c0')
window.geometry('600x600')
window.maxsize(900, 900)

frame = Frame(window, bg='#a0c0c0')
frame.config()
frame.place(relx=.5, rely=.5, anchor=CENTER, relheight=1, relwidth=1)

# Close Application
my_menu = Menu(window)
window.config(menu=my_menu)


# functions


def add_image():
    global image_label, image_tk

    # opens and creates an ImageTk.PhotoImage object
    path = fd.askopenfilename()
    image_tk = ImageTk.PhotoImage(Image.open(path))

    # displays the image
    image_label = Label(frame, image=image_tk)
    image_label.photo = image_tk
    image_label.place(relx=.5, rely=.5, anchor=CENTER)


def clear_image():
    image_label.destroy()
    image_label_2.destroy()


def add_text():
    global image_label_2, watermark_img
    # Becomes an Image object again
    watermark_img = ImageTk.getimage(image_tk)
    width, height = watermark_img.size
    draw = ImageDraw.Draw(watermark_img)
    text = "sample watermark"
    text_font = ImageFont.load_default()
    textwidth, textheight = draw.textsize(text, text_font)
    margin = 10
    x = width - textwidth - margin
    y = height - textheight - margin
    draw.text((x, y), text, font=text_font)

    # image saves with watermark but need to be able to see the watermark first before saving. also,
    # the clear button doesn't clear the watermarked image

    # file = asksaveasfile(mode='wb', defaultextension=".png")
    # if file:
    #     watermark_img.save(file)

    watermarked_image = ImageTk.PhotoImage(watermark_img)

    image_label_2 = Label(frame, image=watermarked_image)
    image_label_2.photo = watermarked_image
    image_label_2.place(relx=.5, rely=.5, anchor=CENTER)

    # edit_image.text((150, 300), text_to_add, ('red'), font=text_font)


def save():
    # file = asksaveasfile(mode='wb', defaultextension=".png")
    # if file:
    #     imgpil = ImageTk.getimage(imageTk)
    #     imgpil.save(file)
    file = asksaveasfile(mode='wb', defaultextension=".png")
    if file:
        watermark_img.save(file)



def add_watermark():
    pass
    path = fd.askopenfilename()
    watermark = ImageTk.PhotoImage(Image.open(path))



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
add_logo = Button(frame, text="Add Logo", command=add_watermark)
add_logo.place(relx=.6, rely=.1, anchor=CENTER)

#text box
text_box = Entry(window, font=('Helvetica', 20))
text_box.place(relx=.5, rely=.82, anchor=CENTER)
window.mainloop()