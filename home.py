import tkinter as tk

root = tk.Tk()

root.title("My House")

canvas = tk.Canvas(root, width=500, height=350, bg="skyblue")

canvas.pack()

# House body
canvas.create_rectangle(150, 150, 350, 300, fill="coral")
canvas.create_polygon(130, 150, 250, 70, 370, 150, fill="brown")
canvas.create_rectangle(220, 220, 280, 300, fill="blue")
canvas.create_rectangle(170, 180, 210, 220, fill="lightblue")
canvas.create_oval(380, 40, 440, 100, fill="yellow")
canvas.create_line(50, 300, 450, 300, width=4)
canvas.create_text(250, 325, text="My House", font=("Arial", 20))

def change_colour(event):
    canvas.create_rectangle(150, 150, 350, 300, fill="lightgreen")

canvas.bind("<Button-1>", change_colour)

root.mainloop()