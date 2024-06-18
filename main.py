from tkinter import *

# ----------------------------------------------- FUNCTIONS -----------------------------------------------

# define screen
root = Tk()
# define size
root.minsize(width=1400, height=800)
# create Title
root.title("Account Access Manager")
# prevent accidental resizing of window
root.resizable(width=False, height=False)

# loop for column to be 700 wide each
for column in range(2):
    root.grid_columnconfigure(index=column, minsize=700)
    print(column)

# loop for first 3 rows to be 100 height
for row in range(3):
    root.grid_rowconfigure(index=row, minsize=100)

# final row to be 500 height
root.grid_rowconfigure(index=3, minsize=500)

# title label on screen
title_label = Label(root, text="Account Access Manager", font=("Helvetica", 30))
title_label.grid(row=0, column=0, columnspan=2)

# buttons for quick links made into frame
quick_links_frame = Frame(root, width=1400, height=100)
quick_links_frame.grid(row=1, column=0, columnspan=2)
# home button
home_button = Button(quick_links_frame, text="HOME", font=("Helvetica", 24))
home_button.grid(row=1, column=0)

# access account button
access_account_button = Button(quick_links_frame, text="ACCESS ACCOUNT", font=("Helvetica", 24))
access_account_button.grid(row=1, column=1, padx=250)
# about button
about_button = Button(quick_links_frame, text="ABOUT", font=("Helvetica", 24))
about_button.grid(row=1, column=3)

# labels for how to use and user reviews
how_to_use_label = Label(root, text="How to use our system", font=("Helvetica", 24))
how_to_use_label.grid(row=2, column=0)

user_reviews_label = Label(root, text="User reviews", font=("Helvetica", 24))
user_reviews_label.grid(row=2, column=1)

# mainloop
root.mainloop()
