import tkinter as tk

root = tk.Tk()

root.title("FalseCulator")
window_width = 400
window_height = 300

# get the screen dimension
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# find the center point
center_x = int(screen_width/2 - window_width / 2)
center_y = int(screen_height/2 - window_height / 2)

root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

root.attributes('-alpha',0.1)

tittle_label = tk.Label(master = window, text = "My Mind is Broken", font = 'Calibri 24')
tittle_label.pack()

root.configure(bg='#075b4d')

button = tk.Button(
root, 
text = "C",
activebackground = "yellow",
padx=5,
pady=5,
width=5,
wraplength=100)

button.pack(padx=5, pady=5)

button = tk.Button(
root, 
text = "1",
activebackground = "green",
padx=5,
pady=5,
width=5,
wraplength=100)

button.pack(padx=5, pady=5)


button = tk.Button(
root, 
text = "2",
activebackground = "green",
padx=5,
pady=5,
width=5,
wraplength=100)

button.pack(padx=5, pady=5)

button = tk.Button(
root, 
text = "3",
activebackground = "green",
padx=5,
pady=5,
width=5,
wraplength=100)

button.pack(padx=5, pady=5)

button = tk.Button(
root, 
text = "4",
activebackground = "green",
padx=5,
pady=5,
width=5,
wraplength=100)

button.pack(padx=5, pady=5)

button = tk.Button(
root, 
text = "5",
activebackground = "green",
padx=5,
pady=5,
width=5,
wraplength=100)

button.pack(padx=5, pady=5)

button = tk.Button(
root, 
text = "6",
activebackground = "green",
padx=5,
pady=5,
width=5,
wraplength=100)

button.pack(padx=5, pady=5)

button = tk.Button(
root, 
text = "7",
activebackground = "green",
padx=5,
pady=5,
width=5,
wraplength=100)

button.pack(padx=5, pady=5)

button = tk.Button(
root, 
text = "8",
activebackground = "green",
padx=5,
pady=5,
width=5,
wraplength=100)

button.pack(padx=5, pady=5)

button = tk.Button(
root, 
text = "9",
activebackground = "green",
padx=5,
pady=5,
width=5,
wraplength=100)

button.pack(padx=5, pady=5)

root.mainloop()     
