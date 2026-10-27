import tkinter as tk

window = tk.Tk()

window.title("FalseCulator")
window_width = 400
window_height = 300

# get the screen dimension
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

# find the center point
center_x = int(screen_width/2 - window_width / 2)
center_y = int(screen_height/2 - window_height / 2)

window.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

window.attributes('-alpha',0.1)

tittle_label = tk.Label(master = window, text = "My Mind is Broken", font = 'Calibri 24')
tittle_label.pack()

num1 = input("Enter the first number")
num2 = input("Enter the second number")

if operator == "+":
    result == num1 + num2
    print(round(result, 3))
    
elif operator == "-":
    result == num1 - num2
    print(round(result, 3))
    
elif operator == "*":
    result == num1 * num2
    print(round(result, 3))
    
elif operator == "//":
    result == num1 // num2
    print(round(result, 3))

else: 
    print(f"[operator] is not a valid operator")
    
# input field (part)

input_frame = tk.Frame(master = window)
entry = tk.Entry(master = input_frame)
button = tk.Button(master = input_frame, text = "Calculate", command = print(operator))
entry.pack(side = 'left', padx = 10)
button.pack(side = 'left')
input_frame.pack(pady = 10)

window.configure(bg='#075b4d')

button = tk.Button(
window,
text = "C",
activebackground = "yellow",
padx=5,
pady=5,
width=5,
wraplength=100)

button.pack(padx=5, pady=5)

button = tk.Button(
window,
text = "1",
activebackground = "green",
padx=5,
pady=5,
width=5,
wraplength=100)

button.pack(padx=5, pady=5)


button = tk.Button(
window,
text = "2",
activebackground = "green",
padx=5,
pady=5,
width=5,
wraplength=100)

button.pack(padx=5, pady=5)

button = tk.Button(
window,
text = "3",
activebackground = "green",
padx=5,
pady=5,
width=5,
wraplength=100)

button.pack(padx=5, pady=5)

button = tk.Button(
window,
text = "4",
activebackground = "green",
padx=5,
pady=5,
width=5,
wraplength=100)

button.pack(padx=5, pady=5)

button = tk.Button(
window,
text = "5",
activebackground = "green",
padx=5,
pady=5,
width=5,
wraplength=100)

button.pack(padx=5, pady=5)

button = tk.Button(
window,
text = "6",
activebackground = "green",
padx=5,
pady=5,
width=5,
wraplength=100)

button.pack(padx=5, pady=5)

button = tk.Button(
window,
text = "7",
activebackground = "green",
padx=5,
pady=5,
width=5,
wraplength=100)

button.pack(padx=5, pady=5)

button = tk.Button(
window,
text = "8",
activebackground = "green",
padx=5,
pady=5,
width=5,
wraplength=100)

button.pack(padx=5, pady=5)

button = tk.Button(
window,
text = "9",
activebackground = "green",
padx=5,
pady=5,
width=5,
wraplength=100)

button.pack(padx=5, pady=5)

window.mainloop()
