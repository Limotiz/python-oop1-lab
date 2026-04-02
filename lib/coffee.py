#!/usr/bin/env python3

class Coffee:
    def __init__(self, size, price):
        self.size = size
        self.price = price
        
    def set_size(self, value):
        if value in ["Small, Medium, or Large"]:
            self.size = value
        else:
            print("size must be Small, Medium, or Large")
            self.size = "Small"    

    def tip(self):   
        print("The kind of coffee which makes me come back! ")
        self.price += 10 

        