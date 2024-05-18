# print('abner')
# name = input("what is your name")
# print(f"hello  {name}")
# s = set()
# s.add(1)
# s.add(2)
# s.add(3)
# s.add(4)
# s.add(5)
# s.add(6)
# s.add(7)
# s.add(8)
# print(s)
# for i in range (10):
#     print(f"the square of{i}is ")

# class Point():
#     def __init__(self,input1,input2):
#         self.x = input1
#         self.y = input2


# p = Point(7,90)

# print(p.x)
# print(p.y)
# class Flight ():
#     def __init__(self,capacity):
#         self.capacity = capacity
#         self.passengers = []
#     def add_pasenger (self,name):
#         if not self.open_seats():
#             return False
#         self.passengers.append(name)
#         return True
#     def open_seats(self):
#         return self.capacity - len(self.passengers)

# flight = Flight(5)
# people =["harry","ron","hermaone","john","abner" ,"grace","joy"]
# for person in people:
#     if flight.add_pasenger(person):
#         print(f"added {person} to flight successfully")
#     else:
#         print(f"No available seat for {person}")




import sys
x =int(input("X:"))
y =int(input("Y:"))
n = x/y
try:
    x =int(input("X:"))
    y =int(input("Y:"))
except ValueError:
    print("Error: ValueError")
    sys.exit(1)

try:
      print(f"{x} / {y} = {n}")
except ZeroDivisionError:
     print("Error:cannot divid by 0")
     sys.exit(1)





import d











