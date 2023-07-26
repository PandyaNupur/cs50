#My first program
# print("Hello world");

#string input
# name=input("Name:")
# print("Hello "+name)
# print(f"Hello, {name}")   fstring like template literal in js


#conditions
# n=int(input("number:"))

# if n > 0:
#     print("n is positive")
# elif n<0:
#     print("n is negative")

# else:
#     print("n is 0")


# name="harry"
# print(name[0]) returns h

# name=["Harry","Ron","Hermione"] python list
# print(name[0]) returns harry

# coordinateX=10.0
# coordinateY=20.0
# coordinate=(10.0,20.0) python tuple
# print(coordinate)

#Define a lsit of names
# names=["Harry","Ron","Hermione"] 
# #list is mutable
# names.append("Draco") #adds this at the end of the list
# names.sort() #sorts the list
# print(names)

#SET
#Creating an empty set
# s=set() #Unique collection
# #Add elemnts to the set
# s.add(1)
# s.add(2)
# s.add(3)
# s.add(3)
# s.remove(2) #removes that element

# print(s)
# print(f"The set has {len(s)} number of elements") #calculates the length


# for i in [0,1,2,3,4,5]:
#     print(i)

# for i in range(7):
#     print(i)

# names=["harry","hermione","ron"]
# for i in names:
#     print(i)

# name="nupur"
# for character in name:
#     print(character)

# #Dictionaries
# houses={"Harry":"Gryffindor","Draco":"Slytherin"}
# houses["Hermione"]="Gryffindor" #to add 
# print(houses)
# print(houses["Harry"])


#Functions
# def square(x):
#     return x*x
# for i in range(10):
#     print(f"The square of {i} is {square(i)}")

# class Flight():
#     def __init__(self,capacity):
#         self.capacity=capacity
#         self.passengers=[]
#     def add_passenger(self,name):
#         if not self.open_seats():
#             return False
#         self.passengers.append(name)
#         return True
#     def open_seats(self):
#         return self.capacity - len(self.passengers)
# flights=Flight(3)
# people=["harry","ron","draco","ginny"]
# for person in people:
#     success=flights.add_passenger(person)
#     if success:
#         print(f"Added {person} to flight")
#     else:
#         print(f"No available seats for {person}")


# def announce(f):
#     def wrapper():
#         print("About to run the function...")
#         f()
#         print("Done with the function")
#     return wrapper
# @announce
# def hello():
#     print("Hello World")
# hello()

# people=[
#     {"name":"Harry","house":"Gryffindor"},
#     {"name":"Cho","house":"Ravenclow"},
#     {"name":"Draco","house":"Malfoy"},
# ]
# # def f(person):
# #     return person["name"]
# people.sort(key=lambda person:person["name"])
# print(people)
import sys
try:
    x=int(input("x:"))
    y=int(input("y:"))
except ValueError:
    print("invalid input")
    sys.exit(1)
try:
    result=x/y
except ZeroDivisionError:
    print("Error:Cannot divide by 0")
    sys.exit(1)
print(result)