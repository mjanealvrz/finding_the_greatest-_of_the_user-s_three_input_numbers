# Program 3
# Ask user to input 3 numbers. Find and print the greatest number using only if-else statement

# pseudocode

# -Ask the user to input first number
first_input_number = int(input("\nInput first number: "))

# -Ask the user to input second number
second_input_number = int(input("\nInput second number: "))

# -Ask the user to input the third number
third_input_number = int(input("\nInput third number: "))

# -Compare the numbers to find the greatest number
if first_input_number >= second_input_number and first_input_number >= third_input_number:
    greatest_number = first_input_number
elif second_input_number >= first_input_number and second_input_number >= third_input_number:
    greatest_number = second_input_number
else: greatest_number = third_input_number 

# -Print the greatest number
print(f"The greatest number is: {greatest_number}")

#----------------------------------------------------------------------------------------------------------------

# Using tkinter and customtkinter for the program's module
import tkinter as tk
from tkinter import Image
import customtkinter as Ctk

# Welcome window
window = Ctk.CTk()
window.title("Numeria")
window.geometry("600x600")

background_image = tk.PhotoImage(file="Numeria.png")
background_label = tk.Label(window, image=background_image)
background_label.place(relwidth=1, relheight=1)

enter_button = Ctk.CTkButton(window, text="Click to Enter",  fg_color="#009E60",border_color="#4F7942", width=10,border_width= 5, command=enter_button)
enter_button.place(relx=0.5, rely=0.7, anchor="center")

window.mainloop()





