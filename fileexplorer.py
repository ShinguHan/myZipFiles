from tkinter import *
from tkinter import filedialog
import zip
# Function for opening the
# file explorer window
def browseFiles():
	filename = filedialog.askdirectory()
	zip.zipFiles(filename)
	# Change label contents
	label_file_explorer.configure(text="File Opened: "+filename)
	
	
																								
# Create the root window
window = Tk()

# Set window title
window.title('성적서 압축기')

# Set window size
window.geometry("700x200")

#Set window background color
window.config(background = "white")

# Create a File Explorer label
label_file_explorer = Label(window,
							text = "압축할 폴더를 선택하세요.",
							width = 100, height = 4,
							fg = "blue")

	
button_explore = Button(window,
						text = "Browse Files",
						command = browseFiles)

button_exit = Button(window,
					text = "Exit",
					command = exit)

# Grid method is chosen for placing
# the widgets at respective positions
# in a table like structure by
# specifying rows and columns
label_file_explorer.grid(column = 1, row = 1)

button_explore.grid(column = 1, row = 2)

button_exit.grid(column = 1,row = 3)

# Let the window wait for any events
window.mainloop()
