from tkinter import *

class Settings:
    def __init__(self, frame):
        self.volume = 50
        self.container = frame
        self.volumeControl()
        self.parameterControls()
    
    def volumeControl(self):
        volumeLabel = Label(self.container, text = 'Sound', bg='black', fg='white')
        volumeInput = Scale(self.container, from_ = 0, to = 100, orient = HORIZONTAL, bg='black', fg='white')
        volumeLabel.grid(row = 1, column = 0)
        volumeInput.grid(row = 1, column = 1, columnspan = 3, pady = 5)

    def parameterControls(self):
        parameterOneLabel = Label(self.container, text = 'PARAMETER 1', bg='black', fg='white')
        parameterTwoLabel = Label(self.container, text = 'PARAMETER 2', bg='black', fg='white')
        parameterOne =  Scale(self.container, from_ = 1, to = 7, tickinterval = 1, orient = HORIZONTAL, bg='black', fg='white')
        parameterTwo =  Scale(self.container, from_ = 1, to = 7, tickinterval = 1, orient = HORIZONTAL, bg='black', fg='white')

        parameterOneLabel.grid(row = 2, column = 0)
        parameterOne.grid(row = 2, column = 1, columnspan = 8, pady = 5)
        parameterTwoLabel.grid(row = 3, column = 0)
        parameterTwo.grid(row = 3, column = 1, columnspan = 8, pady = 5)