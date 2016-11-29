# Resources:

# http://sebsauvage.net/python/gui/#import
# http://effbot.org/tkinterbook/canvas.htm
# https://www.tutorialspoint.com/python/tk_pack.htm
# http://stackoverflow.com/questions/11980812/how-do-you-create-a-button-on-a-tkinter-canvas
# atomicinf

# The purpose of this script is to act as the GUI for a suduko game

import tkinter
import random

Rules = "This is a simple soduku solver. Each red box accepts user input, each grey box is a value which was set initially by the game." \
        "The goal of the game is to fill each row, column, and 3X3 box with vlaues 1-9.  " \
        "To see an example, press 'New Game' followed by 'Solve'  " \
        "'New Game' will clear the board and start a new puzzle.  " \
        "''Hint !' will fill in the next best value in the grid.  " \
        "'Solve' will fill in the entire grid with the solution"


class sudokuSolver():
    validNumbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    dictcolumn = dict()
    dictrow = dict()
    dictbox = dict()
    r1 = []
    r2 = []
    r3 = []
    r4 = []
    r5 = []
    r6 = []
    r7 = []
    r8 = []
    r9 = []
    c1 = []
    c2 = []
    c3 = []
    c4 = []
    c5 = []
    c6 = []
    c7 = []
    c8 = []
    c9 = []
    b1 = []
    b2 = []
    b3 = []
    b4 = []
    b5 = []
    b6 = []
    b7 = []
    b8 = []
    b9 = []
    puzzleState = dict()
    openSquares = []

    def __init__(self):
        sudokuSolver.r1 = sudokuSolver.validNumbers.copy()
        sudokuSolver.r2 = sudokuSolver.validNumbers.copy()
        sudokuSolver.r3 = sudokuSolver.validNumbers.copy()
        sudokuSolver.r4 = sudokuSolver.validNumbers.copy()
        sudokuSolver.r5 = sudokuSolver.validNumbers.copy()
        sudokuSolver.r6 = sudokuSolver.validNumbers.copy()
        sudokuSolver.r7 = sudokuSolver.validNumbers.copy()
        sudokuSolver.r8 = sudokuSolver.validNumbers.copy()
        sudokuSolver.r9 = sudokuSolver.validNumbers.copy()
        sudokuSolver.c1 = sudokuSolver.validNumbers.copy()
        sudokuSolver.c2 = sudokuSolver.validNumbers.copy()
        sudokuSolver.c3 = sudokuSolver.validNumbers.copy()
        sudokuSolver.c4 = sudokuSolver.validNumbers.copy()
        sudokuSolver.c5 = sudokuSolver.validNumbers.copy()
        sudokuSolver.c6 = sudokuSolver.validNumbers.copy()
        sudokuSolver.c7 = sudokuSolver.validNumbers.copy()
        sudokuSolver.c8 = sudokuSolver.validNumbers.copy()
        sudokuSolver.c9 = sudokuSolver.validNumbers.copy()
        sudokuSolver.b1 = sudokuSolver.validNumbers.copy()
        sudokuSolver.b2 = sudokuSolver.validNumbers.copy()
        sudokuSolver.b3 = sudokuSolver.validNumbers.copy()
        sudokuSolver.b4 = sudokuSolver.validNumbers.copy()
        sudokuSolver.b5 = sudokuSolver.validNumbers.copy()
        sudokuSolver.b6 = sudokuSolver.validNumbers.copy()
        sudokuSolver.b7 = sudokuSolver.validNumbers.copy()
        sudokuSolver.b8 = sudokuSolver.validNumbers.copy()
        sudokuSolver.b9 = sudokuSolver.validNumbers.copy()

        r1 = sudokuSolver.r1
        r2 = sudokuSolver.r2
        r3 = sudokuSolver.r3
        r4 = sudokuSolver.r4
        r5 = sudokuSolver.r5
        r6 = sudokuSolver.r6
        r7 = sudokuSolver.r7
        r8 = sudokuSolver.r8
        r9 = sudokuSolver.r9
        c1 = sudokuSolver.c1
        c2 = sudokuSolver.c2
        c3 = sudokuSolver.c3
        c4 = sudokuSolver.c4
        c5 = sudokuSolver.c5
        c6 = sudokuSolver.c6
        c7 = sudokuSolver.c7
        c8 = sudokuSolver.c8
        c9 = sudokuSolver.c9
        b1 = sudokuSolver.b1
        b2 = sudokuSolver.b2
        b3 = sudokuSolver.b3
        b4 = sudokuSolver.b4
        b5 = sudokuSolver.b5
        b6 = sudokuSolver.b6
        b7 = sudokuSolver.b7
        b8 = sudokuSolver.b8
        b9 = sudokuSolver.b9

        sudokuSolver.dictcolumn = {'A1': c1, 'A2': c2, 'A3': c3, 'A4': c4, 'A5': c5, 'A6': c6, 'A7': c7, 'A8': c8,
                                   'A9': c9,
                                   'B1': c1, 'B2': c2, 'B3': c3, 'B4': c4, 'B5': c5, 'B6': c6, 'B7': c7, 'B8': c8,
                                   'B9': c9,
                                   'C1': c1, 'C2': c2, 'C3': c3, 'C4': c4, 'C5': c5, 'C6': c6, 'C7': c7, 'C8': c8,
                                   'C9': c9,
                                   'D1': c1, 'D2': c2, 'D3': c3, 'D4': c4, 'D5': c5, 'D6': c6, 'D7': c7, 'D8': c8,
                                   'D9': c9,
                                   'E1': c1, 'E2': c2, 'E3': c3, 'E4': c4, 'E5': c5, 'E6': c6, 'E7': c7, 'E8': c8,
                                   'E9': c9,
                                   'F1': c1, 'F2': c2, 'F3': c3, 'F4': c4, 'F5': c5, 'F6': c6, 'F7': c7, 'F8': c8,
                                   'F9': c9,
                                   'G1': c1, 'G2': c2, 'G3': c3, 'G4': c4, 'G5': c5, 'G6': c6, 'G7': c7, 'G8': c8,
                                   'G9': c9,
                                   'H1': c1, 'H2': c2, 'H3': c3, 'H4': c4, 'H5': c5, 'H6': c6, 'H7': c7, 'H8': c8,
                                   'H9': c9,
                                   'I1': c1, 'I2': c2, 'I3': c3, 'I4': c4, 'I5': c5, 'I6': c6, 'I7': c7, 'I8': c8,
                                   'I9': c9,
                                   }

        sudokuSolver.dictrow = {'A1': r1, 'A2': r1, 'A3': r1, 'A4': r1, 'A5': r1, 'A6': r1, 'A7': r1, 'A8': r1,
                                'A9': r1,
                                'B1': r2, 'B2': r2, 'B3': r2, 'B4': r2, 'B5': r2, 'B6': r2, 'B7': r2, 'B8': r2,
                                'B9': r2,
                                'C1': r3, 'C2': r3, 'C3': r3, 'C4': r3, 'C5': r3, 'C6': r3, 'C7': r3, 'C8': r3,
                                'C9': r3,
                                'D1': r4, 'D2': r4, 'D3': r4, 'D4': r4, 'D5': r4, 'D6': r4, 'D7': r4, 'D8': r4,
                                'D9': r4,
                                'E1': r5, 'E2': r5, 'E3': r5, 'E4': r5, 'E5': r5, 'E6': r5, 'E7': r5, 'E8': r5,
                                'E9': r5,
                                'F1': r6, 'F2': r6, 'F3': r6, 'F4': r6, 'F5': r6, 'F6': r6, 'F7': r6, 'F8': r6,
                                'F9': r6,
                                'G1': r7, 'G2': r7, 'G3': r7, 'G4': r7, 'G5': r7, 'G6': r7, 'G7': r7, 'G8': r7,
                                'G9': r7,
                                'H1': r8, 'H2': r8, 'H3': r8, 'H4': r8, 'H5': r8, 'H6': r8, 'H7': r8, 'H8': r8,
                                'H9': r8,
                                'I1': r9, 'I2': r9, 'I3': r9, 'I4': r9, 'I5': r9, 'I6': r9, 'I7': r9, 'I8': r9,
                                'I9': r9}

        sudokuSolver.dictbox = {'A1': b1, 'A2': b1, 'A3': b1, 'A4': b2, 'A5': b2, 'A6': b2, 'A7': b3, 'A8': b3,
                                'A9': b3,
                                'B1': b1, 'B2': b1, 'B3': b1, 'B4': b2, 'B5': b2, 'B6': b2, 'B7': b3, 'B8': b3,
                                'B9': b3,
                                'C1': b1, 'C2': b1, 'C3': b1, 'C4': b2, 'C5': b2, 'C6': b2, 'C7': b3, 'C8': b3,
                                'C9': b3,
                                'D1': b4, 'D2': b4, 'D3': b4, 'D4': b5, 'D5': b5, 'D6': b5, 'D7': b6, 'D8': b6,
                                'D9': b6,
                                'E1': b4, 'E2': b4, 'E3': b4, 'E4': b5, 'E5': b5, 'E6': b5, 'E7': b6, 'E8': b6,
                                'E9': b6,
                                'F1': b4, 'F2': b4, 'F3': b4, 'F4': b5, 'F5': b5, 'F6': b5, 'F7': b6, 'F8': b6,
                                'F9': b6,
                                'G1': b7, 'G2': b7, 'G3': b7, 'G4': b8, 'G5': b8, 'G6': b8, 'G7': b9, 'G8': b9,
                                'G9': b9,
                                'H1': b7, 'H2': b7, 'H3': b7, 'H4': b8, 'H5': b8, 'H6': b8, 'H7': b9, 'H8': b9,
                                'H9': b9,
                                'I1': b7, 'I2': b7, 'I3': b7, 'I4': b8, 'I5': b8, 'I6': b8, 'I7': b9, 'I8': b9,
                                'I9': b9}

        sudokuSolver.openSquares = ['A1', 'B1', 'C1', 'D1', 'E1', 'F1', 'G1', 'H1', 'I1',
                                    'A2', 'B2', 'C2', 'D2', 'E2', 'F2', 'G2', 'H2', 'I2',
                                    'A3', 'B3', 'C3', 'D3', 'E3', 'F3', 'G3', 'H3', 'I3',
                                    'A4', 'B4', 'C4', 'D4', 'E4', 'F4', 'G4', 'H4', 'I4',
                                    'A5', 'B5', 'C5', 'D5', 'E5', 'F5', 'G5', 'H5', 'I5',
                                    'A6', 'B6', 'C6', 'D6', 'E6', 'F6', 'G6', 'H6', 'I6',
                                    'A7', 'B7', 'C7', 'D7', 'E7', 'F7', 'G7', 'H7', 'I7',
                                    'A8', 'B8', 'C8', 'D8', 'E8', 'F8', 'G8', 'H8', 'I8',
                                    'A9', 'B9', 'C9', 'D9', 'E9', 'F9', 'G9', 'H9', 'I9', ]

    def solve(self, boardState):

        # read current board state and delete values from valid moves pool
        gameState = dict()
        openSquares = sudokuSolver.openSquares
        StateKeys = boardState.keys()
        for x in StateKeys:
            I = boardState[x]
            R = sudokuSolver.dictrow[x]
            C = sudokuSolver.dictcolumn[x]
            B = sudokuSolver.dictbox[x]
            if I is not None:
                if I in R:
                    deleteR = R.index(I)
                    del R[deleteR]
                if I in C:
                    deleteC = C.index(I)
                    del C[deleteC]
                if I in B:
                    deleteB = B.index(I)
                    del B[deleteB]

        # delete any moves the system makes from the valid moves pool
        systemMoves = dict()
        # while openSquares is not None:
        systemMoveKeys = systemMoves.keys()
        if StateKeys is not None:
            for v in StateKeys:
                if boardState[v] is not None:
                    deleteV = openSquares.index(v)
                    del openSquares[deleteV]
        elif systemMoves is not None:
            for y in systemMoveKeys:
                deleteY = openSquares.index(y)
                del openSquares[deleteY]
        # this is where the system will search for moves
        systemMoves = self.search(openSquares)

        return systemMoves

    def search(self, open):
        done = False
        while not done:
            systemMoves = dict()
            openSquares = open.copy()
            columnNumb = sudokuSolver.dictcolumn.copy()
            rowNumb = sudokuSolver.dictrow.copy()
            boxNumb = sudokuSolver.dictbox.copy()
            for x in openSquares:
                valueT = 1
                while valueT <= 9 and x in openSquares:
                    columnNum = columnNumb[x]
                    rowNum = rowNumb[x]
                    boxNum = boxNumb[x]
                    if valueT in columnNum and valueT in rowNum and valueT in boxNum:
                        systemMoves[x] = valueT
                        deletec = columnNum.index(valueT)
                        del columnNumb[deletec]
                        deleter = rowNum.index(valueT)
                        del rowNumb[deleter]
                        deleteb = boxNum.index(valueT)
                        del boxNumb[deleteb]
                        deletex = openSquares.index(x)
                        del openSquares[deletex]

                    valueT += 1
                else:
                    pass
            gameState = systemMoves

            if openSquares is not None:
                done = False
            else:
                done = True
                return gameState

    def hint(self, boardState):
        pass

    def newPuzzle(self):
        self.__init__()
        newState = self.randPuzzles()
        sudokuSolver.puzzleState = newState

    def State(self):
        return sudokuSolver.puzzleState

    def randPuzzles(self):
        puzzleNumber = random.randint(1, 5)
        puzzle1 = {'A1': 3, 'A3': 1, 'A4': 5, 'A5': 2, 'A6': 9,
                   'B1': 9, 'B3': 4, 'B7': 3, 'B8': 5,
                   'C5': 3, 'C8': 8,
                   'D1': 1, 'D2': 2, 'D3': 5, 'D4': 3, 'D5': 8,
                   'E4': 1, 'E5': 4, 'E7': 7, 'E9': 3,
                   'F1': 7, 'F9': 5,
                   'G1': 8, 'G6': 3, 'G8': 9,
                   'H2': 1, 'H5': 7, 'H9': 8,
                   'I1': 5, 'I2': 3, 'I3': 9, 'I4': 2, 'I5': 1, 'I6': 8, 'I8': 7, 'I9': 6}
        puzzle2 = {'B2': 2}
        puzzle3 = {'C3': 3}
        puzzle4 = {'D4': 4}
        puzzle5 = {'E5': 5}
        if puzzleNumber == 1:
            chosen = puzzle1
        elif puzzleNumber == 2:
            chosen = puzzle2
        elif puzzleNumber == 3:
            chosen = puzzle3
        elif puzzleNumber == 4:
            chosen = puzzle4
        elif puzzleNumber == 5:
            chosen = puzzle5
        else:
            chosen = puzzle2

        return puzzle1


