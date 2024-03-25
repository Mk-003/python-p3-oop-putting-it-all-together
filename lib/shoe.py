#!/usr/bin/env python3

class Shoe:
    class Shoe:
    def __init__(self, size, style, color, brand, price):
        self.size = size
        self.style = style
        self.color = color
        self.brand = brand
        self.price = price

    def calculate_cost(self, tax_percentage):
        total_cost = self.price * (1 + tax_percentage)
        return total_cost

    def add_to_cart(self, cart):
        cart.append(self)