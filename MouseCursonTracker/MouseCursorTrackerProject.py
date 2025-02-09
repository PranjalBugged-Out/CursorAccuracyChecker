import tkinter as tk
import math

root = tk.Tk()
root.title("Mouse Cursor Tracking & Accuracy Analysis")
root.geometry("800x600")
root.configure(bg="black")

canvas = tk.Canvas(root, bg="black", width=800, height=600)
canvas.pack(fill=tk.BOTH, expand=True)

coord_label = tk.Label(root, text="X: 0, Y: 0", font=("Courier", 14), fg="lime", bg="black")
coord_label.place(x=10, y=10)

accuracy_label = tk.Label(root, text="Accuracy: 100%", font=("Courier", 14), fg="cyan", bg="black")
accuracy_label.place(x=10, y=40)

N = 20
trail = []
deviation_sum = 0
movements = 0

def calculate_accuracy():
    global deviation_sum, movements
    if movements == 0:
        return 100  # Default full accuracy
    avg_deviation = deviation_sum / movements
    accuracy = max(0, 100 - avg_deviation * 2)  # Scale deviation to percentage
    return round(accuracy, 2)

def track_mouse(event):
    global trail, deviation_sum, movements

    x, y = event.x, event.y
    coord_label.config(text=f"X: {x}, Y: {y}")

    if trail:
        prev_x, prev_y = trail[0]
        deviation = math.sqrt((x - prev_x) ** 2 + (y - prev_y) ** 2)
        deviation_sum += deviation
        movements += 1
        accuracy_label.config(text=f"Accuracy: {calculate_accuracy()}%")

    trail.insert(0, (x, y))
    if len(trail) > N:
        trail.pop()

    canvas.delete("all")

    for i, (tx, ty) in enumerate(trail):
        size = max(2, 8 - i // 2)
        color = f"#00ff{255 - int(200 * (i / N)):02x}"
        canvas.create_oval(tx - size, ty - size, tx + size, ty + size, fill=color, outline="")

root.bind("<Motion>", track_mouse)
root.mainloop()
