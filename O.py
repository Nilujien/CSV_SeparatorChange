import tkinter as tk

root = tk.Tk()

# Create a Canvas widget with a scrollbar
canvas = tk.Canvas(root)
scrollbar = tk.Scrollbar(root, orient=tk.VERTICAL, command=canvas.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)
canvas.config(yscrollcommand=scrollbar.set)

# Create a frame inside the canvas for the scrollable content
frame = tk.Frame(canvas)
canvas.create_window((0, 0), window=frame, anchor='nw')

# Add some widgets to the scrollable frame
for i in range(50):
    tk.Label(frame, text=f"Label {i}").pack()


# Configure the Canvas to resize with the window
def resize_canvas(event):
    canvas.configure(scrollregion=canvas.bbox('all'))


canvas.bind('<Configure>', resize_canvas)

root.mainloop()
