import random
import tkinter as tk
from tkinter import messagebox

# Function to shuffle names and ensure no one is paired with themselves
def shuffle_names(names):
    if len(names) < 2:
        return "The list of names is not long enough!"
    
    shuffled_names = names[:]
    random.shuffle(shuffled_names)
    
    # Ensure no one is paired with themselves
    for i in range(len(names)):
        if names[i] == shuffled_names[i]:
            return shuffle_names(names)  # Reshuffle if anyone is paired with themselves
    
    # Assign names
    assignments = {}
    for i in range(len(names)):
        assignments[names[i]] = shuffled_names[i]
    
    return assignments

# Tkinter UI
def add_name():
    name = entry.get()
    if name and name not in names_listbox.get(0, tk.END):
        names_listbox.insert(tk.END, name)
    entry.delete(0, tk.END)

def assign_shuffled_names():
    names = names_listbox.get(0, tk.END)
    if len(names) < 2:
        messagebox.showwarning("Error", "Please enter at least 2 names.")
        return
    result = shuffle_names(list(names))
    if isinstance(result, str):  # Error handling
        messagebox.showerror("Error", result)
    else:
        output_text.delete(1.0, tk.END)
        for giver, receiver in result.items():
            output_text.insert(tk.END, f"{giver} → {receiver}\n")

# Main window
root = tk.Tk()
root.title("Name Shuffler")
root.configure(bg="lightblue") #color

# Input field
entry = tk.Entry(root, width=40)
entry.pack(pady=10)

# Add name button
add_button = tk.Button(root, text="Add Name", command=add_name,bg="green", fg="white")
add_button.pack(pady=5)

# Listbox to display entered names
names_listbox = tk.Listbox(root, width=40, height=10)
names_listbox.pack(pady=10)

# Assign Shuffle Names button
assign_button = tk.Button(root, text="Shuffle and Assign Names", command=assign_shuffled_names,bg="orange", fg="black")
assign_button.pack(pady=10)

# Output area
output_text = tk.Text(root, width=40, height=10)
output_text.pack(pady=10)

# Start the Tkinter event loop
root.mainloop()
