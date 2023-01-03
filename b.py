from tkinter import *
import webbrowser

ws = Tk()
ws.title('PythonGuides')
ws.geometry('500x400')


new = 1
url = "https://www.pythonguides.com"

def openbrowser():
    webbrowser.open(url, new=new)

bg = PhotoImage(file = '2.png')

canvas = Canvas(
	ws,
	width = 500,
	height = 400
	)

canvas.pack(fill='both', expand = True)

canvas.create_image(
	0,
	0,
	image=bg,
	anchor = "nw"
	)

canvas.create_text(
	250,
	150,
	text = 'PythonGuides',
	font=('Arial', 50),
	)

btn = Button(
	ws,
	text = 'EXPLORE MORE',
	command=openbrowser,
	width=20,
	height=2,
	relief=SOLID,
	font=('arial', 18)
	)

btn_canvas = canvas.create_window(
	100,
	200,
	anchor = "nw",
	window = btn,
	)


ws.mainloop()