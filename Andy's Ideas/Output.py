#Resources:

#http://sebsauvage.net/python/gui/#import
#http://effbot.org/tkinterbook/canvas.htm
#https://www.tutorialspoint.com/python/tk_pack.htm

#The purpose of this script is to act as the GUI for a suduko game

import tkinter






class simpleapp_tk(tkinter.Tk):
    def __init__ (self, parent):
        tkinter.Tk.__init__(self,parent)
        self.parent = parent
        self.initialize()

    def initialize(self):
        Bframe = tkinter.Frame(self)
        Bframe.pack(side = "right")

        # bottomframe = tkinter.Frame(self)
        # bottomframe.pack()


        redbutton = tkinter.Button(Bframe, text="New Game")
        redbutton.pack()

        greenbutton = tkinter.Button(Bframe, text="Rules")
        greenbutton.pack()

        bluebutton = tkinter.Button(Bframe, text="Hint !")
        bluebutton.pack()

        blackbutton = tkinter.Button(Bframe, text="Solve")
        blackbutton.pack()

    #     #create a frame to hold the canvas
        CFrame = tkinter.Frame(self)
        CFrame.pack(side = "left")
    #     GFrame = tkinter.Frame(self)
    #
    #
         #create the canvas
        grid = tkinter.Canvas(CFrame,bg = "green", bd = 4, cursor = "arrow", relief = "ridge", height = 600, width = 600)
        grid.pack()

        #draw a grid on the canvas
        grid.create_line(x0, y0, x1, y1, ..., xn, yn, options)


    #
    #
    #    self.grid(CFrame)
    #
    #     self.entry = tkinter.Entry(self)
    #     self.entry.grid(column = 0, row = 0, sticky = 'EW')
    #
    #     #create user buttons
    #     #this button will bring up a window with rules for the game
    #     hB = tkinter.Button(self, text = u"Rules")
    #     hB.grid(column = 9, row = 4)
    #
    #     #this button will start a new game ie. initialize the game board
    #     newButton = tkinter.Button(self, text=u"New Game")
    #     newButton.grid(column=9, row=5)
    #
    #     #this button will give the player the next best available move
    #     hintButton = tkinter.Button(self, text = u"Hint!")
    #     hintButton.grid(column = 9, row = 6)
    #
    #     #this button will solve the puzzle and fill in all the empty boxes
    #     solveButton = tkinter.Button(self, text = u"Solve")
    #     solveButton.grid(column = 9, row = 7)
    #
    #
    #
    #
    #
    #     # These lines allow the columns to be resized along with window
    #     self.grid_columnconfigure(0,weight = 1)
    #     self.grid_columnconfigure(1, weight=1)
    #     self.grid_columnconfigure(2, weight=1)
    #     self.grid_columnconfigure(3, weight=1)
    #     self.grid_columnconfigure(4, weight=1)
    #     self.grid_columnconfigure(5, weight=1)
    #     self.grid_columnconfigure(6, weight=1)
    #     self.grid_columnconfigure(7, weight=1)
    #     self.grid_columnconfigure(8, weight=1)
    #     self.grid_columnconfigure(9, weight=1)
    #     self.grid_columnconfigure(10, weight=1)
    #
    #     #These lines allow the rows to be resized along with the window
    #     self.grid_rowconfigure(0,weight = 1)
    #     self.grid_rowconfigure(1, weight=1)
    #     self.grid_rowconfigure(2, weight=1)
    #     self.grid_rowconfigure(3, weight=1)
    #     self.grid_rowconfigure(4, weight=1)
    #     self.grid_rowconfigure(5, weight=1)
    #     self.grid_rowconfigure(6, weight=1)
    #     self.grid_rowconfigure(7, weight=1)
    #     self.grid_rowconfigure(8, weight=1)
    #     self.grid_rowconfigure(9, weight=1)
    #     self.grid_rowconfigure(10, weight=1)
    #
    #     label = tkinter.Label(self, anchor="w", fg="white", bg="red")
    #     label.grid(column=0, row=10, columnspan=10, sticky='EW')
    #
    # def outputLine(self, message):
    #     label = tkinter.Label(self, anchor = "w", fg = "black", bg = "white")
    #     label.grid(column = 0, row = 10, columnspan = 10, sticky = 'EW')

if __name__ == "__main__":
    app = simpleapp_tk(None)
    app.title('sudoku solver 1.0')
    app.mainloop()