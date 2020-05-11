# #For Python 2.6
# import tkinter as tk

# #Globals
# lastx, lasty = 0, 0

# #Definitions
# def xy(event):
#     global lastx, lasty
#     lastx, lasty = event.x, event.y

# def addLine(event):
#     global lastx, lasty
#     canvas.create_line((lastx, lasty, event.x, event.y))
#     lastx, lasty = event.x, event.y

# #Root Create + Setup
# root = tk.Tk()
# root.columnconfigure(0, weight=1)
# root.rowconfigure(0, weight=1)

# #Canvas Create + Setup
# canvas = tk.Canvas(root)
# canvas.grid(column=0, row=0, sticky="NSEW")
# canvas.bind("<Button-1>", xy)
# canvas.bind("<B1-Motion>", addLine)

# #Main Loop
# root.mainloop()

import tkinter as tk

"""paint.py: not exactly a paint program.. just a smooth line drawing demo."""

b1 = "up"
xold, yold = None, None

def main():
    root = tk.Tk()
    drawing_area = tk.Canvas(root)
    drawing_area.pack()
    drawing_area.bind("<Motion>", motion)
    drawing_area.bind("<ButtonPress-1>", b1down)
    drawing_area.bind("<ButtonRelease-1>", b1up)
    root.mainloop()

def b1down(event):
    global b1
    b1 = "down"           # you only want to draw when the button is down
                          # because "Motion" events happen -all the time-

def b1up(event):
    global b1, xold, yold
    b1 = "up"
    xold = None           # reset the line when you let go of the button
    yold = None

def motion(event):
    if b1 == "down":
        global xold, yold
        if xold is not None and yold is not None:
            event.widget.create_line(xold,yold,event.x,event.y,smooth='true')
                          # here's where you draw it. smooth. neat.
        xold = event.x
        yold = event.y

if __name__ == "__main__":
    main()