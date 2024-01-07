import tkinter as tk
from tkinter import PhotoImage
import customtkinter as Ctk

size_border_width = 5

def welcome_page():
     win = Ctk.CTk()
     win.title("Fruits Haven Boutique")
     win.geometry("1000x1000")
     scg_image = tk.PhotoImage(file="secondbg.png")
     scg_label = tk.Label(win, image=scg_image)
     scg_label.place(relwidth=1, relheight=1)

     frame = Ctk.CTkFrame(win, width=900, height=500, fg_color="transparent",border_width=size_border_width, border_color="#4F7942", bg_color= "transparent", corner_radius=50)
     frame.place(relx=0.5, rely=0.5, anchor= "center")

     lexenda_font= Ctk.CTkFont(family="Impact",size=50,weight="bold")
     label = Ctk.CTkLabel(frame, text= "Welcome to Fruits Haven Boutique!", font=lexenda_font,bg_color="transparent", fg_color="transparent", text_color="#013220")
     label.place(relx=0.5, rely=0.5, anchor= "center")
     helv367 = Ctk.CTkFont(family="Helvetica",size=20,weight="bold")
     click_button =Ctk.CTkButton(frame, text="Open Shop",fg_color="#009E60",border_color="#4F7942", width=50, height= 20,border_width=size_border_width, font=helv367)
     click_button.place(relx=0.5, rely=0.7, anchor="center")

     win.mainloop()
