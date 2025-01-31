#task 1

class StringProcessor:
    def __init__(self):
        self.text = ""
    
    def getString(self):
      self.text = input()

    def printString(self):
      print(self.text.upper())

if __name__ == "__main__":
    processor = StringProcessor()
    processor.getString()
    processor.printString()

#task 2
class Shape:
    def shapearea(self):
        return 0
    
class Square(Shape):
    def __init__ (self , lenght):
            self.lenght = lenght
    def area(self):
        return self.lenght ** 2
sq = Square(4)
print(sq.area())

# #task 3
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def area(self):
        return self.length * self.width
rec = Rectangle(5 , 4)
print(rec.area())

# #task 4
import math
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def show(self):
        print(self.x, self.y)
    
    def move(self, newx, newy):
        self.x = newx
        self.y = newy
    
    def dist(self , other_point: "Point") -> float:
        return math.sqrt((self.x - other_point.x) ** 2 + (self.y - other_point.y) ** 2)

pt1 = Point(2 , 3)
pt2= Point(1 , 1)
distance = pt1.dist(pt2)
print(distance)

#task 5
class Account:
    def __init__(self , owner , balance = 0):
        self.owner = owner
        self.balance = balance
    def deposit(self , amount):
        self.balance += amount
        print(f"Deposited {amount} , and balanced {self.balance}" )
    def withdraw(self , amount):
        if amount > self.balance:
            print("No way!")
        else:
            self.balance -= amount
            print(f"Withdraw {amount} , new balance {self.balance}")
    def __str__(self):
        return f"Account owner: {self.owner}, Balance: {self.balance}"
    
bankacc = Account("Dariya" , 50000000)
print(bankacc)

#task 6
from math import sqrt

def is_prime(n):
    if n < 2:
        return False
    for i in range(2 , int(sqrt(n) + 1)):
        if n % i == 0:
            return False
    return True
num = [2 , 3 , 4 , 5 , 6 , 7 , 8 , 9]
prime = list(filter(lambda x: is_prime(x) , num))
print(prime)