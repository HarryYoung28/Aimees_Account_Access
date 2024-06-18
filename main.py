from tkinter import *

# ----------------------------------------------- FUNCTIONS -----------------------------------------------

# define screen
root = Tk()
# define size
root.minsize(width=1400, height=800)
# create Title
root.title("Hacktastic HQ - Hack That Account!")
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
title_label = Label(root, text="Hacktastic HQ", font=("Helvetica", 40))
title_label.grid(row=0, column=0, columnspan=2)

# buttons for quick links made into frame
quick_links_frame = Frame(root, width=1400, height=100)
quick_links_frame.grid(row=1, column=0, columnspan=2)
# home button
home_button = Button(quick_links_frame, text="HOME", font=("Helvetica", 30))
home_button.grid(row=1, column=0)

# access account button
access_account_button = Button(quick_links_frame, text="ACCESS ACCOUNT", font=("Helvetica", 30))
access_account_button.grid(row=1, column=1, padx=250)

# about button
about_button = Button(quick_links_frame, text="ABOUT", font=("Helvetica", 30))
about_button.grid(row=1, column=3)

# frames to differentiate how to use and user reviews
how_to_use_label_frame = Frame(root, width=700, height=100)
# border width and relief to create a black edging
how_to_use_label_frame.configure(borderwidth=2, relief=SOLID)
# sticky north, south, east, west to ensure it hits all sides
how_to_use_label_frame.grid(row=2, column=0, sticky=NSEW)

user_reviews_label_frame = Frame(root, width=700, height=100)
# border width and relief to create a black edging
user_reviews_label_frame.configure(borderwidth=2, relief=SOLID)
# sticky north, south, east, west to ensure it hits all sides
user_reviews_label_frame.grid(row=2, column=1, sticky=NSEW)

# labels for how to use and user reviews
how_to_use_label = Label(how_to_use_label_frame, text="How To Use Our System", font=("Helvetica", 30))
# expand and fill both to ensure label is in the middle of the frame
how_to_use_label.pack(expand=True, fill=BOTH)

user_reviews_label = Label(user_reviews_label_frame, text="User Reviews", font=("Helvetica", 30))
# expand and fill both to ensure label is in the middle of the frame
user_reviews_label.pack(expand=True, fill=BOTH)

# mainloop
root.mainloop()
