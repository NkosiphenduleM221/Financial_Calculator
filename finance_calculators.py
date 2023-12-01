import math
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import PIL


# Function to validate user input
def get_valid_input(prompt, entry_widget, input_type=float, min_value=None, allow_zero=False):
    try:
        user_input = float(entry_widget.get().replace(" ", ""))
        if min_value is not None and user_input < min_value:
            messagebox.showerror("Error", f"{prompt.split(':')[0]} must be greater than or equal to {min_value}.")
            return None
        if not allow_zero and user_input <= 0:
            messagebox.showerror("Error", f"{prompt.split(':')[0]} must be greater than zero.")
            return None
        return user_input
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number.")
        return None

# Function to calculate investment or bond
def calculate():
    global interest_type  # Declare interest_type as global

    choice = calculation_choice.get()
    if choice == 1:  # Investment calculation
        amount = get_valid_input("Enter the amount of money (R): ", principle_entry, min_value=10)
        if amount is None:
            return

        rate = get_valid_input("Enter the interest rate (%): ", interest_entry)
        if rate is None:
            return
        rate /= 100

        years = get_valid_input("Enter the number of years: ", years_entry, int)
        if years is None:
            return

        interest_type_val = interest_type.get()

        if interest_type_val == 1:  # Simple Interest calculation
            final_amount = amount * (1 + rate * years)
        else:  # Compound Interest calculation
            final_amount = amount * (1 + rate) ** years

        result_label.config(text=f"Your investment will be worth: R{final_amount:.2f}")

    elif choice == 2:  # Bond calculation
        present_value = get_valid_input("Enter the present value of the house (R): ", principle_entry, min_value=100)
        if present_value is None:
            return

        annual_rate = get_valid_input("Enter the annual interest rate(%): ", interest_entry)
        if annual_rate is None:
            return
        monthly_rate = annual_rate / 12

        years = get_valid_input("Enter the number of years for bond repayment: ", years_entry, int)
        if years is None:
            return

        n = years * 12  # Total number of payments
        repayment = (monthly_rate * present_value) / (1 - (1 + monthly_rate) ** -n)
        
        result_label.config(text=f"Your monthly bond repayment will be: R{repayment:.2f}")

def show_investment_fields():
    clear_entry()
    interest_type_frame.pack()

# Function to display bond fields
def show_bond_fields():
    clear_entry()
    interest_type_frame.pack_forget()
    
# Function to clear entry fields
def clear_entry():
    principle_entry.delete(0, tk.END)
    interest_entry.delete(0, tk.END)
    years_entry.delete(0, tk.END)

# Main function to create the GUI
def main():
    global principle_entry, interest_entry, years_entry, calculation_choice, result_label, interest_type_frame, interest_type
    
    root = tk.Tk()
    root.title("Financial Calculator")

    welcome_label = tk.Label(root, text="Welcome to the Financial Calculator", bg='lightgreen')
    welcome_label.pack()
    
    root.configure(bg='lightgreen')

    # Add an image
    # Load the image and resize it
    welcome_image = Image.open("Devs.png")
    welcome_image = welcome_image.resize((300, 300), PIL.Image.LANCZOS)  # Resizing the image
    welcome_image = ImageTk.PhotoImage(welcome_image)

    # Create a label to display the image
    welcome_image_label = tk.Label(root, image=welcome_image)
    welcome_image_label.pack()
    
    calculate_button = tk.Button(root, text="Calculate", command=calculate, bg='lightgreen')
    calculate_button.pack()
    
    clear_button = tk.Button(root, text="Clear Entry", command=clear_entry, bg='lightgreen')
    clear_button.pack()

    calculation_choice = tk.IntVar()

    investment_label = tk.Label(root, text="Choose type of calculation:", bg='lightgreen')
    investment_label.pack()

    investment_radio1 = tk.Radiobutton(root, text="Investment", variable=calculation_choice, value=1, command=show_investment_fields, bg='lightgreen')
    investment_radio1.pack()

    investment_radio2 = tk.Radiobutton(root, text="Bond", variable=calculation_choice, value=2, command=show_bond_fields, bg='lightgreen')
    investment_radio2.pack()

    principle_frame = tk.Frame(root)
    principle_frame.pack()

    principle_label = tk.Label(principle_frame, text="Enter the amount (R):", bg='lightgreen')
    principle_label.pack(side=tk.LEFT)

    principle_entry = tk.Entry(principle_frame)
    principle_entry.pack(side=tk.LEFT)

    interest_frame = tk.Frame(root)
    interest_frame.pack()

    interest_label = tk.Label(interest_frame, text="Enter the annual interest rate (%):", bg='lightgreen')
    interest_label.pack(side=tk.LEFT)

    interest_entry = tk.Entry(interest_frame)
    interest_entry.pack(side=tk.LEFT)

    years_frame = tk.Frame(root)
    years_frame.pack()

    years_label = tk.Label(years_frame, text="Enter the number of years:", bg='lightgreen')
    years_label.pack(side=tk.LEFT)

    years_entry = tk.Entry(years_frame)
    years_entry.pack(side=tk.LEFT)

    result_label = tk.Label(root, text="          ", bg='lightgreen')
    result_label.pack()

    interest_type_frame = tk.Frame(root, bg='lightgreen')  # Define the interest_type_frame
    interest_type_frame.pack()  # Pack the interest_type_frame

    # Define the interest_type variable
    interest_type = tk.IntVar()

    interest_type_label = tk.Label(interest_type_frame, text="Choose interest type:", bg='lightgreen')
    interest_type_label.pack()

    interest_radio1 = tk.Radiobutton(interest_type_frame, text="Simple Interest", variable=interest_type, value=1, bg='lightgreen')
    interest_radio1.pack()

    interest_radio2 = tk.Radiobutton(interest_type_frame, text="Compound Interest", variable=interest_type, value=2, bg='lightgreen')
    interest_radio2.pack()

    root.mainloop()

if __name__ == "__main__":
    main()
