# Oto przykładowy kod na prostego auto clickera w pythonie z udziałem mojej ulubionej persony czyli Stuartem

import tkinter as tk
from tkinter import ttk
import pyautogui
import threading
import time
import keyboard  

running = False
stary_w_oknie_zycia = False
klikanie = None

def start_clicking():
    try:
        cps = float(cps_var.get())
        interval = 1 / cps
    except ValueError:
        cps_label.config(text="Liczby kurwo")
        return
    
    # Stuu Stuu Stuu 

    burton = mouse_burton_var.get()
    if burton == "Lewy":
        btn = "left"
    elif burton == "Prawy":
        btn = "right"
    
    global running
    while running:
        if not stary_w_oknie_zycia:
            pyautogui.click(button=btn)
        time.sleep(interval)

def toggle_clicking():
    global running, klikanie
    if running:
        running = False
        if klikanie and klikanie.is_alive(): 
            klikanie.join() 
        start_burton.config(state=tk.NORMAL)
        stop_burton.config(state=tk.DISABLED)
    else:
        running = True
        klikanie = threading.Thread(target=start_clicking)
        klikanie.start()
        start_burton.config(state=tk.DISABLED)
        stop_burton.config(state=tk.NORMAL)

def on_enter_key(event=None):
    toggle_clicking()

def on_mouse_enter(event):
    global stary_w_oknie_zycia
    stary_w_oknie_zycia = True

def on_mouse_leave(event):
    global stary_w_oknie_zycia
    stary_w_oknie_zycia = False

root = tk.Tk()
root.title("Auto Clicker Stuarta v2")
cps_var = tk.StringVar(value="30")
mouse_burton_var = tk.StringVar(value="Lewy")


# Boli to w oczy? (specialnie tak HIHI)
cps_label = ttk.Label(root, text="CPS:")
cps_label.grid(row=0, column=0, padx=5, pady=5)
cps_entry = ttk.Entry(root, textvariable=cps_var)
cps_entry.grid(row=0, column=1, padx=5, pady=5)
mouse_burton_label = ttk.Label(root, text="Pedal:")
mouse_burton_label.grid(row=1, column=0, padx=5, pady=5)
mouse_burton_combo = ttk.Combobox(root, textvariable=mouse_burton_var, values=["Lewy", "Prawy"], state="readonly")
mouse_burton_combo.grid(row=1, column=1, padx=5, pady=5)
start_burton = ttk.Button(root, text="Start", command=toggle_clicking)
start_burton.grid(row=2, column=0, padx=5, pady=5)
stop_burton = ttk.Button(root, text="Stop", command=toggle_clicking, state=tk.DISABLED)
stop_burton.grid(row=2, column=1, padx=5, pady=5)

root.bind('<Return>', on_enter_key)
root.bind('<Enter>', on_mouse_enter)
root.bind('<Leave>', on_mouse_leave)

keyboard.add_hotkey('enter', on_enter_key)
root.mainloop()
keyboard.unhook_all_hotkeys()


# tak wiem mam dziwne nazwy zmiennych ale nie wiem jak inaczej XDDD
