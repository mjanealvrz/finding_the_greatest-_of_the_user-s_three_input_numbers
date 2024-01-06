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
