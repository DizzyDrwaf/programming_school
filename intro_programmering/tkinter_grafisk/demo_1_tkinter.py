import tkinter as tk


def press_button():
    # set output text
    # read input text width method get()
    output['text'] = "Go to bed " + userInput.get()


# root is main window
root = tk.Tk()
root.title("demo 1")
root.minsize(700, 400)

# label added to root
label = tk.Label(root, text='Enter your name and press button.')
# call pack() to arrange label and make it visible
label.pack()

# text input added to root
userInput = tk.Entry(root)
userInput.pack()

# button added to root
# The function press_button() will be called when button is pressed.
button = tk.Button(root, text='button', command=press_button, bg='red')
button.pack()

output = tk.Label(root, text='output')
output.pack()

# run application
root.mainloop()

