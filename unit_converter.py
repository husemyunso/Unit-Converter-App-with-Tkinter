import tkinter as tk
from tkinter import ttk


# Conversion Functions
def convert_units():
    try:
        input_value = float(entry_input.get())
        unit_from = combo_from.get()
        unit_to = combo_to.get()

        # Length Conversion
        length_units = {"Meters": 1, "Kilometers": 0.001, "Centimeters": 100, "Inches": 39.3701, "Feet": 3.28084}
        weight_units = {"Kilograms": 1, "Grams": 1000, "Pounds": 2.20462, "Ounces": 35.274}
        temp_units = {"Celsius": lambda x: x, "Fahrenheit": lambda x: (x * 9/5) + 32, "Kelvin": lambda x: x + 273.15}

        if category.get() == "Length":
            factor_from = length_units[unit_from]
            factor_to = length_units[unit_to]
            result = input_value * (factor_to / factor_from)

        elif category.get() == "Weight":
            factor_from = weight_units[unit_from]
            factor_to = weight_units[unit_to]
            result = input_value * (factor_to / factor_from)

        elif category.get() == "Temperature":
            if unit_from == "Celsius" and unit_to == "Fahrenheit":
                result = (input_value * 9/5) + 32
            elif unit_from == "Celsius" and unit_to == "Kelvin":
                result = input_value + 273.15
            elif unit_from == "Fahrenheit" and unit_to == "Celsius":
                result = (input_value - 32) * 5/9
            elif unit_from == "Fahrenheit" and unit_to == "Kelvin":
                result = ((input_value - 32) * 5/9) + 273.15
            elif unit_from == "Kelvin" and unit_to == "Celsius":
                result = input_value - 273.15
            elif unit_from == "Kelvin" and unit_to == "Fahrenheit":
                result = ((input_value - 273.15) * 9/5) + 32
            else:
                result = input_value

        label_result['text'] = f"Result: {round(result, 4)} {unit_to}"

    except ValueError:
        label_result['text'] = "Invalid Input!"


# Update unit options based on category
def update_units(event):
    selected_category = category.get()

    if selected_category == "Length":
        units = ["Meters", "Kilometers", "Centimeters", "Inches", "Feet"]
    elif selected_category == "Weight":
        units = ["Kilograms", "Grams", "Pounds", "Ounces"]
    elif selected_category == "Temperature":
        units = ["Celsius", "Fahrenheit", "Kelvin"]

    combo_from['values'] = units
    combo_to['values'] = units
    combo_from.current(0)
    combo_to.current(1)


# Tkinter Setup
root = tk.Tk()
root.title("Unit Converter")
root.geometry("460x400")
root.configure(bg="lightblue")

# Title Label
label_title = tk.Label(root, text="Unit Converter", font=("Arial", 18, "bold"), bg="lightblue")
label_title.pack(pady=10)

# Category Selection
category = ttk.Combobox(root, values=["Length", "Weight", "Temperature"], state="readonly", font=("Arial", 12))
category.current(0)
category.bind("<<ComboboxSelected>>", update_units)
category.pack(pady=10)

# Input Section
frame_input = tk.Frame(root, bg="lightblue")
frame_input.pack(pady=10)

entry_input = tk.Entry(frame_input, width=10, font=("Arial", 14))
entry_input.grid(row=0, column=0, padx=10)

combo_from = ttk.Combobox(frame_input, values=[], state="readonly", font=("Arial", 12), width=12)
combo_from.grid(row=0, column=1, padx=10)

label_to = tk.Label(frame_input, text="to", font=("Arial", 12), bg="lightblue")
label_to.grid(row=0, column=2)

combo_to = ttk.Combobox(frame_input, values=[], state="readonly", font=("Arial", 12), width=12)
combo_to.grid(row=0, column=3, padx=10)

# Result Section
btn_convert = tk.Button(root, text="Convert", font=("Arial", 12, "bold"), bg="darkblue", fg="white", command=convert_units)
btn_convert.pack(pady=20)

label_result = tk.Label(root, text="Result: ", font=("Arial", 14), bg="lightblue")
label_result.pack(pady=10)

# Footer
label_footer = tk.Label(root, text="Created with ❤️By Husem", font=("Arial", 10), bg="lightblue")
label_footer.pack(side="bottom", pady=10)

# Initialize Unit Options
update_units(None)

# Run the App
root.mainloop()
