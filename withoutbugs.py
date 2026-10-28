import tkinter as tk

# Initialize main window
window = tk.Tk()
window.title("FalseCulator")
window_width = 400
window_height = 500
window.resizable(True, True)

# Get screen dimensions and center the window
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
center_x = int(screen_width / 2 - window_width / 2)
center_y = int(screen_height / 2 - window_height / 2)
window.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

# Set background color (alpha set to 1.0 so it's fully visible)
window.configure(bg='#075b4d')
window.attributes('-alpha', 1.0)

# Title Label
title_label = tk.Label(master=window, text="FalseCulator", font='Calibri 24', bg='#075b4d', fg='white')
title_label.pack(pady=10)

# Input frame
input_frame = tk.Frame(master=window, bg='#075b4d')
entry = tk.Entry(master=input_frame)
button_calc = tk.Button(master=input_frame, text="Calculate", command=lambda: print("Calculate clicked"))
entry.pack(side='left', padx=10)
button_calc.pack(side='left')
input_frame.pack(pady=10)

# Number and Control Buttons
buttons = [
    ("C", "yellow"),
    ("1", "green"), ("2", "green"), ("3", "green"),
    ("4", "green"), ("5", "green"), ("6", "green"),
    ("7", "green"), ("8", "green"), ("9", "green")
]

for (text_val, color) in buttons:
    btn = tk.Button(
        window,
        text=text_val,
        activebackground=color,
        padx=5,
        pady=5,
        width=5,
        wraplength=100
    )
    btn.pack(padx=5, pady=2)

# Text widget for output/logs
text_box = tk.Text(window, height=4, width=40)
text_box.pack(pady=10)

# Run the application
window.mainloop()
