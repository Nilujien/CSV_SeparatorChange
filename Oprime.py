import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Create initial data for the pie chart
labels = ['A', 'B', 'C']
values = [30, 40, 50]

# Create tkinter window
root = tk.Tk()

# Create matplotlib figure and pie chart
fig = plt.Figure(figsize=(5, 4), dpi=100)
ax = fig.add_subplot(111)
pie = ax.pie(values, labels=labels)

# Create matplotlib canvas and add it to the tkinter window
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.draw()
canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

# Define update function
def update_pie(new_values):
    # Update data in the pie chart
    for i, val in enumerate(new_values):
        pie[0][i].set_data([0, val])
    ax.relim()
    ax.autoscale_view()
    canvas.draw()

# Create tkinter button to trigger the update function
button = tk.Button(root, text='Update Pie', command=lambda: update_pie([40, 30, 60]))
button.pack(side=tk.BOTTOM)

# Start tkinter main loop
root.mainloop()
