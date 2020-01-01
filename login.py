import tkinter

class Login:
    def __init__(self):
        self.password = ''
        
    def loginUI(self, frame):
        passwordLabel = tkinter.Label(frame, text='Password', bg='black', fg='white')
        passwordInput = tkinter.Entry(frame, textvariable = self.password)
        passwordButton = tkinter.Button(frame, text = 'Login')

        passwordLabel.grid(row = 0, column = 0, sticky = 'nsnew', pady = 4, padx = 3)
        passwordInput.grid(row = 1, column = 0, columnspan=3, sticky = 'nsnew')
        passwordButton.grid(row = 2, column = 2, pady = 10)
