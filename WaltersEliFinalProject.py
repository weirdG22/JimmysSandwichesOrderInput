"""
Author:  Eli Walters
Date Started: 09/29/23
Assignment:   SDEV140 Final Project
Short Desc:   This program will open a GUI and allow workers of a sandwich shop to input orders and print out a clean, readable receipt.
"""

from breezypythongui import EasyFrame
from tkinter import *
from PIL import Image
from PIL import ImageTk

class OrderingWindow(EasyFrame):
    """Application window for the ordering screen."""
 
    def __init__(self):
        """Sets up the window and the widgets."""
        EasyFrame.__init__(self, title = "Jimmy's Sandwiches | Order Entry Window")
        self.setResizable(False)

        # Stored line items on the receipt
        self.order = []

        # Total of items added to order variable
        self.subtotal = 0

        # Top Menu Buttons
        self.addButton(text = "Print Receipt", row = 1, column = 1, columnspan = 2, command = self.printReceipt)
        self.addButton(text = "Exit", row = 1, column = 3, command = self.destroy)

        # Sandwiches Section
        self.addLabel(text = "Sandwiches", row = 1, column = 0)

        # Ham and Cheese Image and Button
        self.loadImage("images/hamAndCheese.gif", 200, 200, 2, 0)
        self.addButton(text = "Add: $8 Ham and Cheese", row = 3, column = 0, command = lambda: self.addItem("Ham and Cheese", 8))
        self.addButton(text = "Item Description", row = 3, column = 1, command = lambda: self.itemDesc("Ham, Cheese, Lettuce, Tomato, Mayo"))

        # Roast Beef Image and Button
        self.loadImage("images/roastBeef.gif", 200, 200, 2, 2)
        self.addButton(text = "Add: $7 Roast Beef", row = 3, column = 2, command = lambda: self.addItem("Roast Beef", 7))
        self.addButton(text = "Item Description", row = 3, column = 3, command = lambda: self.itemDesc("Roast Beef, Lettuce, Tomato, Mayo"))

        # Italian Image and Button
        self.loadImage("images/italian.gif", 200, 200, 4, 0)
        self.addButton(text = "Add: $9 Italian", row = 5, column = 0, command = lambda: self.addItem("Italian", 9))
        self.addButton(text = "Item Description", row = 5, column = 1, command = lambda: self.itemDesc("Ham, Salami, Cheese, Onion, Lettuce, Tomato, Mayo"))

        # Tuna Image and Button
        self.loadImage("images/tuna.gif", 200, 200, 4, 2)
        self.addButton(text = "Add: $7 Tuna", row = 5, column = 2, command = lambda: self.addItem("Tuna", 7))
        self.addButton(text = "Item Description", row = 5, column = 3, command = lambda: self.itemDesc("Tuna, Lettuce, Tomato, Cucumber"))

        # Sandwiches Section
        self.addLabel(text = "Side Items - All $2", row = 6, column = 0)

        # Sides Buttons
        self.addButton(text = "Add: Regular Chips", row = 7, column = 0, command = lambda: self.addItem("Regular Chips", 2))
        self.addButton(text = "Add: BBQ Chips", row = 7, column = 1, command = lambda: self.addItem("BBQ Chips", 2))
        self.addButton(text = "Add: Jalapeno Chips", row = 7, column = 2, command = lambda: self.addItem("Jalapeno Chips", 2))
        self.addButton(text = "Add: Salt & Vinegar Chips", row = 7, column = 3, command = lambda: self.addItem("Salt & Vinegar Chips", 2))

        # Sandwiches Section
        self.addLabel(text = "Drinks - All $3", row = 8, column = 0)

        # Sides Buttons
        self.addButton(text = "Add: Coke", row = 9, column = 0, command = lambda: self.addItem("Coke", 3))
        self.addButton(text = "Add: Diet Coke", row = 9, column = 1, command = lambda: self.addItem("Diet Coke", 3))
        self.addButton(text = "Add: Sprite", row = 9, column = 2, command = lambda: self.addItem("Sprite", 3))
        self.addButton(text = "Add: Ice Tea", row = 9, column = 3, command = lambda: self.addItem("Ice Tea", 3))
        

    def printReceipt(self):
        """Takes order list and prints with a formatted receipt including subtotal, sales tax, and total."""

        # Add all items to receipt text
        output = ""
        for lineItem in self.order:
            output += "$" + str(lineItem["price"]) + ": " + lineItem["item"] + "\n"

        # Calculate Sales Tax
        salesTax = self.subtotal * 0.07

        # Add Subtotal, Sales Tax, and Grand Total to Receipt Text
        output += "\n"
        output += "Subtotal: $" + str("%0.2f" % self.subtotal)
        output += "\nSales Tax: $" + str("%0.2f" % salesTax)
        output += "\nGrand Total: $" + str("%0.2f" % (self.subtotal + salesTax))

        # Create Receipt Window
        receipt = Toplevel(self)
        receipt.title("Order Receipt")

        # Add Receipt Text
        receiptLabel = Label(receipt, text = output)
        receiptLabel.pack(pady=10, padx=20)

        # Add Receipt Button
        closeReceipt = Button(receipt, text = "Close", command = receipt.destroy)
        closeReceipt.pack()

    def loadImage(self, photoPath, width, height, row, col):
        """Loads a photo into the application with a path, width, height, row, and column."""
        load = Image.open(photoPath)
        load = load.resize((width, height))
        render = ImageTk.PhotoImage(load)
        img = Label(self, image=render, width=width, height=height)
        img.image = render
        img.grid(row=row, column=col, columnspan=2)


    def addItem(self, item, price):
        """Adds an item to the receipt and adds the defined price to the subtotal."""
        self.subtotal += price
        self.order.append({"item": item, "price": price})

    def itemDesc(self, desc):
        """Pops up message box with an item description."""
        self.messageBox(title = "Item Description", message = desc)
 
#Instantiate and pop up the window.
OrderingWindow().mainloop()
