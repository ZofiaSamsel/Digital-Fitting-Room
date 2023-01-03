from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog
import tkinter.font as font
from utils.image import FashionPoseImage
import cv2
from base import run_outfit, run_outfit1

#CREATING WINDOW
root = Tk()
root.title('Fashion App')
#root.iconbitmap("images_gui/bone.png")
root.geometry("800x800")


#DEFINING A BACKGROUND
background = PhotoImage(file = "images/bg.png")
background_label = Label(root, image=background)
#PLACING A BACKGROUND INTO ROOT (MAIN WINDOW)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

#DEFINING A FONT
buttonFont = font.Font(family='Arcus', size=12, weight='bold')


#FUNCTION THAT DEFINES A BUTTON THAT OPENS A PNG FILE FROM A HARD DRIVE
def open_a_file():
    global img_open_a_file #must be global, cause otherwise won't work
    #OPEN A PNG FILE FROM A HARD DRIVE
    root.filename = filedialog.askopenfilename(initialdir="/documents", title="select a file", filetypes=[("png files", ".png")])
    label_open_a_file = Label(root, text=root.filename)
    label_open_a_file.pack()
    img_open_a_file = ImageTk.PhotoImage(Image.open(root.filename))
    img_open_a_file_label = Label(image=img_open_a_file)
    #PLACING A widget INTO ROOT (MAIN WINDOW)
    img_open_a_file_label.pack()

#BUTTON THAT CALLS A FUNCTION THAT OPENS A FILE FROM A HARD DRIVE
button_open_a_file = Button(root, text="Open File", bg='#c5bae2', bd=0, font=buttonFont, command=open_a_file)
#PLACING A BUTTON INTO ROOT (MAIN WINDOW)
button_open_a_file.place(x=400, y=700)


#FUNCTION THAT DEFINES A BUTTON THAT OPENS A NEW WINDOW WITH A SKELETON + BG PHOTO
def load_skeleton(outfit):
    global imgtk, img
    frame = LabelFrame(root)
    frame.pack
    label = Label(root)
    label.pack()
    img = Image.fromarray(run_outfit(outfit))
    imgtk = ImageTk.PhotoImage(image=img)
    label.configure(image=imgtk)
    label.after(20, load_skeleton())
    
#FUNCTION THAT DEFINES A BUTTON THAT OPENS A NEW WINDOW WITH A SKELETON + BG GIF
def load_skeleton1(outfit):
    global imgtk, img
    frame = LabelFrame(root)
    frame.pack
    label = Label(root)
    label.pack()
    img = Image.fromarray(run_outfit1(outfit))
    imgtk = ImageTk.PhotoImage(image=img)
    label.configure(image=imgtk)
    label.after(20, load_skeleton())


#CREATING A NEW FRAME WITH OPTIONS - OUTFIT+GIF BACKGROUND
def choose_outfits():
    #NEW FRAME
    frame1 = LabelFrame(root, text="  Choose outfit with gif  ", bg='#a78ce3', font=buttonFont)
    frame1.place(x=350, y=500)
    #BUTTON THAT OPENS WINDOW WITH SKELETON OUTFIT
    button_skeleton1 = Button(frame1, text="skeleton", bg='#c5bae2', bd=0, font=buttonFont, command=lambda: load_skeleton(outfit='Skeleton'))
    #PLACING A BUTTON INTO ROOT (FRAME IN A MAIN WINDOW)
    button_skeleton1.pack(pady=5)
    #BUTTON THAT OPENS WINDOW WITH ASTRONAUT OUTFIT
    button_astronaut1 = Button(frame1, text="astronaut", bg='#c5bae2', bd=0, font=buttonFont, command=lambda: load_skeleton(outfit='Astronaut'))
    #PLACING A BUTTON INTO ROOT (FRAME IN A MAIN WINDOW)
    button_astronaut1.pack(pady=5)
    #BUTTON THAT OPENS WINDOW WITH JACKET OUTFIT
    button_jacket1 = Button(frame1, text="jacket", bg='#c5bae2', bd=0, font=buttonFont, command=lambda: load_skeleton(outfit='Jacket'))
    button_jacket1.pack(pady=5)
    #BUTTON THAT CLOSES WINDOW WITH OPTIONS (RETURNS TO THE MAIN MENU)
    button_background_gif_quit = Button(frame1, text="close", bg='#c5bae2', bd=0, font=buttonFont, command=frame1.destroy)
    #PLACING A BUTTON INTO ROOT (FRAME IN A MAIN WINDOW)
    button_background_gif_quit.pack(pady=5)
    #NEW FRAME
    frame2 = LabelFrame(root, text="Choose outfit with photo", bg='#a78ce3', font=buttonFont)
    frame2.place(x=550, y=500)
    #BUTTON THAT OPENS WINDOW WITH SKELETON OUTFIT
    button_skeleton2 = Button(frame2, text="skeleton", bg='#c5bae2', bd=0, font=buttonFont, command=lambda: load_skeleton1(outfit='Skeleton'))
    #PLACING A BUTTON INTO ROOT (FRAME IN A MAIN WINDOW)
    button_skeleton2.pack(pady=5)
    #BUTTON THAT OPENS WINDOW WITH ASTRONAUT OUTFIT
    button_astronaut2 = Button(frame2, text="astronaut", bg='#c5bae2', bd=0, font=buttonFont, command=lambda: load_skeleton1(outfit='Astronaut'))
    #PLACING A BUTTON INTO ROOT (FRAME IN A MAIN WINDOW)
    button_astronaut2.pack(pady=5)
    #BUTTON THAT OPENS WINDOW WITH JACKET OUTFIT
    button_jacket2 = Button(frame2, text="jacket", bg='#c5bae2', bd=0, font=buttonFont, command=lambda: load_skeleton1(outfit='Jacket'))
    button_jacket2.pack(pady=5)
    #BUTTON THAT CLOSES WINDOW WITH OPTIONS (RETURNS TO THE MAIN MENU)
    button_background_photo_quit = Button(frame2, text="close", bg='#c5bae2', bd=0, font=buttonFont, command=frame2.destroy)
    #PLACING A BUTTON INTO ROOT (FRAME IN A MAIN WINDOW)
    button_background_photo_quit.pack(pady=5)


#BUTTON THAT OPEN A WINDOW WITH OPTIONS (ALL AVAILABLE OUTFITS)
button_outfits = Button(root, text="Start by webcam", bg='#c5bae2', bd=0, font=buttonFont, command=choose_outfits)
#PLACING A BUTTON INTO ROOT (MAIN WINDOW)
button_outfits.place(x=500, y=700)


#BUTTON THAT QUITS PROGRAM
button_quit = Button(root, text="Exit", bg='#c5bae2', bd=0, font=buttonFont, command=root.quit)
#PLACING A BUTTON INTO ROOT (MAIN WINDOW)
button_quit.place(x=655, y=700)


root.mainloop()