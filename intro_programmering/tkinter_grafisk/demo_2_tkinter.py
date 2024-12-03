import tkinter as tk

root = tk.Tk()

# Add labels at specified row and column.
# width to make all cells have same width independent of text length

row_0_column_0 = tk.Label(root,
                          text='row 0 column 0 ...',
                          borderwidth=1,
                          relief="solid",
                          width=20,
                          pady=10,)
row_0_column_0.grid(row=0, column=0)

row_0_column_1 = tk.Label(root,
                          text='row 0 column 1',
                          borderwidth=1,
                          relief="solid",
                          width=20,
                          pady=10)
row_0_column_1.grid(row=0, column=1)

row_1_column_0 = tk.Label(root,
                          text='row 1 column 0',
                          borderwidth=1,
                          relief="solid",
                          width=20,
                          pady=10)
row_1_column_0.grid(row=1, column=0)

row_1_column_1 = tk.Label(root,
                          text='row 1 column 1',
                          borderwidth=1,
                          relief="solid",
                          width=20,
                          pady=10)
row_1_column_1.grid(row=1, column=1)

row_2_column_0 = tk.Label(root,
                          text='row 2 column 0',
                          borderwidth=1,
                          relief="solid",
                          width=20,
                          pady=10)
row_2_column_0.grid(row=2, column=0)

row_2_column_1 = tk.Label(root,
                          text='row 2 column 1 ...',
                          borderwidth=1,
                          relief="solid",
                          width=20,
                          pady=10)
row_2_column_1.grid(row=2, column=1)

root.mainloop()
