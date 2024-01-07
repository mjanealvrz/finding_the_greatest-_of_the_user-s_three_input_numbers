import tkinter as tk
from tkinter import Image
import customtkinter as Ctk

def enter_button()
    
 #Welcome window   
window = Ctk.CTk()
window.title("Numeria")
window.geometry("600x600")

background_image = tk.PhotoImage(file="Numeria.png")
background_label = tk.Label(window, image=background_image)
background_label.place(relwidth=1, relheight=1)



enter_button = Ctk.CTkButton(window, text="Click to Enter",  fg_color="#009E60",border_color="#4F7942", width=10,border_width= 5, command=enter_button)
enter_button.place(relx=0.5, rely=0.7, anchor="center")

window.mainloop()