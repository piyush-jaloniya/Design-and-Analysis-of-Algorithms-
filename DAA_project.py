import tkinter as tk
from tkinter import ttk, messagebox

class Item:
    def __init__(self, name, weight, profit):
        self.name = name
        self.weight = weight
        self.profit = profit
        self.profit_per_weight = profit / weight

    def __str__(self):
        return f"{self.name}: Weight={self.weight}, Profit={self.profit}, Profit/Weight={self.profit_per_weight:.2f}"


class Inventory:
    def __init__(self):
        self.items = []

    def add_item(self, name, weight, profit):
        item = Item(name, weight, profit)
        self.items.append(item)
        return f"Added item: {item}"

    def update_item(self, name, weight, profit):
        for item in self.items:
            if item.name == name:
                item.weight = weight
                item.profit = profit
                item.profit_per_weight = profit / weight
                return f"Updated item: {item}"
        return "Item not found."

    def remove_item(self, name):
        for item in self.items:
            if item.name == name:
                self.items.remove(item)
                return f"Removed item: {name}"
        return "Item not found."

    def view_items(self):
        if not self.items:
            return "No items in inventory."
        return "\n".join(str(item) for item in self.items)

    def fractional_knapsack(self, capacity):
        self.items.sort(key=lambda item: item.profit_per_weight, reverse=True)
        total_profit = 0
        result_text = "Selected items for knapsack:\n"

        for item in self.items:
            if capacity <= 0:
                break
            if item.weight <= capacity:
                total_profit += item.profit
                capacity -= item.weight
                result_text += f"Added full item: {item.name}, Weight: {item.weight}, Profit: {item.profit}\n"
            else:
                fraction = capacity / item.weight
                total_profit += item.profit * fraction
                result_text += f"Added partial item: {item.name}, Weight: {capacity}, Profit: {item.profit * fraction}\n"
                capacity = 0

        result_text += f"\nTotal profit in knapsack: {total_profit:.2f}"
        return result_text


class InventoryApp:
    def __init__(self, root):
        self.inventory = Inventory()
        self.root = root
        self.root.title("Inventory Management System")

        # Labels and entry fields
        tk.Label(root, text="Item Name:").grid(row=0, column=0, padx=5, pady=5)
        self.name_entry = tk.Entry(root)
        self.name_entry.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(root, text="Weight (kg):").grid(row=1, column=0, padx=5, pady=5)
        self.weight_entry = tk.Entry(root)
        self.weight_entry.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(root, text="Profit:").grid(row=2, column=0, padx=5, pady=5)
        self.profit_entry = tk.Entry(root)
        self.profit_entry.grid(row=2, column=1, padx=5, pady=5)

        tk.Label(root, text="Knapsack Capacity (kg):").grid(row=3, column=0, padx=5, pady=5)
        self.capacity_entry = tk.Entry(root)
        self.capacity_entry.grid(row=3, column=1, padx=5, pady=5)

        # Buttons for functionalities
        ttk.Button(root, text="Add Item", command=self.add_item).grid(row=4, column=0, padx=5, pady=5)
        ttk.Button(root, text="Update Item", command=self.update_item).grid(row=4, column=1, padx=5, pady=5)
        ttk.Button(root, text="Remove Item", command=self.remove_item).grid(row=5, column=0, padx=5, pady=5)
        ttk.Button(root, text="View Items", command=self.view_items).grid(row=5, column=1, padx=5, pady=5)
        ttk.Button(root, text="Calculate Fractional Knapsack", command=self.calculate_knapsack).grid(row=6, column=0, columnspan=2, padx=5, pady=5)

        # Text area for displaying output
        self.output_text = tk.Text(root, width=40, height=15, wrap="word")
        self.output_text.grid(row=7, column=0, columnspan=2, padx=5, pady=5)

    def add_item(self):
        name = self.name_entry.get()
        weight = float(self.weight_entry.get())
        profit = float(self.profit_entry.get())
        result = self.inventory.add_item(name, weight, profit)
        messagebox.showinfo("Result", result)
    
        # Clear the entry fields after adding the item
        self.name_entry.delete(0, tk.END)
        self.weight_entry.delete(0, tk.END)
        self.profit_entry.delete(0, tk.END)


    def update_item(self):
        name = self.name_entry.get()
        weight = float(self.weight_entry.get())
        profit = float(self.profit_entry.get())
        result = self.inventory.update_item(name, weight, profit)
        messagebox.showinfo("Result", result)
        
        # Clear the entry fields after adding the item
        self.name_entry.delete(0, tk.END)
        self.weight_entry.delete(0, tk.END)
        self.profit_entry.delete(0, tk.END)
        
    def remove_item(self):
        name = self.name_entry.get()
        result = self.inventory.remove_item(name)
        messagebox.showinfo("Result", result)

    def view_items(self):
        items = self.inventory.view_items()
        self.output_text.delete(1.0, tk.END)
        self.output_text.insert(tk.END, items)

    def calculate_knapsack(self):
        capacity = float(self.capacity_entry.get())
        result = self.inventory.fractional_knapsack(capacity)
        self.output_text.delete(1.0, tk.END)
        self.output_text.insert(tk.END, result)



root = tk.Tk()
app = InventoryApp(root)
root.mainloop()
