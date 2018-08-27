"""
In this quiz, you'll write your own hash table and hash function that uses string keys. Your table will store strings in buckets by their first two letters, according to the formula below:

Hash Value = (ASCII Value of First Letter * 100) + ASCII Value of Second Letter


You can assume that the string will have at least two letters, and the first two characters are uppercase letters (ASCII values from 65 to 90). You can use the Python function ord() to get the ASCII value of a letter, and chr() to get the letter associated with an ASCII value.

You'll create a HashTable class, methods to store and lookup values, and a helper function to calculate a hash value given a string. You cannot use a Python dictionary—only lists! And remember to store lists at each bucket, and not just the string itself. For example, you can store "UDACITY" at index 8568 as ["UDACITY"].



Write a HashTable class that stores strings
in a hash table, where keys are calculated
using the first two letters of the string."""

class HashTable:
    def __init__(self):
        self.table = [None]*10000
    def store(self,string):
        hv = self.calculate_hash_value(string)
        if hv != -1:
            if self.table[hv] != None:
                self.table[hv].append(string)
            else:
                self.table[hv] = string

    def look_up(self,string):
        hv = self.calculate_hash_value(string)
        if hv != -1:
            if self.table[hv] != None:
                if string in self.table[hv]:
                    return hv
        return -1
    def calculate_hash_value(self,string):
        hv = ord(string[0])*100 + ord(string[1])
        return hv

my_hash_table = HashTable()
print(my_hash_table.calculate_hash_value("UDACITY"))
print(my_hash_table.look_up("UDACITY"))
my_hash_table.store("UDACITY")
print(my_hash_table.look_up("UDACITY"))
my_hash_table.store("UDACIOUS")
print(my_hash_table.look_up("UDACIOUS"))
