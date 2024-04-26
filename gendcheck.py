import tkinter as tk
import tkinter.messagebox
import random

class CustomDialog(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.geometry("900x500")
        self.title("Custom Dialog")
        
        self.message_label = tk.Label(self, text="Are you gay?")
        self.message_label.pack(pady=10)
        
        self.yes_button = tk.Button(self, text="Yes", command=self.answer_yes)
        self.no_button = tk.Button(self, text="No", command=self.answer_no)
        self.no_button.pack(side="right", padx=10)
        self.yes_button.pack(side="right")
        
    def answer_yes(self):
        print("Da fuq")
        self.destroy()
        
    def answer_no(self):
        new_x = random.randint(0, window_width - button_width)
        new_y = random.randint(0, window_height - button_height)
        no_button.place(x=new_x, y=new_y)

def move_no_button():
    new_x = random.randint(0, window_width - button_width)
    new_y = random.randint(0, window_height - button_height)
    no_button.place(x=new_x, y=new_y)

def open_custom_dialog():
    dialog = CustomDialog(root)

# Create the main window
root = tk.Tk()
root.title("gender Check")

# Get the dimensions of the window
window_width = 1000
window_height = 1500
# Create the "Yes" and "No" buttons
yes_button = tk.Button(root, text="Yes", command=open_custom_dialog)
no_button = tk.Button(root, text="No", command=move_no_button)

# Get button dimensions
button_width = yes_button.winfo_reqwidth()
button_height = yes_button.winfo_reqheight()

# Place the buttons initially
yes_button.place(x=window_width // 3, y=window_height // 2)
no_button.place(x=2 * window_width // 3, y=window_height // 2)

# Start the main loop
root.mainloop()
