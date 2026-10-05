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

import tkinter as tk

root = tk.Tk()

root.title("My House and Neighbor House")

canvas = tk.Canvas(root, width=800, height=400, bg="skyblue")

canvas.pack()


# =========================
# MY HOUSE
# =========================

# House body
canvas.create_rectangle(
    100, 180, 300, 330,
    fill="coral"
)

# Roof
canvas.create_polygon(
    80, 180,
    200, 100,
    320, 180,
    fill="brown"
)

# Door
canvas.create_rectangle(
    170, 250, 230, 330,
    fill="blue"
)

# Window
canvas.create_rectangle(
    120, 210, 160, 250,
    fill="lightblue"
)

# Sun
canvas.create_oval(
    650, 40, 710, 100,
    fill="yellow"
)

# Ground
canvas.create_line(
    40, 330, 760, 330,
    width=4
)

# My House name
canvas.create_text(
    200, 360,
    text="My House",
    font=("Arial", 18)
)


# =========================
# NEIGHBOR HOUSE
# =========================

# Neighbor house body
canvas.create_rectangle(
    450, 180, 650, 330,
    fill="lightyellow"
)

# Neighbor roof
canvas.create_polygon(
    430, 180,
    550, 100,
    670, 180,
    fill="darkgreen"
)

# Neighbor door
canvas.create_rectangle(
    520, 250, 580, 330,
    fill="saddlebrown"
)

# Door handle
canvas.create_oval(
    565, 285, 572, 292,
    fill="yellow"
)

# Left window
canvas.create_rectangle(
    465, 210, 510, 250,
    fill="lightblue"
)

# Left window cross
canvas.create_line(
    487, 210, 487, 250,
    width=2
)

canvas.create_line(
    465, 230, 510, 230,
    width=2
)

# Right window
canvas.create_rectangle(
    590, 210, 635, 250,
    fill="lightblue"
)

# Right window cross
canvas.create_line(
    612, 210, 612, 250,
    width=2
)

canvas.create_line(
    590, 230, 635, 230,
    width=2
)

# Tree beside neighbor
canvas.create_rectangle(
    700, 260, 720, 330,
    fill="saddlebrown"
)

canvas.create_oval(
    670, 180, 750, 270,
    fill="green"
)

canvas.create_oval(
    685, 150, 755, 230,
    fill="forestgreen"
)

# Neighbor House name
canvas.create_text(
    550, 360,
    text="Neighbor House",
    font=("Arial", 18)
)


# =========================
# CONNECTING PATH
# =========================

canvas.create_line(
    300, 330, 450, 330,
    width=5
)

canvas.create_text(
    375, 315,
    text="Path",
    font=("Arial", 10)
)


# =========================
# CLICK EVENT
# =========================

def change_colour(event):
    canvas.create_rectangle(
        100, 180, 300, 330,
        fill="lightgreen"
    )


canvas.bind("<Button-1>", change_colour)


root.mainloop()

