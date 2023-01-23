from tkinter import Label as label
from tkinter import Tk as tk
from time import strftime

# creating tkinter window
root = tk()
root.title('Pedro\'s Clock')

# This function is used to
# display time on the label


def time():
    string = strftime('%H:%M:%S %p')
    lbl.config(text=string)
    lbl.after(1000, time)


# Styling the label widget so that clock
# will look more attractive
lbl = label(
    root,
    font=('garamond', 47, 'bold'),
    height='4',
    width='17',
    background='crimson',
    foreground='white',
)

# Placing clock at the centre
# of the tkinter window
lbl.pack(anchor='center')
time()
root.mainloop()
