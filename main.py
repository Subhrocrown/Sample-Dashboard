import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
from data import sales_data, inventory_data, product_data, sales_year_data, inventory_month_data

# Set color cycle for plots
plt.rcParams["axes.prop_cycle"] = plt.cycler(color=["blue", "yellow", "pink", "gray", "red"])

# Chart 1: Bar chart of sales data
fig1, ax1 = plt.subplots()
ax1.bar(sales_data.keys(), sales_data.values())
ax1.set_title("Sales by Product")
ax1.set_xlabel("Product")
ax1.set_ylabel("Sales")

# Chart 2: Horizontal bar chart of inventory data
fig2, ax2 = plt.subplots()
ax2.barh(list(inventory_data.keys()), inventory_data.values())
ax2.set_title("Inventory by Product")
ax2.set_xlabel("Inventory")
ax2.set_ylabel("Product")

# Chart 3: Pie chart of product data
fig3, ax3 = plt.subplots()
ax3.pie(product_data.values(), labels=product_data.keys(), autopct='%1.1f%%')
ax3.set_title("Product \nBreakdown")

# Chart 4: Line chart of sales by year
fig4, ax4 = plt.subplots()
ax4.plot(list(sales_year_data.keys()), list(sales_year_data.values()))
ax4.set_title("Sales by Year")
ax4.set_xlabel("Year")
ax4.set_ylabel("Sales")

# Chart 5: Area chart of inventory by month
fig5, ax5 = plt.subplots()
ax5.fill_between(inventory_month_data.keys(), inventory_month_data.values())
ax5.set_title("Inventory by Month")
ax5.set_xlabel("Months")
ax5.set_ylabel("Inventory")

# Create a window and add charts
root = tk.Tk()
root.title("Dashboard")
root.state('zoomed')

# Side frame for the dashboard label
side_frame = tk.Frame(root, bg="#4C2A85")
side_frame.pack(side="left", fill="y")

# Dashboard label
label = tk.Label(side_frame, text="Dashboard", bg="#4C2A85", fg="#FFF", font=25)
label.pack(pady=20, padx=20)  # Use pady for vertical spacing

# Frame for charts
charts_frame = tk.Frame(root)
charts_frame.pack(fill="both", expand=True)

# Upper frame for the first three charts
upper_frame = tk.Frame(charts_frame)
upper_frame.pack(fill="both", expand=True)

# Canvas for the first chart
canvas1 = FigureCanvasTkAgg(fig1, upper_frame)
canvas1.draw()
canvas1.get_tk_widget().pack(side="left", fill="both", expand=True)

# Canvas for the second chart
canvas2 = FigureCanvasTkAgg(fig2, upper_frame)
canvas2.draw()
canvas2.get_tk_widget().pack(side="left", fill="both", expand=True)

# Canvas for the third chart
canvas3 = FigureCanvasTkAgg(fig3, upper_frame)
canvas3.draw()
canvas3.get_tk_widget().pack(side="left", fill="both", expand=True)

# Lower frame for the last two charts
lower_frame = tk.Frame(charts_frame)
lower_frame.pack(fill="both", expand=True)

# Canvas for the fourth chart
canvas4 = FigureCanvasTkAgg(fig4, lower_frame)
canvas4.draw()
canvas4.get_tk_widget().pack(side="left", fill="both", expand=True)

# Canvas for the fifth chart
canvas5 = FigureCanvasTkAgg(fig5, lower_frame)
canvas5.draw()
canvas5.get_tk_widget().pack(side="left", fill="both", expand=True)

# Start the Tkinter main loop
root.mainloop()