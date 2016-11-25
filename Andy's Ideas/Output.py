#Resources:

#http://sebsauvage.net/python/gui/#import
#http://effbot.org/tkinterbook/canvas.htm
#https://www.tutorialspoint.com/python/tk_pack.htm
#http://stackoverflow.com/questions/11980812/how-do-you-create-a-button-on-a-tkinter-canvas
    #atomicinf

#The purpose of this script is to act as the GUI for a suduko game

import tkinter
#import sudoku.py




class sudokuGUI(tkinter.Tk):
    boxDictionary = []
    openBoxes = []
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

        boxDictionary = [((1,1), e1_1), ((2,1), e2_1), ((3,1), e3_1), ((4,1), e4_1), ((5,1), e5_1), ((6,1), e6_1), ((7,1), e7_1), ((8,1), e8_1), ((9,1), e9_1),
                         ((1, 2), e1_2), ((2,2), e2_2), ((3,2), e3_2), ((4,2), e4_2), ((5,2), e5_2), ((6,2), e6_2), ((7,2), e7_2), ((8,2), e8_2), ((9,2), e9_2),
                         ((1, 3), e1_3), ((2,3), e2_3), ((3,3), e3_3), ((4,3), e4_3), ((5,3), e5_3), ((6,3), e6_3), ((7,3), e7_3), ((8,3), e8_3), ((9,3), e9_3),
                         ((1, 4), e1_4), ((2,4), e2_4), ((3,4), e3_4), ((4,4), e4_4), ((5,4), e5_4), ((6,4), e6_4), ((7,4), e7_4), ((8,4), e8_4), ((9,4), e9_4),
                         ((1, 5), e1_5), ((2,5), e2_5), ((3,5), e3_5), ((4,5), e4_5), ((5,5), e5_5), ((6,5), e6_5), ((7,5), e7_5), ((8,5), e8_5), ((9,5), e9_5),
                         ((1, 6), e1_6), ((2,6), e2_6), ((3,6), e3_6), ((4,6), e4_6), ((5,6), e5_6), ((6,6), e6_6), ((7,6), e7_6), ((8,6), e8_6), ((9,6), e9_6),
                         ((1, 7), e1_7), ((2,7), e2_7), ((3,7), e3_7), ((4,7), e4_7), ((5,7), e5_7), ((6,7), e6_7), ((7,7), e7_7), ((8,7), e8_7), ((9,7), e9_7),
                         ((1, 8), e1_8), ((2,8), e2_8), ((3,8), e3_8), ((4,8), e4_8), ((5,8), e5_8), ((6,8), e6_8), ((7,8), e7_8), ((8,8), e8_8), ((9,8), e9_8),
                         ((1, 9), e1_9), ((2,9), e2_9), ((3,9), e3_9), ((4,9), e4_9), ((5,9), e5_9), ((6,9), e6_9), ((7,9), e7_9), ((8,9), e8_9), ((9,9), e9_9),]

        fill









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


    def print(self, message):
        pass

    def fill (self, tofill, available):
        pass









if __name__ == "__main__":
    app = sudokuGUI(None)
    app.title('sudoku player 1.0')
    #game = sudoku




    app.mainloop()
