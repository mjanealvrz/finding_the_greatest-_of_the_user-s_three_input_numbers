# Program 3
# Ask user to input 3 numbers. Find and print the greatest number using only if-else statement


# ====================== Actual Code ========================================================================

# Using tkinter and customtkinter for the program's module
import tkinter as tk
from tkinter import Image
import customtkinter as Ctk



def finding_greatest_number():
    global result_label
    def find_greatest():
        num1_entry = int(input_num1_entry.get())
        num2_entry = int(input_num2_entry.get())
        num3_entry = int(input_num3_entry.get())

        if not (num1_entry and num2_entry and num3_entry): 
             result_label.configure(text="Error: Please fill in all fields!")
        else:
            try:
                num1 = float(num1_entry)
                num2 = float(num2_entry)
                num3 = float(num3_entry)

                greatest = max(num1, num2, num3)
                result_label.configure(text=f"Greatest number: {greatest}")
            
            except ValueError:
                result_label.configure(text="Error: Please enter valid numbers!")
            

                        
# Another window
    win = Ctk.CTk()
    win.title("Input three number")
    win.geometry("600x600")
        
# Entry widgets for user's input three numbers
    frame = Ctk.CTkFrame(win, width=900, height=500, fg_color="transparent",border_width=5, border_color="#4F7942", bg_color= "transparent", corner_radius=50)
    frame.place(relx=0.5, rely=0.5, anchor= "center")

    input_num1_label = Ctk.CTkLabel(frame, text="1st input:", width=10)
    input_num1_label.place(relx=0.2, rely=0.3, anchor= "center")
    input_num1_entry = Ctk.CTkEntry(frame )
    input_num1_entry .place(relx=0.4, rely=0.3, anchor="center")

    input_num2_label = Ctk.CTkLabel(frame, text="2nd input:", width=10)
    input_num2_label.place(relx=0.2, rely=0.4, anchor= "center")
    input_num2_entry = Ctk.CTkEntry(frame )
    input_num2_entry .place(relx=0.4, rely=0.4, anchor="center")

    input_num3_label = Ctk.CTkLabel(frame, text="3rd input:", width=10)
    input_num3_label.place(relx=0.2, rely=0.5, anchor= "center")
    input_num3_entry = Ctk.CTkEntry(frame )
    input_num3_entry .place(relx=0.4, rely=0.5, anchor="center")

    find_button = Ctk.CTkButton(frame, text= "Find Greatest!",  fg_color="#009E60", border_color="#4F7942", width=10,border_width= 5, command=find_greatest)
    find_button.place(relx=0.5, rely=0.7, anchor="center")


    result_label = Ctk.CTkLabel(frame, text="Greatest number: ", width=20)
    result_label.place(relx=0.5, rely=0.6)


# Run the another mainloop
    win.mainloop()



       



# Welcome window
window = Ctk.CTk()
window.title("Numeria")
window.geometry("600x600")

# Set background image
background_image = tk.PhotoImage(file="Numeria.png")
background_label = tk.Label(window, image=background_image)
background_label.place(relwidth=1, relheight=1)

# Enter button to take to another window
enter_button = Ctk.CTkButton(window, text="Click to Enter",  fg_color="#009E60",border_color="#4F7942", width=10,border_width= 5, command=finding_greatest_number)
enter_button.place(relx=0.5, rely=0.7, anchor="center")

# Run the mainloop
window.mainloop()

# Destroy window
window.destroy()







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
