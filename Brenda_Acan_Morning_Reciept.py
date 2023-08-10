#inheritance
class Vehicle:
    def __init__(self, brand):
        self.brand = brand

    def start_engine(self):
        print("Engine started.")

    def stop_engine(self):
        print("Engine stopped.")

class Car(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand)
        self.model = model

    def drive(self):
        print(f"Driving the {self.brand} {self.model}.")

class Bicycle(Vehicle):
    def pedal(self):
        print("Pedaling the bicycle.")

car = Car("Toyota", "Camry")
car.start_engine()  
car.drive()        
car.stop_engine()  

bicycle = Bicycle("Giant")
bicycle.start_engine()  
bicycle.pedal()        
bicycle.stop_engine()  
#multiple inheritance
class Animal:
    def __init__(self, name):
        self.name = name

    def sleep(self):
        print(f"{self.name} is sleeping.")

class Flyable:
    def fly(self):
        print("Flying.")

class Bird(Animal, Flyable):
    def __init__(self, name):
        super().__init__(name)

    def chirp(self):
        print("Chirping.")

bird = Bird("Sparrow")
bird.sleep()  
bird.chirp()  
bird.fly() 
#Polymorphism
  #method overiding
class Shape:
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

rectangle = Rectangle(5, 3)
print(rectangle.area()) 

circle = Circle(4)
print(circle.area()) 
  #method overloading
def add(a, b):
    return a + b

print(add(5, 3))          
print(add("Hello", "World"))  
#Abstraction
from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass

    @abstractmethod
    def move(self):
        pass

class Dog(Animal):
    def sound(self):
        return "Woof!"

    def move(self):
        return "Running"

class Cat(Animal):
    def sound(self):
        return "Meow!"

    def move(self):
        return "Jumping"

# Uncommenting the following line will result in an error,
# as abstract methods are not implemented in the derived class.
# animal = Animal()

dog = Dog()
print(dog.sound())  

print(dog.move())   

cat = Cat()
print(cat.sound())  
print(cat.move())   

from tkinter import*

root=Tk()
root.title("billing")
root.geometry("300x100")

# ---------top section-----
title=Label(root,text='Reciept')
title.pack(fill=X)
#------customer detail-----
F1=LabelFrame(root,text='Customer Detatil')
F1.place(x=0,y=80,relwidth=1)

cname_lbl=Label(F1,text='Customer Name')
cname_lbl.grid(row=0,column=0 ,padx=10,pady=5)
cname_txt=Entry(F1, width =15,relief=SUNKEN)
cname_txt.grid(row=0,column=1,padx=10,pady=5)



cphone_lbl=Label(F1,text='Customer PhoneNo')
cphone_lbl.grid(row=0,column=2 ,padx=10,pady=5)
cphone_txt=Entry(F1, width =15,relief=SUNKEN)
cphone_txt.grid(row=0,column=3,padx=10,pady=5)

#--------Product detail-----
F2=LabelFrame(root,text=' Product Detatil')
F2.place(x=20,y=180,width=630,height=500)

item=Label(F2,text='Product Name')
item.grid(row=0,column=0,padx=30,pady=20)
item_txt=Entry(F2, width =20,relief=SUNKEN)
item_txt.grid(row=0,column=1,padx=30,pady=20)



item=Label(F2,text='Price')
item.grid(row=1,column=0,padx=30,pady=20)
item_txt=Entry(F2, width =20,relief=SUNKEN)
item_txt.grid(row=1,column=1,padx=30,pady=20)

item=Label(F2,text='Quantity')
item.grid(row=2,column=0,padx=30,pady=20)
item_txt=Entry(F2, width =20,relief=SUNKEN)
item_txt.grid(row=2,column=1,padx=30,pady=20)
    
item=Label(F2,text='total')
item.grid(row=3,column=0,padx=30,pady=20)
item_txt=Entry(F2, width =20,relief=SUNKEN)
item_txt.grid(row=3,column=1,padx=30,pady=20)


btn=Button(F2,text='Add item')
btn.grid(row=4,column=0,padx=10,pady=30)


btn=Button(F2,text='Bill')
btn.grid(row=4,column=1,padx=10,pady=30)

btn=Button(F2,text='clear')
btn.grid(row=5,column=0,padx=10,pady=30)

btn=Button(F2,text='Exit')
btn.grid(row=5,column=1,padx=10,pady=30)


root.mainloop()