import os
import tkinter
import threading

MOVE_KEYS = {
    'w': [0, -10],
    'e': [0, 0],
    'a': [-10, 0],
    'q': [0, 0],
    'x': [0, 10],
    'z': [0, 0],
    'd': [10, 0],
    'c': [0, 0],
}

LEFT_KEYS = [ "f", "u" ]
RIGHT_KEYS = [ "r", "h" ]

PRESSED = [ False, False ]

def move_mouse(dx, dy):
    if dx == dy == 0:
        return
    os.system(f"echo mousemove {dx} {dy} | dotoolc")

def press_mouse(i, s):
    if PRESSED[i] == s:
        return
    PRESSED[i] = s
    os.system(f"echo button{'down' if s else 'up'} {'right' if i else 'left'} | dotoolc")

root = tkinter.Tk(className="myTkWindows")
root.title("myTkWindow")

label = tkinter.Label(root, text="Нажмите любую клавишу", font=("Arial", 16))
label.pack(padx=40, pady=40)

def key_handler(event):
    print(event.char)
    if event.char in MOVE_KEYS:
        dx, dy = MOVE_KEYS[event.char]
        move_mouse(dx, dy)
    if event.char in LEFT_KEYS:
        press_mouse(0, bool(LEFT_KEYS.index(event.char)))
    if event.char in RIGHT_KEYS:
        press_mouse(1, bool(RIGHT_KEYS.index(event.char)))

root.bind("<Key>", key_handler)

def func():
    os.system('swaymsg [title="myTkWindow"] floating enable')
    os.system('swaymsg [title="myTkWindow"] sticky enable')
    os.system('swaymsg [title="myTkWindow"] focus')
    threading.Timer(0.05,func).start()

func()

threading.Thread(target=lambda: os.system("dotoold")).start()

root.mainloop()
