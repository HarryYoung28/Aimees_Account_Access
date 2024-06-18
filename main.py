from tkinter import *

# define screen
main = Tk()
# define size
main.minsize(width=1400, height=800)
# create Title
main.title("Account Access Manager")
# prevent accidental resizing of window
main.resizable(width=False, height=False)

# loop for column to be 700 wide each
for column in range(2):
    main.grid_columnconfigure(index=column, minsize=700)
    print(column)

# loop for first 3 rows to be 100 height
for row in range(3):
    main.grid_rowconfigure(index=row, minsize=100)

# final row to be 500 height
main.grid_rowconfigure(index=3, minsize=500)


# mainloop
main.mainloop()
