# Program 3
# Ask user to input 3 numbers. Find and print the greatest number using only if-else statement


# ====================== Actual Code ========================================================================

# Using tkinter and customtkinter for the program's module
import tkinter as tk
from tkinter import PhotoImage
import customtkinter as Ctk

# Set appearance mode
Ctk.set_appearance_mode("light")

# Set color theme
Ctk.set_default_color_theme("green")


def finding_greatest_number():
    global result_label
    def find_greatest():

        # retrieve input values in the entry fields
        # convert input values to integers
        try:
            number1_entry = input_number1_entry.get().strip()
            number2_entry = input_number2_entry.get().strip()
            number3_entry = input_number3_entry.get().strip()

            # if the fields are empty it will display error
            if len(number1_entry) == 0 or len(number2_entry) == 0 or len(number3_entry) == 0:
                result_label.configure(text="Error: Please fill in all fields!")
            else:
                    # find the maximum value 
                    greatest = int( max(number1_entry, number2_entry, number3_entry))
                    # display the greatest result
                    result_label.configure(text=f"Greatest number: {greatest}")

         # display the error in the result label            
        except ValueError:
            result_label.configure(text="Error: Please enter valid numbers!")
            
# Create  window
    win = Ctk.CTk()
    win.title("Input three number")
    win.geometry("600x600")
       
# make GUI components (button, entry fields, and labels).
    # specify where GUI items should be placed in the window
    # attach the method find_greatest() to the button.

    frame = Ctk.CTkFrame(win, width=500, height=500, fg_color="transparent",border_width=5, border_color="#4F7942", bg_color="#D1FFBD")
    frame.place(relx=0.5, rely=0.5, anchor= "center")

    input_number1_label = Ctk.CTkLabel(frame, text="1st input:",font=helv37, width=10, bg_color="#D1FFBD")
    input_number1_label.place(relx=0.2, rely=0.3, anchor= "center")
    input_number1_entry = Ctk.CTkEntry(frame )
    input_number1_entry.place(relx=0.5, rely=0.3, anchor="center")

    input_number2_label = Ctk.CTkLabel(frame, text="2nd input:",font=helv37, width=10, bg_color="#D1FFBD")
    input_number2_label.place(relx=0.2, rely=0.4, anchor= "center")
    input_number2_entry = Ctk.CTkEntry(frame )
    input_number2_entry.place(relx=0.5, rely=0.4, anchor="center")

    input_number3_label = Ctk.CTkLabel(frame, text="3rd input:",font=helv37, width=10, bg_color="#D1FFBD")
    input_number3_label.place(relx=0.2, rely=0.5, anchor= "center")
    input_number3_entry = Ctk.CTkEntry(frame )
    input_number3_entry.place(relx=0.5, rely=0.5, anchor="center")

    find_button = Ctk.CTkButton(frame, text= "Find the Greatest!",  fg_color="#009E60", border_color="#4F7942",height=30, width=30, font= helv38, border_width= 2, command=find_greatest)
    find_button.place(relx=0.5, rely=0.6, anchor="center")


    result_label = Ctk.CTkLabel(frame, text="Greatest Number:   ",font=helv36, width=20, bg_color="#D1FFBD")
    result_label.place(relx=0.1, rely=0.7)


# Run the another mainloop
    win.mainloop()
# Destroy the window
    win.destroy()

# Welcome window
window = Ctk.CTk()
window.title("Numeria")
window.geometry("600x600")

# Overall font
helv36 = Ctk.CTkFont(family="Helvetica",size=25,weight="bold")
helv37 = Ctk.CTkFont(family="Helvetica",size=15,weight="bold")
helv38 = Ctk.CTkFont(family="Helvetica",size=20,weight="bold")

# Set background image
background_image = tk.PhotoImage(file="Numeria.png")
background_label = tk.Label(window, image=background_image)
background_label.place(relwidth=1, relheight=1)

# Enter button to take to another window
enter_button = Ctk.CTkButton(window, text="Click to Enter", font= helv36,fg_color="#009E60",border_color="#D0F0C0", width=30,border_width= 2, command=finding_greatest_number)
enter_button.place(relx=0.5, rely=0.7, anchor="center")

# Run the mainloop
window.mainloop()





# pseudocode

# -Ask the user to input first number
#first_input_number = int(input("\nInput first number: "))

# -Ask the user to input second number
#second_input_number = int(input("\nInput second number: "))

# -Ask the user to input the third number
#third_input_number = int(input("\nInput third number: "))

# -Compare the numbers to find the greatest number
#if first_input_number >= second_input_number and first_input_number >= third_input_number:
    #greatest_number = first_input_number
#elif second_input_number >= first_input_number and second_input_number >= third_input_number:
    #greatest_number = second_input_number
#else: greatest_number = third_input_number 

# -Print the greatest number
#print(f"The greatest number is: {greatest_number}")
