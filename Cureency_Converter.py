from tkinter import *
from tkinter import ttk
from tkinter import messagebox


root = Tk()
root.title("Currency_converter")
root.geometry("700x700")
root.config(bg="lightblue")

def convert():
    if amount_entry.get() == "" and rate_entry.get() == "":
        messagebox.showerror("", "Fill all the fields!...")

    elif conversion_entry.get() == "" and home_entry.get() == "":
        messagebox.showinfo("", "fill all the fields!...")


    # Clear converted Entry Box
    converted_entry.delete(0, END)
    # convert
    conversion = float(rate_entry.get()) * float(amount_entry.get())
    # Convert To 2 Decimal
    conversion = round(conversion, 2)
    # Add Commas
    conversion = '{:,}'.format(conversion)
    # update Entry Box
    converted_entry.insert(0, f'{conversion}')


def clear():
    amount_entry.delete(0, END)
    converted_entry.delete(0, END)
    home_entry.delete(0, END)
    conversion_entry.delete(0, END)
    rate_entry.delete(0, END)


home = LabelFrame(text="Your Home Currency", bg="grey")
home.pack(pady=20)

# Home Currency Entry Box
home_entry = Entry(home, font=("Helvetica", 20))
home_entry.pack(pady=10, padx=10)

amount_lable = LabelFrame(text="Amount To Convert", bg="grey")
amount_lable.pack(pady=20)

# Entry box for amount
amount_entry = Entry(amount_lable, font=("Helvatica", 20))
amount_entry.pack(pady=10, padx=10)

# Conversion Currency Frame
conversion = LabelFrame(text="Coversion Currency", bg="grey")
conversion.pack(pady=20)

# Convert to Lable
conversion_lable = Label(conversion, text="Currency To Convert To...", bg="grey")
conversion_lable.pack(pady=10)

# Convert To Entry
conversion_entry = Entry(conversion, font=("Helvatica", 20))
conversion_entry.pack(pady=10, padx=10)

# Rate Lable
rate_lable = Label(conversion, text="Current Conversion Rate...",bg="grey")
rate_lable.pack(pady=10)

# Rate to Entry
rate_entry = Entry(conversion, font=("Helvatica", 20))
rate_entry.pack(pady=10, padx=10)

# Convert Button
convert_button = Button(text="Convert", command=convert, bg="lightgreen")
convert_button.pack(pady=20)

# Clear Button
clear_button = Button(text="Clear", command=clear, bg="lightgreen")
clear_button.pack(pady=10, padx=20)

# Equales Frame
converted_lable = LabelFrame(text="Converted Currency", bg="grey")
converted_lable.pack(pady=20, padx=10)

# Converted Entry
converted_entry = Entry(converted_lable, font=("Helvatica", 20), bd=0)
converted_entry.pack(pady=10, padx=10)

root.mainloop()
