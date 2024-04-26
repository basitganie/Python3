import tkinter as tk 
from tkinter import messagebox, simpledialog 

root = tk.Tk()
root.withdraw

response = messagebox.askyesno("Request","Are you free")

if response:
        response = messagebox.askyesno("Request", "can we hangout")
        respond = messagebox.showinfo("ok", "Cool")
    
else:
      response = messagebox.showinfo("Error 404","Ok" )
    

    
   
      
           
    
    
    
    
    
    
    
    