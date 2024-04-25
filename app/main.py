import tkinter as tk
from tkinter import Scale, HORIZONTAL, Label, Button, Entry
import subprocess
import re


def on_slider_change(event):
    # Update the entry with the slider value
    power_value_var.set(slider.get())


def on_entry_change(*args):
    # Update the slider with the entry value
    slider.set(power_value_var.get())


def set_power_limit():
    # Get the power value from the slider
    power_value = power_value_var.get()
    command = ["sudo", "nvidia-smi", "-pl", str(power_value)]
    subprocess.run(command)
    # Refresh the current power limit display after setting
    display_current_power_limit()


def display_current_power_limit():
    # Command to fetch the current power limit
    command = ["nvidia-smi", "-q", "-d", "POWER"]
    # Execute the command and capture the output
    result = subprocess.run(command, text=True, capture_output=True)
    # Parse the output to find the power limit
    lines = result.stdout.split('\n')
    power_limit_line = next((line for line in lines if "Power Limit" in line), "Power Limit: Not found")
    # Extract just the numerical value from the line
    power_limit_value = re.search(r':\s*([\d\.]+)\s*W', power_limit_line)
    if power_limit_value:
        current_power_label.config(text="Current Power Limit: " + power_limit_value.group(1) + " W")
    else:
        current_power_label.config(text=power_limit_line.strip())


def create_gui():
    global slider, current_power_label, power_value_var
    # Create the main window
    window = tk.Tk()
    window.title("NVIDIA Power")

    # Set padding for the window
    window['padx'] = 40
    window['pady'] = 40

    # Create a StringVar to synchronize the slider and the entry
    power_value_var = tk.StringVar(value='169')

    # Horizontal slider initialized to 169W
    slider = Scale(window, from_=0, to=225, orient=HORIZONTAL, variable=power_value_var, command=on_slider_change,
                   showvalue=0, length=300)
    slider.grid(row=0, column=1, padx=(0, 10), pady=10, sticky='ew')

    # Entry to display and set the power value
    power_entry = Entry(window, textvariable=power_value_var, width=5)
    power_entry.grid(row=0, column=2, padx=5, pady=10, sticky='w')
    power_value_var.trace("w", on_entry_change)

    # Unit label
    unit_label = Label(window, text="(W)")
    unit_label.grid(row=0, column=3, padx=5, pady=10, sticky='w')

    # Button to set power limit
    Button(window, text="Set Power Limit", command=set_power_limit).grid(row=0, column=4, padx=5, pady=5)

    # Label to display the current power limit
    current_power_label = Label(window, text="")
    current_power_label.grid(row=1, column=0, columnspan=5, padx=5, pady=5)

    # Initialize the display of the current power limit
    display_current_power_limit()

    # Configure the grid columns
    window.grid_columnconfigure(1, weight=1)

    # Start the GUI event loop
    window.mainloop()


# Run the GUI
create_gui()
