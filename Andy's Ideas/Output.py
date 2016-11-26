#Resources:

#http://sebsauvage.net/python/gui/#import
#http://effbot.org/tkinterbook/canvas.htm
#https://www.tutorialspoint.com/python/tk_pack.htm
#http://stackoverflow.com/questions/11980812/how-do-you-create-a-button-on-a-tkinter-canvas
    #atomicinf

#The purpose of this script is to act as the GUI for a suduko game

import tkinter
#import sudoku.py

boxDictionary = {}
gridFrame = None
messageBox = None


Rules = "This is a simple soduku solver. Each red box accepts user input, each grey box is a value which was set initially by the game." \
             "The goal of the game is to fill each row, column, and 3X3 box with vlaues 1-9.  " \
            "To see an example, press 'New Game' followed by 'Solve'  " \
             "'New Game' will clear the board and start a new puzzle.  " \
             "''Hint !' will fill in the next best value in the grid.  " \
             "'Solve' will fill in the entire grid with the solution"







class sudokuGUI(tkinter.Tk):
    # boxDictionary = {}
    # ACanvas = None
    # Rules = "This is a simple soduku solver. Each red box accepts user input, each grey box is a value which was set initially by the game." \
    #         "The goal of the game is to fill each row, column, and 3X3 box with vlaues 1-9.  To see an example, press 'New Game' followed by 'Solve'" \
    #         "'New Game' will clear the board and start a new puzzle" \
    #         "''Hint !' will fill in the next best value in the grid" \
    #         "'Solve' will fill in the entire grid with the solution"


    #openBoxes = {}
    rulesPressed = False
    def __init__ (self, parent):
        tkinter.Tk.__init__(self,parent)
        self.parent = parent
        self.initialize()

    def initialize(self):


        Bframe = tkinter.Frame(self)
        Bframe.pack(side = "right")

        # bottomframe = tkinter.Frame(self)
        # bottomframe.pack()

        # create text box at bottom for displaying messages
        messageB = tkinter.Text(self, height = 10, width = 50, bg = "grey")
        messageB.pack(side="right")
        messageB.configure(wrap="word")


        newButton = tkinter.Button(Bframe, text="New Game", command = lambda: self.buttonClick("new", None))
        newButton.pack()

        rButton = tkinter.Button(Bframe, text="Rules", command=lambda: self.buttonClick("rules", messageB))
        rButton.pack()

        hiButton = tkinter.Button(Bframe, text="Hide Rules", command=lambda: self.buttonClick("hide", messageB))
        hiButton.pack()

        hButton = tkinter.Button(Bframe, text="Hint !", command = lambda: self.buttonClick("hint", None))
        hButton.pack()

        sButton = tkinter.Button(Bframe, text="Solve", command = lambda: self.buttonClick("solve", None))
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





        ACanvas = grid
        self.createInputBoxes(grid)
        #self.fill(game.boardstate)

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

        boxDictionary = {'A1':e1_1, 'A2': e2_1, 'A3': e3_1, 'A4': e4_1, 'A5': e5_1, 'A6': e6_1, 'A7': e7_1, 'A8': e8_1, 'A9': e9_1,
                         'B1':e1_2, 'B2': e2_2, 'B3': e3_2, 'B4': e4_2, 'B5': e5_2, 'B6': e6_2, 'B7': e7_2, 'B8': e8_2, 'B9': e9_2,
                         'C1':e1_3, 'C2': e2_3, 'C3': e3_3, 'C4': e4_3, 'C5': e5_3, 'C6': e6_3, 'C7': e7_3, 'C8': e8_3, 'C9': e9_3,
                         'D1':e1_4, 'D2': e2_4, 'D3': e3_4, 'D4': e4_4, 'D5': e5_4, 'D6': e6_4, 'D7': e7_4, 'D8': e8_4, 'D9': e9_4,
                         'E1':e1_5, 'E2': e2_5, 'E3': e3_5, 'E4': e4_5, 'E5': e5_5, 'E6': e6_5, 'E7': e7_5, 'E8': e8_5, 'E9': e9_5,
                         'F1':e1_6, 'F2': e2_6, 'F3': e3_6, 'F4': e4_6, 'F5': e5_6, 'F6': e6_6, 'F7': e7_6, 'F8': e8_6, 'F9': e9_6,
                         'G1':e1_7, 'G2': e2_7, 'G3': e3_7, 'G4': e4_7, 'G5': e5_7, 'G6': e6_7, 'G7': e7_7, 'G8': e8_7, 'G9': e9_7,
                         'H1':e1_8, 'H2': e2_8, 'H3': e3_8, 'H4': e4_8, 'H5': e5_8, 'H6': e6_8, 'H7': e7_8, 'H8': e8_8, 'H9': e9_8,
                         'I1':e1_9, 'I2': e2_9, 'I3': e3_9, 'I4': e4_9, 'I5': e5_9, 'I6': e6_9, 'I7': e7_9, 'I8': e8_9, 'I9': e9_9}











    def buttonClick(self, button, frame):
        if button is "new":
            pass
            # game.newGame
            #self.initialize

        elif button is "rules":
            self.print(Rules, frame)


        elif button is "hint":
            pass
            #self.fill(game.hint)
        elif button is "solve":
            pass
            #self.fill(game.solve)
        elif button is "hide":
            self.clearMessage(frame)


    def print(self, message, frame):

        frame.insert("end", message)

    def clearMessage(self, frame):
        frame.delete(1.0, "end")



    def fill (self, State):
        #@variable State should be a dictionary with keys representing board coordinates and values representing what number should
        #be in that coordinate ie{A1:4, B3:2, etc}

        Dict1 = State
        Dict2 = boxDictionary

        stateKeys = Dict1.keys()
        I = 0
        while I < stateKeys.length():
            x = Dict1(stateKeys(I))
            y = Dict2(stateKeys(I))
            if y.state != "readonly":
                y.insert(x)
                y.configure(state = "readonly")
                I = I + 1
            else:
                I = I + 1
















if __name__ == "__main__":
    app = sudokuGUI(None)
    app.title('sudoku player 1.0')
    #game = sudoku
    #game.update(self.readIn())




    app.mainloop()
