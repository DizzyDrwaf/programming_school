import tkinter as tk

def press_button():
    # set output text
    # read input text width method get()
    output['text'] = "Go to bed " + userInput.get()

root = tk.Tk()
root.title('Yatzy')
root.minsize(300, 100)

# Column 0
labels = []

labels_sv = ['Namn', 'Ettor', 'Tvåor', 'Treor', 'Fyror', 'Femmor', 'Sexor']
for currentLabel in labels_sv:
    newLabel = tk.Label(root, text=currentLabel)
    labels.append(newLabel)

for currentRow in range(len(labels)):
    # use sticky to justify left
    labels[currentRow].grid(row=currentRow, column=0, sticky=tk.W)

# Column 1, 2, ...
numberOfPlayers = 3

# player[0] list for first player. Name of player and results.
# player[1] list for second player
# player[2] ...
# ...
players = []

# add a list per player
for i in range(numberOfPlayers):
    players.append([])

for i in range(len(players)):
    # fill each list with empty labels
    for currentRow in range(len(labels)):
        playerEntry = tk.Label(root)
        players[i].append(playerEntry)
        playerEntry.grid(row=currentRow, column=i + 1)

# set player names
players[0][0]['text'] = 'Ada'
players[1][0]['text'] = 'Beda'
players[2][0]['text'] = 'Cedric'

root.mainloop()