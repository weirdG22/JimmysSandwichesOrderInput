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

order = []

class OrderingWindow(EasyFrame):
    """Application window for the ordering screen."""
 
    def __init__(self):
        """Sets up the window and the widgets."""
        EasyFrame.__init__(self, title = "Jimmy's Sandwiches | Order Entry Window")
        self.setResizable(False)

        # Button to print final receipt
        self.addButton(text = "Print Receipt", row = 6, column = 0, columnspan = 2, command = self.printReceipt)

        # Sandwiches Section
        self.addLabel(text = "Sandwiches", row = 1, column = 0)

        # Ham and Cheese Image and Button
        self.loadImage("images/hamAndCheese.gif", 200, 200, 2, 0)
        self.addButton(text = "Ham and Cheese", row = 3, column = 0, command = lambda: self.addItem("Ham and Cheese", 8))

        # Roast Beef Image and Button
        self.loadImage("images/roastBeef.gif", 200, 200, 2, 1)
        self.addButton(text = "Roast Beef", row = 3, column = 1, command = lambda: self.addItem("Roast Beef", 7))

        # Italian Image and Button
        self.loadImage("images/italian.gif", 200, 200, 4, 0)
        self.addButton(text = "Italian", row = 5, column = 0, command = lambda: self.addItem("Italian", 9))

        # Tuna Image and Button
        self.loadImage("images/tuna.gif", 200, 200, 4, 1)
        self.addButton(text = "Tuna", row = 5, column = 1, command = lambda: self.addItem("Tuna", 7))

    def printReceipt(self):
        """Takes order list and prints with a formatted receipt including subtotal, sales tax, and total."""
        output = ""
        for lineItem in order:
            output += "$" + str(lineItem["price"]) + ": " + lineItem["item"] + "\n"
        self.messageBox(title = "Order Receipt", message = output)

    def loadImage(self, photoPath, width, height, row, col):
        """Loads a photo into the application with a path, width, height, row, and column."""
        load = Image.open(photoPath)
        load = load.resize((width, height))
        render = ImageTk.PhotoImage(load)
        img = Label(self, image=render, width=width, height=height)
        img.image = render
        img.grid(row=row, column=col)


    def addItem(self, item, price):
        order.append({"item": item, "price": price})
 
#Instantiate and pop up the window.
OrderingWindow().mainloop()
