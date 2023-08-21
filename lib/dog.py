#!/usr/bin/env python3

APPROVED_BREEDS = [
    "Mastiff",
    "Chihuahua",
    "Corgi",
    "Shar Pei",
    "Beagle",
    "French Bulldog",
    "Pug",
    "Pointer"
]

# class Dog:
#     def __init__(self, name):
#         self._name = None  # Initialize the _name attribute
    
#     def name(self):
#         return self._name  # Getter for the name property

#     def name(self, value):
#         if type(value) is str and len(value) <= 25:
#             self._name = value.title()  
#         else:
#           print("Name must be a string under 25 characters.")


class Dog:
    def __init__(self, name=None, breed=None):
        self._name = None
        self._breed = None
        if name is not None:
            self.name = name
        if breed is not None:
            self.breed = breed

    def name(self):
        return self._name

    def name(self, value):
        if isinstance(value, str) and   len(value) <= 25:
            self._name = value.title()
        else:
            print("Name must be string between 1 and 25 characters.")

    def breed(self):
        return self._breed

    def breed(self, value):
        if value in APPROVED_BREEDS:
            self._breed = value
        else:
            print("Breed must be in list of approved breeds.")
