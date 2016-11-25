#Resources:

#http://sebsauvage.net/python/gui/#import
#http://effbot.org/tkinterbook/canvas.htm
#https://www.tutorialspoint.com/python/tk_pack.htm
#http://stackoverflow.com/questions/11980812/how-do-you-create-a-button-on-a-tkinter-canvas
    #atomicinf

#The purpose of this script is to act as the GUI for a suduko game

import tkinter




class sudokuGUI(tkinter.Tk):
    def __init__ (self, parent):
        tkinter.Tk.__init__(self,parent)
        self.parent = parent
        self.initialize()

    def initialize(self):
        Bframe = tkinter.Frame(self)
        Bframe.pack(side = "right")

        # bottomframe = tkinter.Frame(self)
        # bottomframe.pack()


        newButton = tkinter.Button(Bframe, text="New Game", command = self.buttonClick("new"))
        newButton.pack()

        rButton = tkinter.Button(Bframe, text="Rules", command = self.buttonClick("rules"))
        rButton.pack()

        hButton = tkinter.Button(Bframe, text="Hint !", command = self.buttonClick("hint"))
        hButton.pack()

        sButton = tkinter.Button(Bframe, text="Solve", command = self.buttonClick("solve"))
        sButton.pack()

    #     #create a frame to hold the canvas
        CFrame = tkinter.Frame(self)
        CFrame.pack(side = "left")
    #     GFrame = tkinter.Frame(self)
    #
    #
         #create the canvas
        grid = tkinter.Canvas(CFrame,bg = "black", bd = 8, cursor = "arrow", relief = "raised", height = 630, width = 630)
        grid.pack()

        #draw horizontal lines on the canvas
        linewidth = 5
        grid.create_rectangle(10, 10, 641, 641, fill = "white")

        grid.create_line(10,80,641,80)
        grid.create_line(10, 150, 641, 150)
        grid.create_line(10, 220, 641, 220, width = linewidth)
        grid.create_line(10, 290, 641, 290)
        grid.create_line(10, 360, 641, 360)
        grid.create_line(10, 430, 641, 430, width = linewidth)
        grid.create_line(10, 500, 641, 500)
        grid.create_line(10, 570, 641, 570)

        #draw vertical lines on the canvas
        grid.create_line(80, 10, 80, 641)
        grid.create_line(150, 10, 150, 641)
        grid.create_line(220, 10, 220, 641, width = linewidth)
        grid.create_line(290, 10, 290, 641)
        grid.create_line(360, 10, 360, 641)
        grid.create_line(430, 10, 430, 641, width = linewidth)
        grid.create_line(500, 10, 500, 641)
        grid.create_line(570, 10, 570, 641)

        self.createInputBoxes(grid)

    def createInputBoxes(self, window):
        #create user input boxes on each grid box
        grid = window

        e1_1 = tkinter.Entry(self, width = 4, bg = "red", relief = "flat", font = 70, readonlybackground = "grey",
                                 justify = "center" )
        e2_1 = tkinter.Entry(self, width = 4, bg = "red", relief = "flat", font = 70, readonlybackground = "grey",
                                 justify = "center" )
        e3_1 = tkinter.Entry(self, width = 4, bg = "red", relief = "flat", font = 70, readonlybackground = "grey",
                                 justify = "center" )
        e4_1 = tkinter.Entry(self, width = 4, bg = "red", relief = "flat", font = 70, readonlybackground = "grey",
                                 justify = "center" )
        e5_1 = tkinter.Entry(self, width = 4, bg = "red", relief = "flat", font = 70, readonlybackground = "grey",
                                 justify = "center" )
        e6_1 = tkinter.Entry(self, width = 4, bg = "red", relief = "flat", font = 70, readonlybackground = "grey",
                                 justify = "center" )
        e7_1 = tkinter.Entry(self, width = 4, bg = "red", relief = "flat", font = 70, readonlybackground = "grey",
                                 justify = "center" )
        e8_1 = tkinter.Entry(self, width = 4, bg = "red", relief = "flat", font = 70, readonlybackground = "grey",
                                 justify = "center" )
        e9_1 = tkinter.Entry(self, width = 4, bg = "red", relief = "flat", font = 70, readonlybackground = "grey",
                                 justify = "center" )
        e1_2 = tkinter.Entry(self, width = 4, bg = "red", relief = "flat", font = 70, readonlybackground = "grey",
                                 justify = "center" )
        e2_2 = tkinter.Entry(self, width = 4, bg = "red", relief = "flat", font = 70, readonlybackground = "grey",
                                 justify = "center" )
        e3_2 = tkinter.Entry(self, width = 4, bg = "red", relief = "flat", font = 70, readonlybackground = "grey",
                                 justify = "center" )
        e4_2 = tkinter.Entry(self, width = 4, bg = "red", relief = "flat", font = 70, readonlybackground = "grey",
                                 justify = "center" )
        e5_2 = tkinter.Entry(self, width = 4, bg = "red", relief = "flat", font = 70, readonlybackground = "grey",
                                 justify = "center" )
        e6_2 = tkinter.Entry(self, width = 4, bg = "red", relief = "flat", font = 70, readonlybackground = "grey",
                                 justify = "center" )
        e7_2 = tkinter.Entry(self, width = 4, bg = "red", relief = "flat", font = 70, readonlybackground = "grey",
                                 justify = "center" )
        e8_2 = tkinter.Entry(self, width = 4, bg = "red", relief = "flat", font = 70, readonlybackground = "grey",
                                 justify = "center" )
        e9_2 = tkinter.Entry(self, width = 4, bg = "red", relief = "flat", font = 70, readonlybackground = "grey",
                                 justify = "center" )
        e1_3 = tkinter.Entry(self, width = 4, bg = "red", relief = "flat", font = 70, readonlybackground = "grey",
                                 justify = "center" )
        e2_3 = tkinter.Entry(self, width = 4, bg = "red", relief = "flat", font = 70, readonlybackground = "grey",
                                 justify = "center" )
        e3_3 = tkinter.Entry(self, width = 4, bg = "red", relief = "flat", font = 70, readonlybackground = "grey",
                                 justify = "center" )
        e4_3 = tkinter.Entry(self, width = 4, bg = "red", relief = "flat", font = 70, readonlybackground = "grey",
                                 justify = "center" )
        e5_3 = tkinter.Entry(self, width = 4, bg = "red", relief = "flat", font = 70, readonlybackground = "grey",
                                 justify = "center" )
        e6_3 = tkinter.Entry(self, width = 4, bg = "red", relief = "flat", font = 70, readonlybackground = "grey",
                                 justify = "center" )
        e7_3 = tkinter.Entry(self, width = 4, bg = "red", relief = "flat", font = 70, readonlybackground = "grey",
                                 justify = "center" )
        e8_3 = tkinter.Entry(self, width = 4, bg = "red", relief = "flat", font = 70, readonlybackground = "grey",
                                 justify = "center" )
        e9_3 = tkinter.Entry(self, width = 4, bg = "red", relief = "flat", font = 70, readonlybackground = "grey",
                                 justify = "center" )
        e1_4 = tkinter.Entry(self, width = 4, bg = "red", relief = "flat", font = 70, readonlybackground = "grey",
                                 justify = "center" )
        e2_4 = tkinter.Entry(self, width = 4, bg = "red", relief = "flat", font = 70, readonlybackground = "grey",
                                 justify = "center" )
        e3_4 = tkinter.Entry(self, width = 4, bg = "red", relief = "flat", font = 70, readonlybackground = "grey",
                                 justify = "center" )
        e4_4 = tkinter.Entry(self, width = 4, bg = "red", relief = "flat", font = 70, readonlybackground = "grey",
                                 justify = "center" )
        e5_4 = tkinter.Entry(self, width = 4, bg = "red", relief = "flat", font = 70, readonlybackground = "grey",
                                 justify = "center" )
        e6_4 = tkinter.Entry(self, width = 4, bg = "red", relief = "flat", font = 70, readonlybackground = "grey",
                                 justify = "center" )
        e7_4 = tkinter.Entry(self, width = 4, bg = "red", relief = "flat", font = 70, readonlybackground = "grey",
                                 justify = "center" )
        e8_4 = tkinter.Entry(self, width = 4, bg = "red", relief = "flat", font = 70, readonlybackground = "grey",
                                 justify = "center" )
        e9_4 = tkinter.Entry(self, width = 4, bg = "red", relief = "flat", font = 70, readonlybackground = "grey",
                                 justify = "center" )
        e1_5 = tkinter.Entry(self, width = 4, bg = "red", relief = "flat", font = 70, readonlybackground = "grey",
                                 justify = "center" )
        e2_5 = tkinter.Entry(self, width = 4, bg = "red", relief = "flat", font = 70, readonlybackground = "grey",
                                 justify = "center" )
        e3_5 = tkinter.Entry(self, width = 4, bg = "red", relief = "flat", font = 70, readonlybackground = "grey",
                                 justify = "center" )
        e4_5 = tkinter.Entry(self, width = 4, bg = "red", relief = "flat", font = 70, readonlybackground = "grey",
                                 justify = "center" )
        e5_5 = tkinter.Entry(self, width = 4, bg = "red", relief = "flat", font = 70, readonlybackground = "grey",
                                 justify = "center" )
        e6_5 = tkinter.Entry(self, width = 4, bg = "red", relief = "flat", font = 70, readonlybackground = "grey",
                                 justify = "center" )
        e7_5 = tkinter.Entry(self, width = 4, bg = "red", relief = "flat", font = 70, readonlybackground = "grey",
                                 justify = "center" )
        e8_5 = tkinter.Entry(self, width = 4, bg = "red", relief = "flat", font = 70, readonlybackground = "grey",
                                 justify = "center" )
        e9_5 = tkinter.Entry(self, width = 4, bg = "red", relief = "flat", font = 70, readonlybackground = "grey",
                                 justify = "center" )
        e1_6 = tkinter.Entry(self, width = 4, bg = "red", relief = "flat", font = 70, readonlybackground = "grey",
                                 justify = "center" )
        e2_6 = tkinter.Entry(self, width = 4, bg = "red", relief = "flat", font = 70, readonlybackground = "grey",
                                 justify = "center" )
        e3_6 = tkinter.Entry(self, width = 4, bg = "red", relief = "flat", font = 70, readonlybackground = "grey",
                                 justify = "center" )
        e4_6 = tkinter.Entry(self, width = 4, bg = "red", relief = "flat", font = 70, readonlybackground = "grey",
                                 justify = "center" )
        e5_6 = tkinter.Entry(self, width = 4, bg = "red", relief = "flat", font = 70, readonlybackground = "grey",
                                 justify = "center" )
        e6_6 = tkinter.Entry(self, width = 4, bg = "red", relief = "flat", font = 70, readonlybackground = "grey",
                                 justify = "center" )
        e7_6 = tkinter.Entry(self, width = 4, bg = "red", relief = "flat", font = 70, readonlybackground = "grey",
                                 justify = "center" )
        e8_6 = tkinter.Entry(self, width = 4, bg = "red", relief = "flat", font = 70, readonlybackground = "grey",
                                 justify = "center" )
        e9_6 = tkinter.Entry(self, width = 4, bg = "red", relief = "flat", font = 70, readonlybackground = "grey",
                                 justify = "center" )
        e1_7 = tkinter.Entry(self, width = 4, bg = "red", relief = "flat", font = 70, readonlybackground = "grey",
                                 justify = "center" )
        e2_7 = tkinter.Entry(self, width = 4, bg = "red", relief = "flat", font = 70, readonlybackground = "grey",
                                 justify = "center" )
        e3_7 = tkinter.Entry(self, width = 4, bg = "red", relief = "flat", font = 70, readonlybackground = "grey",
                                 justify = "center" )
        e4_7 = tkinter.Entry(self, width = 4, bg = "red", relief = "flat", font = 70, readonlybackground = "grey",
                                 justify = "center" )
        e5_7 = tkinter.Entry(self, width = 4, bg = "red", relief = "flat", font = 70, readonlybackground = "grey",
                                 justify = "center" )
        e6_7 = tkinter.Entry(self, width = 4, bg = "red", relief = "flat", font = 70, readonlybackground = "grey",
                                 justify = "center" )
        e7_7 = tkinter.Entry(self, width = 4, bg = "red", relief = "flat", font = 70, readonlybackground = "grey",
                                 justify = "center" )
        e8_7 = tkinter.Entry(self, width = 4, bg = "red", relief = "flat", font = 70, readonlybackground = "grey",
                                 justify = "center" )
        e9_7 = tkinter.Entry(self, width = 4, bg = "red", relief = "flat", font = 70, readonlybackground = "grey",
                                 justify = "center" )
        e1_8 = tkinter.Entry(self, width = 4, bg = "red", relief = "flat", font = 70, readonlybackground = "grey",
                                 justify = "center" )
        e2_8 = tkinter.Entry(self, width = 4, bg = "red", relief = "flat", font = 70, readonlybackground = "grey",
                                 justify = "center" )
        e3_8 = tkinter.Entry(self, width = 4, bg = "red", relief = "flat", font = 70, readonlybackground = "grey",
                                 justify = "center" )
        e4_8 = tkinter.Entry(self, width = 4, bg = "red", relief = "flat", font = 70, readonlybackground = "grey",
                                 justify = "center" )
        e5_8 = tkinter.Entry(self, width = 4, bg = "red", relief = "flat", font = 70, readonlybackground = "grey",
                                 justify = "center" )
        e6_8 = tkinter.Entry(self, width = 4, bg = "red", relief = "flat", font = 70, readonlybackground = "grey",
                                 justify = "center" )
        e7_8 = tkinter.Entry(self, width = 4, bg = "red", relief = "flat", font = 70, readonlybackground = "grey",
                                 justify = "center" )
        e8_8 = tkinter.Entry(self, width = 4, bg = "red", relief = "flat", font = 70, readonlybackground = "grey",
                                 justify = "center" )
        e9_8 = tkinter.Entry(self, width = 4, bg = "red", relief = "flat", font = 70, readonlybackground = "grey",
                                 justify = "center" )
        e1_9 = tkinter.Entry(self, width = 4, bg = "red", relief = "flat", font = 70, readonlybackground = "grey",
                                 justify = "center" )
        e2_9 = tkinter.Entry(self, width = 4, bg = "red", relief = "flat", font = 70, readonlybackground = "grey",
                                 justify = "center" )
        e3_9 = tkinter.Entry(self, width = 4, bg = "red", relief = "flat", font = 70, readonlybackground = "grey",
                                 justify = "center" )
        e4_9 = tkinter.Entry(self, width = 4, bg = "red", relief = "flat", font = 70, readonlybackground = "grey",
                                 justify = "center" )
        e5_9 = tkinter.Entry(self, width = 4, bg = "red", relief = "flat", font = 70, readonlybackground = "grey",
                                 justify = "center" )
        e6_9 = tkinter.Entry(self, width = 4, bg = "red", relief = "flat", font = 70, readonlybackground = "grey",
                                 justify = "center" )
        e7_9 = tkinter.Entry(self, width = 4, bg = "red", relief = "flat", font = 70, readonlybackground = "grey",
                                 justify = "center" )
        e8_9 = tkinter.Entry(self, width = 4, bg = "red", relief = "flat", font = 70, readonlybackground = "grey",
                                 justify = "center" )
        e9_9 = tkinter.Entry(self, width = 4, bg = "red", relief = "flat", font = 70, readonlybackground = "grey",
                                 justify = "center" )





        grid.create_window(20, 30, anchor= "nw", window=e1_1)
        grid.create_window(90, 30, anchor="nw", window=e2_1)
        grid.create_window(160, 30, anchor="nw", window=e3_1)
        grid.create_window(230, 30, anchor="nw", window=e4_1)
        grid.create_window(300, 30, anchor="nw", window=e5_1)
        grid.create_window(370, 30, anchor="nw", window=e6_1)
        grid.create_window(440, 30, anchor="nw", window=e7_1)
        grid.create_window(510, 30, anchor="nw", window=e8_1)
        grid.create_window(580, 30, anchor="nw", window=e9_1)

        grid.create_window(20, 100, anchor="nw", window=e1_2)
        grid.create_window(90, 100, anchor="nw", window=e2_2)
        grid.create_window(160, 100, anchor="nw", window=e3_2)
        grid.create_window(230, 100, anchor="nw", window=e4_2)
        grid.create_window(300, 100, anchor="nw", window=e5_2)
        grid.create_window(370, 100, anchor="nw", window=e6_2)
        grid.create_window(440, 100, anchor="nw", window=e7_2)
        grid.create_window(510, 100, anchor="nw", window=e8_2)
        grid.create_window(580, 100, anchor="nw", window=e9_2)

        grid.create_window(20, 170, anchor="nw", window=e1_3)
        grid.create_window(90, 170, anchor="nw", window=e2_3)
        grid.create_window(160, 170, anchor="nw", window=e3_3)
        grid.create_window(230, 170, anchor="nw", window=e4_3)
        grid.create_window(300, 170, anchor="nw", window=e5_3)
        grid.create_window(370, 170, anchor="nw", window=e6_3)
        grid.create_window(440, 170, anchor="nw", window=e7_3)
        grid.create_window(510, 170, anchor="nw", window=e8_3)
        grid.create_window(580, 170, anchor="nw", window=e9_3)

        grid.create_window(20, 240, anchor="nw", window=e1_4)
        grid.create_window(90, 240, anchor="nw", window=e2_4)
        grid.create_window(160, 240, anchor="nw", window=e3_4)
        grid.create_window(230, 240, anchor="nw", window=e4_4)
        grid.create_window(300, 240, anchor="nw", window=e5_4)
        grid.create_window(370, 240, anchor="nw", window=e6_4)
        grid.create_window(440, 240, anchor="nw", window=e7_4)
        grid.create_window(510, 240, anchor="nw", window=e8_4)
        grid.create_window(580, 240, anchor="nw", window=e9_4)

        grid.create_window(20, 310, anchor="nw", window=e1_5)
        grid.create_window(90, 310, anchor="nw", window=e2_5)
        grid.create_window(160, 310, anchor="nw", window=e3_5)
        grid.create_window(230, 310, anchor="nw", window=e4_5)
        grid.create_window(300, 310, anchor="nw", window=e5_5)
        grid.create_window(370, 310, anchor="nw", window=e6_5)
        grid.create_window(440, 310, anchor="nw", window=e7_5)
        grid.create_window(510, 310, anchor="nw", window=e8_5)
        grid.create_window(580, 310, anchor="nw", window=e9_5)

        grid.create_window(20, 380, anchor="nw", window=e1_6)
        grid.create_window(90, 380, anchor="nw", window=e2_6)
        grid.create_window(160, 380, anchor="nw", window=e3_6)
        grid.create_window(230, 380, anchor="nw", window=e4_6)
        grid.create_window(300, 380, anchor="nw", window=e5_6)
        grid.create_window(370, 380, anchor="nw", window=e6_6)
        grid.create_window(440, 380, anchor="nw", window=e7_6)
        grid.create_window(510, 380, anchor="nw", window=e8_6)
        grid.create_window(580, 380, anchor="nw", window=e9_6)

        grid.create_window(20, 450, anchor="nw", window=e1_7)
        grid.create_window(90, 450, anchor="nw", window=e2_7)
        grid.create_window(160, 450, anchor="nw", window=e3_7)
        grid.create_window(230, 450, anchor="nw", window=e4_7)
        grid.create_window(300, 450, anchor="nw", window=e5_7)
        grid.create_window(370, 450, anchor="nw", window=e6_7)
        grid.create_window(440, 450, anchor="nw", window=e7_7)
        grid.create_window(510, 450, anchor="nw", window=e8_7)
        grid.create_window(580, 450, anchor="nw", window=e9_7)

        grid.create_window(20, 520, anchor="nw", window=e1_8)
        grid.create_window(90, 520, anchor="nw", window=e2_8)
        grid.create_window(160, 520, anchor="nw", window=e3_8)
        grid.create_window(230, 520, anchor="nw", window=e4_8)
        grid.create_window(300, 520, anchor="nw", window=e5_8)
        grid.create_window(370, 520, anchor="nw", window=e6_8)
        grid.create_window(440, 520, anchor="nw", window=e7_8)
        grid.create_window(510, 520, anchor="nw", window=e8_8)
        grid.create_window(580, 520, anchor="nw", window=e9_8)

        grid.create_window(20, 590, anchor="nw", window=e1_9)
        grid.create_window(90, 590, anchor="nw", window=e2_9)
        grid.create_window(160, 590, anchor="nw", window=e3_9)
        grid.create_window(230, 590, anchor="nw", window=e4_9)
        grid.create_window(300, 590, anchor="nw", window=e5_9)
        grid.create_window(370, 590, anchor="nw", window=e6_9)
        grid.create_window(440, 590, anchor="nw", window=e7_9)
        grid.create_window(510, 590, anchor="nw", window=e8_9)
        grid.create_window(580, 590, anchor="nw", window=e9_9)



    def buttonClick(self, button):
        if button is "new":
            pass
            # game.newGame
            #self.initialize

        elif button is "rules":
            pass
            #self.print(game.rules)
        elif button is "hint":
            pass
            #self.fill(game.hint)
        elif button is "solve":
            pass
            #self.fill(game.solve)








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
    app = sudokuGUI(None)
    app.title('sudoku player 1.0')




    app.mainloop()
