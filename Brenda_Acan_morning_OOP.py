#class in OOP





class Rectangle:
    def __init__(self,length,width) -> None:
        self.length=length
        self.width=width

    def calculate_area(self):
        return self.length*self.width   
    
    def calculate_perimeter(self):
        return 2*(self.length+self.width)
    
    
my_rectangle=Rectangle(12,2)
print(my_rectangle.calculate_area())
print(my_rectangle.calculate_perimeter())


#calculate the area of a  circle
class Circle:
    def __init__(self,radius): 
      self.radius=radius

    def calculate_area(self):
          return 2*3.14*self.radius
      
circle=Circle(4)
print (circle.calculate_area())


class Mine:
        def __init__(self,name) -> None:
            self.name=name
my_object=Mine("John")
print(my_object.name)


#2
class Mine :
      def __init__(self,name) -> None:
            self.name=name
      def _greet(self):
            print("Hello,"+self.name)
my_object=Mine("John")
print(my_object._greet())   

3#
class Name:
      def __init__(self,name )-> None:
            self.name=name
      def sick(self):
            print(self.name  +"is sick. ") 


person1=Name("Tracy")  
person2=Name("Edith")  
print(person1.sick()) 
print(person2.sick())  

#####Calculate and display the employee bonus (15%) of salary(employee1:150000, employee2:230000)
class Employee:
      def __init__(self,name, salary):
            self.name= name
            self.salary=salary
            
      
            
      def calculate(self):
            return self.salary+ (self.salary*(15/100) )  

myemployee1=Employee("James",150000)
myemployee2=Employee("Sharon",230000)      

print (myemployee1.calculate())
print (myemployee2.calculate())



class BankAccount:
      def __init__(self,number,balance) -> None:
            self.number=number
            self.balance=balance
      def deposit(self,amount):
          self.balance+=amount       
      def withdraw(self,amount):
            if self.balance>=amount:
                  self.balance=amount
            else:
              print("insufficient amount")
              
      def get_balance(self):
            return self.balance        
                             

my_account=BankAccount(123345678,1000)
print(my_account.balance)
print(my_account.number)


#Exercise one 
class Convert:
      def __init__(self,celcius):
            self.celcius=celcius
      def convert(self):
            return(self.celcius* 9/5) +32
           
convert=Convert(37)
print(convert.convert())   
#2 Show encapsulaation with employee information to give a pay salary incremenatation (Salary with employee information to new salary e.g)from 850000 to 1000000
class Employee:
      def __init__(self, name, salary,):
            self.name=name
            self.salary=salary
         
      def increment(self,increase):
       self.increase=increase
      
       if increase>0:
             print("Increment has been applied")
       else:
             print("The increase should be grater than zero.")

      
      def display(self):
            
            return self.salary+ self.increase
        

my_employee=Employee("Agatha", 850000)
print(my_employee.increment(150000))
print(my_employee.display())


    