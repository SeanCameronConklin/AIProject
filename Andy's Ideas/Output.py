#http://sebsauvage.net/python/gui/#import
#The purpose of this script is to act as the GUI for a suduko game

import tkinter





class simpleapp_tk(tkinter.Tk):
    def __init__ (self, parent):
        tkinter.Tk.__init__(self,parent)
        self.parent = parent
        self.initialize()

    def initialize(self):
        self.grid()

        self.entry = tkinter.Entry(self)
        self.entry.grid(column = 0, row = 0, sticky = 'EW')

        button = tkinter.Button(self, text = u"Click me !")
        button.grid(column = 1, row = 0)

        label = tkinter.Label(self, anchor = "w", fg = "white", bg = "blue")
        label.grid(column = 0, row = 1, columnspan = 2, sticky = 'EW')

if __name__ == "__main__":
    app = simpleapp_tk(None)
    app.title('sudoku solver 1.0')
    app.mainloop()