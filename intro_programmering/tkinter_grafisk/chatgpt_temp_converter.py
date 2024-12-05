import tkinter as tk
from tkinter import ttk

def convert_temperature():
    try:
        input_value = float(entry_input.get())
        input_scale = selected_input.get()
        output_scale = selected_output.get()

        if input_scale == "Celsius":
            if output_scale == "Kelvin":
                result = input_value + 273.15
            elif output_scale == "Fahrenheit":
                result = (input_value * 9/5) + 32
            else:
                result = input_value

        elif input_scale == "Kelvin":
            if output_scale == "Celsius":
                result = input_value - 273.15
            elif output_scale == "Fahrenheit":
                result = (input_value - 273.15) * 9/5 + 32
            else:
                result = input_value

        elif input_scale == "Fahrenheit":
            if output_scale == "Celsius":
                result = (input_value - 32) * 5/9
            elif output_scale == "Kelvin":
                result = (input_value - 32) * 5/9 + 273.15
            else:
                result = input_value

        label_result.config(text=f"Result: {result:.2f} {output_scale}")
    except ValueError:
        label_result.config(text="Please enter a valid number!")

# Create the main window
root = tk.Tk()
root.title("Temperature Converter")
root.geometry("400x300")

# Input Field
label_input = tk.Label(root, text="Enter Temperature:")
label_input.pack(pady=5)
entry_input = tk.Entry(root, width=20)
entry_input.pack(pady=5)

# Input Scale Selection
label_input_scale = tk.Label(root, text="Select Input Scale:")
label_input_scale.pack(pady=5)
selected_input = tk.StringVar(value="Celsius")  # Default selection
frame_input = tk.Frame(root)
frame_input.pack(pady=5)
for scale in ["Celsius", "Kelvin", "Fahrenheit"]:
    btn = ttk.Radiobutton(frame_input, text=scale, value=scale, variable=selected_input)
    btn.pack(side=tk.LEFT, padx=10)

# Output Scale Selection
label_output_scale = tk.Label(root, text="Select Output Scale:")
label_output_scale.pack(pady=5)
selected_output = tk.StringVar(value="Kelvin")  # Default selection
frame_output = tk.Frame(root)
frame_output.pack(pady=5)
for scale in ["Celsius", "Kelvin", "Fahrenheit"]:
    btn = ttk.Radiobutton(frame_output, text=scale, value=scale, variable=selected_output)
    btn.pack(side=tk.LEFT, padx=10)

# Convert Button
btn_convert = tk.Button(root, text="Convert", command=convert_temperature)
btn_convert.pack(pady=10)

# Result Label
label_result = tk.Label(root, text="Result: ")
label_result.pack(pady=10)

# Run the application
root.mainloop()
