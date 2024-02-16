# Importiere das Tkinter-Modul
import tkinter as tk

# Erstelle eine Funktion, die etwas macht, wenn der Button geklickt wird
def plus_action():
    print("Plus geklickt")

# Erstelle ein Fenster
root = tk.Tk()

# Erstelle ein Canvas-Element, um das Plus-Symbol zu zeichnen
canvas = tk.Canvas(root, width=100, height=100)
canvas.pack()

# Zeichne zwei Linien, die sich kreuzen
canvas.create_line(50, 10, 50, 90, width=10, fill="blue")
canvas.create_line(10, 50, 90, 50, width=10, fill="blue")

# Erstelle einen Button-Widget, der das Canvas-Element überdeckt
button = tk.Button(root, command=plus_action)
button.place(x=0, y=0, width=100, height=100)

# Starte die Hauptschleife
root.mainloop()
