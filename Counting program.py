import tkinter as tk
import keyboard

counters = {"w": 0, "a": 0, "s": 0, "d": 0, "space": 0}
key_states = {"w": False, "a": False, "s": False, "d": False, "space": False}

def press_key(key):
    if key_states[key.name] == False:

        counters[key.name] += 1

        key_states[key.name] = True

        buttons[key.name].config(text=f"{key.name.upper()}: {counters[key.name]}", bg="Gray")

        root.after(100, lambda: buttons[key.name].config(bg="SystemButtonFace"))

def release_key(key):
    if key_states[key.name] == True:

        key_states[key.name] = False


root = tk.Tk()
root.title("Keyboard Counter")


buttons = {}
buttons["w"] = tk.Button(root, text=f"W: {counters['w']}", width=10, height=3)
buttons["w"].grid(row=0, column=1)
buttons["a"] = tk.Button(root, text=f"A: {counters['a']}", width=10, height=3)
buttons["a"].grid(row=1, column=0)
buttons["s"] = tk.Button(root, text=f"S: {counters['s']}", width=10, height=3)
buttons["s"].grid(row=1, column=1)
buttons["d"] = tk.Button(root, text=f"D: {counters['d']}", width=10, height=3)
buttons["d"].grid(row=1, column=2)
buttons["space"] = tk.Button(root, text=f"SPACE: {counters['space']}", width=24, height=3)
buttons["space"].grid(row=2, column=0, columnspan=3)

for key in counters.keys():
    keyboard.on_press_key(key, press_key)
    keyboard.on_release_key(key, release_key)


root.mainloop()

