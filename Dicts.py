#Exercise1
students={
    "Alice":85,
    "Sarah":23,
    "Vicent":90,
    "Eve":23
  }
age=list(students.values())
print("list of age:",age )
#Exercise2
#check if the key exists in the dictionary
Students={
    "Alice":85,
    "Sarah" :23,
    "Vicent":90,
    "Eve"  :40
}
key="Sarah"
if key in Students:
 print("The key[key] exists")

else:
    print("The key[key] doesnt exist")
#Exercise 3
#Ho to update
Students={
    "Alice":90,
    "Sarah":23,
    "Joan":18,
    "Alisha":5,
}
additional={
    "Beatrice":5,
    "Mercy":12,
    "Fred":13,
}
Students.update(additional)
print(Students)
#Exercise4
#How to add dictionary items and how to remove dictionary items
#Adding items
mydict={}
  #method1 :by using assignment operator
mydict["key1"]="value1"
mydict["key2"]="value2"
#method 2 : by using update() method
mydict.update({"key3":"value3","key4":"value4"})
print(mydict)
#Removing items
mydict={
    "key1":"value1",
    "key2":"value2",
    "key3":"value3",

}
del mydict["key1"]
mydict. pop("key2")
print(mydict)
#Exercise5
#How to loop through a dictionary
Students={
    "Sarah":60,
    "Christine":42,
    "steven":56,
}
for key,value in Students.items():
    print( key,':',value)

#Nesting a dictionary
employees={
  "John" :{
        "age":32,
        "position":"Manager"
    },
    "Alice":{
             "age":28,
             "position":"Engineer",

    },

}
for employee,details in employees.items():
    print("Employee:",employee)
    print("Age",details["age"])
    print("position:",details["position"])
    print()

#Exercise
    #Numbers
    #1.Determine the length of a string using the len() function
    x="dress"
    y=len(x)
    print(y)
    #2.Iterate through each character in a string using a for loop
    my_string="Hello World"
    for char in my_string:
        print(char)
     #3. slice  a string to extract specific portions of it
    my_char ="Hello, World!"
    subchar=my_char[7:12]
    print(subchar)   
    subchar=my_char[:5]
    print(subchar)
    subchar=my_char[7:]
    print(subchar)
    #4. Perform arithmetic operations with numbers  and print the results .
    #Addition
    result=5+4
    print("Addition:",result)
    #subtraction
    result=8-5
    print("subtraction:",result)
    #multiplication
    result=4*3
    print("Multiplication:",result)
    #Division
    result=15/3
    print("Division:",result)
    #Modulus
    result=10%3
    print("Modulus:",result)
    #Floor Division
    result=15//4
    print("Floor Division:",result)
    #Expontentiation
    result=2**3
    print("Expontentiation:",result)

    #5.Use booloean values and conditions to control program flow.
    #Conditional Statements
    x=5
    if x>10:
        print ("x is greater than 10")
    elif x>5:
        print("x is greater than 5")
    else:
        print("x is 5 or less")   
    #Logical operatores (and , or, and not)
    x=5
    y=12
    if x>0 and y>0:
         print ("Both x and y are positive ")  
    elif x>0 or y>0:
        print("Either x  or y(or both) is positive")
    else:
        print("Neither x nor y is positive")
  
     #Comparison Operators 
    x=8
    if x>10:
        print ("x is greater than 10")
    elif x==10:
        print ("x is equal to 10")
    else:
        print("x is less than 10")       