class sudokuGUI(tkinter.Tk):
    rulesPressed = False
    boxDictionary = dict()
    # gameState = {"A1":1, "B6":6, "F2":2}
    bgColor = "red"
    game = sudokuSolver

    def __init__(self, parent):
        tkinter.Tk.__init__(self, parent)
        self.parent = parent
        self.initialize()

    def initialize(self):

        Bframe = tkinter.Frame(self)
        Bframe.pack(side="right")

        # bottomframe = tkinter.Frame(self)
        # bottomframe.pack()

        # create text box at bottom for displaying messages
        messageB = tkinter.Text(self, height=10, width=50, bg="grey")
        messageB.pack(side="right")
        messageB.configure(wrap="word")

        newButton = tkinter.Button(Bframe, text="New Game", command=lambda: self.buttonClick("new", None))
        newButton.pack()

        rButton = tkinter.Button(Bframe, text="Rules", command=lambda: self.buttonClick("rules", messageB))
        rButton.pack()

        hiButton = tkinter.Button(Bframe, text="Hide Rules", command=lambda: self.buttonClick("hide", messageB))
        hiButton.pack()

        hButton = tkinter.Button(Bframe, text="Hint !", command=lambda: self.buttonClick("hint", None))
        hButton.pack()

        sButton = tkinter.Button(Bframe, text="Solve", command=lambda: self.buttonClick("solve", None))
        sButton.pack()

        #     #create a frame to hold the canvas
        CFrame = tkinter.Frame(self)
        CFrame.pack(side="left")
        #     GFrame = tkinter.Frame(self)
        #
        #
        # create the canvas
        grid = tkinter.Canvas(CFrame, bg="black", bd=8, cursor="arrow", relief="raised", height=630, width=630)
        grid.pack()

        # draw horizontal lines on the canvas
        linewidth = 5
        grid.create_rectangle(10, 10, 641, 641, fill="white")

        grid.create_line(10, 80, 641, 80)
        grid.create_line(10, 150, 641, 150)
        grid.create_line(10, 220, 641, 220, width=linewidth)
        grid.create_line(10, 290, 641, 290)
        grid.create_line(10, 360, 641, 360)
        grid.create_line(10, 430, 641, 430, width=linewidth)
        grid.create_line(10, 500, 641, 500)
        grid.create_line(10, 570, 641, 570)

        # draw vertical lines on the canvas
        grid.create_line(80, 10, 80, 641)
        grid.create_line(150, 10, 150, 641)
        grid.create_line(220, 10, 220, 641, width=linewidth)
        grid.create_line(290, 10, 290, 641)
        grid.create_line(360, 10, 360, 641)
        grid.create_line(430, 10, 430, 641, width=linewidth)
        grid.create_line(500, 10, 500, 641)
        grid.create_line(570, 10, 570, 641)

        ACanvas = grid
        self.createInputBoxes(grid)
        # self.fill(sudoku.gameState)

    def createInputBoxes(self, window):
        # create user input boxes on each grid box
        grid = window

        e1_1 = tkinter.Entry(self, width=4, bg=sudokuGUI.bgColor, relief="flat", font=70, readonlybackground="grey",
                             justify="center")
        e2_1 = tkinter.Entry(self, width=4, bg=sudokuGUI.bgColor, relief="flat", font=70, readonlybackground="grey",
                             justify="center")
        e3_1 = tkinter.Entry(self, width=4, bg=sudokuGUI.bgColor, relief="flat", font=70, readonlybackground="grey",
                             justify="center")
        e4_1 = tkinter.Entry(self, width=4, bg=sudokuGUI.bgColor, relief="flat", font=70, readonlybackground="grey",
                             justify="center")
        e5_1 = tkinter.Entry(self, width=4, bg=sudokuGUI.bgColor, relief="flat", font=70, readonlybackground="grey",
                             justify="center")
        e6_1 = tkinter.Entry(self, width=4, bg=sudokuGUI.bgColor, relief="flat", font=70, readonlybackground="grey",
                             justify="center")
        e7_1 = tkinter.Entry(self, width=4, bg=sudokuGUI.bgColor, relief="flat", font=70, readonlybackground="grey",
                             justify="center")
        e8_1 = tkinter.Entry(self, width=4, bg=sudokuGUI.bgColor, relief="flat", font=70, readonlybackground="grey",
                             justify="center")
        e9_1 = tkinter.Entry(self, width=4, bg=sudokuGUI.bgColor, relief="flat", font=70, readonlybackground="grey",
                             justify="center")
        e1_2 = tkinter.Entry(self, width=4, bg=sudokuGUI.bgColor, relief="flat", font=70, readonlybackground="grey",
                             justify="center")
        e2_2 = tkinter.Entry(self, width=4, bg=sudokuGUI.bgColor, relief="flat", font=70, readonlybackground="grey",
                             justify="center")
        e3_2 = tkinter.Entry(self, width=4, bg=sudokuGUI.bgColor, relief="flat", font=70, readonlybackground="grey",
                             justify="center")
        e4_2 = tkinter.Entry(self, width=4, bg=sudokuGUI.bgColor, relief="flat", font=70, readonlybackground="grey",
                             justify="center")
        e5_2 = tkinter.Entry(self, width=4, bg=sudokuGUI.bgColor, relief="flat", font=70, readonlybackground="grey",
                             justify="center")
        e6_2 = tkinter.Entry(self, width=4, bg=sudokuGUI.bgColor, relief="flat", font=70, readonlybackground="grey",
                             justify="center")
        e7_2 = tkinter.Entry(self, width=4, bg=sudokuGUI.bgColor, relief="flat", font=70, readonlybackground="grey",
                             justify="center")
        e8_2 = tkinter.Entry(self, width=4, bg=sudokuGUI.bgColor, relief="flat", font=70, readonlybackground="grey",
                             justify="center")
        e9_2 = tkinter.Entry(self, width=4, bg=sudokuGUI.bgColor, relief="flat", font=70, readonlybackground="grey",
                             justify="center")
        e1_3 = tkinter.Entry(self, width=4, bg=sudokuGUI.bgColor, relief="flat", font=70, readonlybackground="grey",
                             justify="center")
        e2_3 = tkinter.Entry(self, width=4, bg=sudokuGUI.bgColor, relief="flat", font=70, readonlybackground="grey",
                             justify="center")
        e3_3 = tkinter.Entry(self, width=4, bg=sudokuGUI.bgColor, relief="flat", font=70, readonlybackground="grey",
                             justify="center")
        e4_3 = tkinter.Entry(self, width=4, bg=sudokuGUI.bgColor, relief="flat", font=70, readonlybackground="grey",
                             justify="center")
        e5_3 = tkinter.Entry(self, width=4, bg=sudokuGUI.bgColor, relief="flat", font=70, readonlybackground="grey",
                             justify="center")
        e6_3 = tkinter.Entry(self, width=4, bg=sudokuGUI.bgColor, relief="flat", font=70, readonlybackground="grey",
                             justify="center")
        e7_3 = tkinter.Entry(self, width=4, bg=sudokuGUI.bgColor, relief="flat", font=70, readonlybackground="grey",
                             justify="center")
        e8_3 = tkinter.Entry(self, width=4, bg=sudokuGUI.bgColor, relief="flat", font=70, readonlybackground="grey",
                             justify="center")
        e9_3 = tkinter.Entry(self, width=4, bg=sudokuGUI.bgColor, relief="flat", font=70, readonlybackground="grey",
                             justify="center")
        e1_4 = tkinter.Entry(self, width=4, bg=sudokuGUI.bgColor, relief="flat", font=70, readonlybackground="grey",
                             justify="center")
        e2_4 = tkinter.Entry(self, width=4, bg=sudokuGUI.bgColor, relief="flat", font=70, readonlybackground="grey",
                             justify="center")
        e3_4 = tkinter.Entry(self, width=4, bg=sudokuGUI.bgColor, relief="flat", font=70, readonlybackground="grey",
                             justify="center")
        e4_4 = tkinter.Entry(self, width=4, bg=sudokuGUI.bgColor, relief="flat", font=70, readonlybackground="grey",
                             justify="center")
        e5_4 = tkinter.Entry(self, width=4, bg=sudokuGUI.bgColor, relief="flat", font=70, readonlybackground="grey",
                             justify="center")
        e6_4 = tkinter.Entry(self, width=4, bg=sudokuGUI.bgColor, relief="flat", font=70, readonlybackground="grey",
                             justify="center")
        e7_4 = tkinter.Entry(self, width=4, bg=sudokuGUI.bgColor, relief="flat", font=70, readonlybackground="grey",
                             justify="center")
        e8_4 = tkinter.Entry(self, width=4, bg=sudokuGUI.bgColor, relief="flat", font=70, readonlybackground="grey",
                             justify="center")
        e9_4 = tkinter.Entry(self, width=4, bg=sudokuGUI.bgColor, relief="flat", font=70, readonlybackground="grey",
                             justify="center")
        e1_5 = tkinter.Entry(self, width=4, bg=sudokuGUI.bgColor, relief="flat", font=70, readonlybackground="grey",
                             justify="center")
        e2_5 = tkinter.Entry(self, width=4, bg=sudokuGUI.bgColor, relief="flat", font=70, readonlybackground="grey",
                             justify="center")
        e3_5 = tkinter.Entry(self, width=4, bg=sudokuGUI.bgColor, relief="flat", font=70, readonlybackground="grey",
                             justify="center")
        e4_5 = tkinter.Entry(self, width=4, bg=sudokuGUI.bgColor, relief="flat", font=70, readonlybackground="grey",
                             justify="center")
        e5_5 = tkinter.Entry(self, width=4, bg=sudokuGUI.bgColor, relief="flat", font=70, readonlybackground="grey",
                             justify="center")
        e6_5 = tkinter.Entry(self, width=4, bg=sudokuGUI.bgColor, relief="flat", font=70, readonlybackground="grey",
                             justify="center")
        e7_5 = tkinter.Entry(self, width=4, bg=sudokuGUI.bgColor, relief="flat", font=70, readonlybackground="grey",
                             justify="center")
        e8_5 = tkinter.Entry(self, width=4, bg=sudokuGUI.bgColor, relief="flat", font=70, readonlybackground="grey",
                             justify="center")
        e9_5 = tkinter.Entry(self, width=4, bg=sudokuGUI.bgColor, relief="flat", font=70, readonlybackground="grey",
                             justify="center")
        e1_6 = tkinter.Entry(self, width=4, bg=sudokuGUI.bgColor, relief="flat", font=70, readonlybackground="grey",
                             justify="center")
        e2_6 = tkinter.Entry(self, width=4, bg=sudokuGUI.bgColor, relief="flat", font=70, readonlybackground="grey",
                             justify="center")
        e3_6 = tkinter.Entry(self, width=4, bg=sudokuGUI.bgColor, relief="flat", font=70, readonlybackground="grey",
                             justify="center")
        e4_6 = tkinter.Entry(self, width=4, bg=sudokuGUI.bgColor, relief="flat", font=70, readonlybackground="grey",
                             justify="center")
        e5_6 = tkinter.Entry(self, width=4, bg=sudokuGUI.bgColor, relief="flat", font=70, readonlybackground="grey",
                             justify="center")
        e6_6 = tkinter.Entry(self, width=4, bg=sudokuGUI.bgColor, relief="flat", font=70, readonlybackground="grey",
                             justify="center")
        e7_6 = tkinter.Entry(self, width=4, bg=sudokuGUI.bgColor, relief="flat", font=70, readonlybackground="grey",
                             justify="center")
        e8_6 = tkinter.Entry(self, width=4, bg=sudokuGUI.bgColor, relief="flat", font=70, readonlybackground="grey",
                             justify="center")
        e9_6 = tkinter.Entry(self, width=4, bg=sudokuGUI.bgColor, relief="flat", font=70, readonlybackground="grey",
                             justify="center")
        e1_7 = tkinter.Entry(self, width=4, bg=sudokuGUI.bgColor, relief="flat", font=70, readonlybackground="grey",
                             justify="center")
        e2_7 = tkinter.Entry(self, width=4, bg=sudokuGUI.bgColor, relief="flat", font=70, readonlybackground="grey",
                             justify="center")
        e3_7 = tkinter.Entry(self, width=4, bg=sudokuGUI.bgColor, relief="flat", font=70, readonlybackground="grey",
                             justify="center")
        e4_7 = tkinter.Entry(self, width=4, bg=sudokuGUI.bgColor, relief="flat", font=70, readonlybackground="grey",
                             justify="center")
        e5_7 = tkinter.Entry(self, width=4, bg=sudokuGUI.bgColor, relief="flat", font=70, readonlybackground="grey",
                             justify="center")
        e6_7 = tkinter.Entry(self, width=4, bg=sudokuGUI.bgColor, relief="flat", font=70, readonlybackground="grey",
                             justify="center")
        e7_7 = tkinter.Entry(self, width=4, bg=sudokuGUI.bgColor, relief="flat", font=70, readonlybackground="grey",
                             justify="center")
        e8_7 = tkinter.Entry(self, width=4, bg=sudokuGUI.bgColor, relief="flat", font=70, readonlybackground="grey",
                             justify="center")
        e9_7 = tkinter.Entry(self, width=4, bg=sudokuGUI.bgColor, relief="flat", font=70, readonlybackground="grey",
                             justify="center")
        e1_8 = tkinter.Entry(self, width=4, bg=sudokuGUI.bgColor, relief="flat", font=70, readonlybackground="grey",
                             justify="center")
        e2_8 = tkinter.Entry(self, width=4, bg=sudokuGUI.bgColor, relief="flat", font=70, readonlybackground="grey",
                             justify="center")
        e3_8 = tkinter.Entry(self, width=4, bg=sudokuGUI.bgColor, relief="flat", font=70, readonlybackground="grey",
                             justify="center")
        e4_8 = tkinter.Entry(self, width=4, bg=sudokuGUI.bgColor, relief="flat", font=70, readonlybackground="grey",
                             justify="center")
        e5_8 = tkinter.Entry(self, width=4, bg=sudokuGUI.bgColor, relief="flat", font=70, readonlybackground="grey",
                             justify="center")
        e6_8 = tkinter.Entry(self, width=4, bg=sudokuGUI.bgColor, relief="flat", font=70, readonlybackground="grey",
                             justify="center")
        e7_8 = tkinter.Entry(self, width=4, bg=sudokuGUI.bgColor, relief="flat", font=70, readonlybackground="grey",
                             justify="center")
        e8_8 = tkinter.Entry(self, width=4, bg=sudokuGUI.bgColor, relief="flat", font=70, readonlybackground="grey",
                             justify="center")
        e9_8 = tkinter.Entry(self, width=4, bg=sudokuGUI.bgColor, relief="flat", font=70, readonlybackground="grey",
                             justify="center")
        e1_9 = tkinter.Entry(self, width=4, bg=sudokuGUI.bgColor, relief="flat", font=70, readonlybackground="grey",
                             justify="center")
        e2_9 = tkinter.Entry(self, width=4, bg=sudokuGUI.bgColor, relief="flat", font=70, readonlybackground="grey",
                             justify="center")
        e3_9 = tkinter.Entry(self, width=4, bg=sudokuGUI.bgColor, relief="flat", font=70, readonlybackground="grey",
                             justify="center")
        e4_9 = tkinter.Entry(self, width=4, bg=sudokuGUI.bgColor, relief="flat", font=70, readonlybackground="grey",
                             justify="center")
        e5_9 = tkinter.Entry(self, width=4, bg=sudokuGUI.bgColor, relief="flat", font=70, readonlybackground="grey",
                             justify="center")
        e6_9 = tkinter.Entry(self, width=4, bg=sudokuGUI.bgColor, relief="flat", font=70, readonlybackground="grey",
                             justify="center")
        e7_9 = tkinter.Entry(self, width=4, bg=sudokuGUI.bgColor, relief="flat", font=70, readonlybackground="grey",
                             justify="center")
        e8_9 = tkinter.Entry(self, width=4, bg=sudokuGUI.bgColor, relief="flat", font=70, readonlybackground="grey",
                             justify="center")
        e9_9 = tkinter.Entry(self, width=4, bg=sudokuGUI.bgColor, relief="flat", font=70, readonlybackground="grey",
                             justify="center")

        grid.create_window(20, 30, anchor="nw", window=e1_1)
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

        sudokuGUI.boxDictionary = {'A1': e1_1, 'A2': e2_1, 'A3': e3_1, 'A4': e4_1, 'A5': e5_1, 'A6': e6_1, 'A7': e7_1,
                                   'A8': e8_1, 'A9': e9_1,
                                   'B1': e1_2, 'B2': e2_2, 'B3': e3_2, 'B4': e4_2, 'B5': e5_2, 'B6': e6_2, 'B7': e7_2,
                                   'B8': e8_2, 'B9': e9_2,
                                   'C1': e1_3, 'C2': e2_3, 'C3': e3_3, 'C4': e4_3, 'C5': e5_3, 'C6': e6_3, 'C7': e7_3,
                                   'C8': e8_3, 'C9': e9_3,
                                   'D1': e1_4, 'D2': e2_4, 'D3': e3_4, 'D4': e4_4, 'D5': e5_4, 'D6': e6_4, 'D7': e7_4,
                                   'D8': e8_4, 'D9': e9_4,
                                   'E1': e1_5, 'E2': e2_5, 'E3': e3_5, 'E4': e4_5, 'E5': e5_5, 'E6': e6_5, 'E7': e7_5,
                                   'E8': e8_5, 'E9': e9_5,
                                   'F1': e1_6, 'F2': e2_6, 'F3': e3_6, 'F4': e4_6, 'F5': e5_6, 'F6': e6_6, 'F7': e7_6,
                                   'F8': e8_6, 'F9': e9_6,
                                   'G1': e1_7, 'G2': e2_7, 'G3': e3_7, 'G4': e4_7, 'G5': e5_7, 'G6': e6_7, 'G7': e7_7,
                                   'G8': e8_7, 'G9': e9_7,
                                   'H1': e1_8, 'H2': e2_8, 'H3': e3_8, 'H4': e4_8, 'H5': e5_8, 'H6': e6_8, 'H7': e7_8,
                                   'H8': e8_8, 'H9': e9_8,
                                   'I1': e1_9, 'I2': e2_9, 'I3': e3_9, 'I4': e4_9, 'I5': e5_9, 'I6': e6_9, 'I7': e7_9,
                                   'I8': e8_9, 'I9': e9_9}

    def buttonClick(self, button, frame):
        if button is "new":

            sudokuGUI.game.newPuzzle(sudokuSolver())
            self.clearBoard()
            self.fill(sudokuGUI.game.State(sudokuSolver()))

        elif button is "rules":
            self.print(Rules, frame)


        elif button is "hint":
            pass
            # self.hint()
        elif button is "solve":

            self.solve()
        elif button is "hide":
            self.clearMessage(frame)

    def print(self, message, frame):

        frame.insert("end", message)

    def clearMessage(self, frame):
        frame.delete(1.0, "end")

    def fill(self, State):
        # @variable State should be a dictionary with keys representing board coordinates and values representing what number should
        # be in that coordinate ie{A1:4, B3:2, etc}

        Dict1 = State
        Dict2 = sudokuGUI.boxDictionary

        stateKeys = Dict1.keys()
        boardKeys = Dict2.keys()
        for I in stateKeys:
            for W in boardKeys:
                if I is W:
                    x = Dict1[I]
                    y = Dict2[I]
                    # g = y.get()
                    if y.get() is '':
                        y.insert(0, x)
                        y.configure(state="readonly")

    def readBoard(self):
        boxes = sudokuGUI.boxDictionary
        squareKeys = boxes.keys()
        boardState = dict()
        # I = 0
        # while I < len(boxDictionary):
        for x in squareKeys:
            square = boxes[x]
            try:
                boxValue = int(square.get())
            except:
                boxValue = None
            if boxValue is not None:
                boardState[x] = boxValue
        return boardState

    def clearBoard(self):
        gridBoxes = sudokuGUI.boxDictionary.values()
        for x in gridBoxes:
            x.configure(state="normal", bg=sudokuGUI.bgColor)
            x.delete(0, "end")

    def solve(self):
        boardState = self.readBoard()
        self.fill(sudokuGUI.game.solve(sudokuSolver(), boardState))

    def hint(self):
        boardState = self.readBoard()
        sudokuGUI.game.hint(sudokuSolver(), boardState)


if __name__ == "__main__":
    app = sudokuGUI(None)
    app.title('sudoku player 1.0')
    app.mainloop()
