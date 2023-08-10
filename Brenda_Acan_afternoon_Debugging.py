#Syntax Error
amount =10000
if(amount>2999)
print("You are eligible to purchase")

#Exceptions
marks =100000
a=marks/0
print(a)
 #1 Type error 
x=6
y="hi"
z =x+y
print(z)
# Try catch to resolve
x=7
y="Jambo"
try:
    z=x+y

except TypeError:
    print("Error:cannot add init and string")

#IndexError
try:
    numbers=[1,2,3,4,5]
    index=int(input("Please enter a number"))
    value=numbers[index]
    print ("The value at index ", index ,"is", value, )
except IndexError:
    print("Value at index" ,index," is  out of range")
finally:
 print ("the final block is allways executed")


 #file handling
 #f=open(filename,mode)
 #Read mode
 file=open("file.txt","r")
 for each in file:
    print(each)
 print(file.read())
 # read() method character wise
 print(file.read(5))

 #write mode
 file =open(" file.txt","w")
 file.write("This is a write command")
 file.write("It can allow us tomwrite in a file")
 file.close()

 #Appemd mode
 file=open("file.txt","a")
 file.write("This will add this line")
 file.close()
 #Trial
 def read_file(filename):
    try: 
        with open ( filename,'r') as file:
             contents= file.read()
             print(contents)
    except FileNotFoundError:
        print("File not found")
    except IOError:
        print ("error readin the file")

def write_file(filename,content):
    try:
        with open(filename,'w') as file:
            file.write(content)
            print("File Written sucessfully") 
    except IOError:
        print("Error writing to the file") 
file_name="files.txt"
content_to_write="Hello_World"

write_file(file_name,content_to_write)
read_file(file_name)
  




