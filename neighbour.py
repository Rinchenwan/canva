import tkinter as tk

root = tk.Tk()

root.title("Neighbor House")

canvas = tk.Canvas(
    root,
    width=500,
    height=350,
    bg="skyblue"
)

canvas.pack()

# Neighbor house body
canvas.create_rectangle(
    150, 150, 350, 300,
    fill="lightyellow"
)

# Roof
canvas.create_polygon(
    130, 150,
    250, 70,
    370, 150,
    fill="darkgreen"
)

# Door
canvas.create_rectangle(
    220, 220, 280, 300,
    fill="saddlebrown"
)

# Door handle
canvas.create_oval(
    265, 255, 272, 262,
    fill="yellow"
)

# Left window
canvas.create_rectangle(
    165, 180, 210, 220,
    fill="lightblue"
)

# Left window lines
canvas.create_line(
    187, 180, 187, 220,
    width=2
)

canvas.create_line(
    165, 200, 210, 200,
    width=2
)

# Right window
canvas.create_rectangle(
    290, 180, 335, 220,
    fill="lightblue"
)

# Right window lines
canvas.create_line(
    312, 180, 312, 220,
    width=2
)

canvas.create_line(
    290, 200, 335, 200,
    width=2
)

# Tree trunk
canvas.create_rectangle(
    390, 230, 410, 300,
    fill="saddlebrown"
)

# Tree leaves
canvas.create_oval(
    360, 150, 440, 240,
    fill="green"
)

canvas.create_oval(
    375, 125, 450, 210,
    fill="forestgreen"
)

# Sun
canvas.create_oval(
    40, 40, 90, 90,
    fill="yellow"
)

# Ground
canvas.create_line(
    50, 300, 450, 300,
    width=4
)

# Name
canvas.create_text(
    250, 325,
    text="Neighbor House",
    font=("Arial", 20)
)

root.mainloop()
