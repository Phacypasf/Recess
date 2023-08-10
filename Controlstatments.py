age=20
if age <15:
    print('You are young')
elif age >=15 and age<=65:
    print('you are an adult')
else:
    print (' you are a senior citizen')
#loops
#loops(for, while)
#for
fruits=('mango','apple','pears')
for fruit in fruits:
    print(fruit)
#while
fruits=('mango','apple','pears')
count=0
while count<len(fruits):
    print(fruits[count])
    count +=1 
#bBreak and continue statemnt
#break
for number in range(1,20):
    if number==10:
        break
    print(number)

phones=('samsung','redmi','tecno','infinix','oppo')
for phone in phones:
    if phone == 'tecno':    
         break
print(phone)
phones =('samsung','redmi','tecno','infinix','oppo')
for phone in phones:
    if phone=='tecno':
        continue
    print(phone)
    #pass statement
    #pass statement is a place holder  for code that eill be implemented later
    data="Hello"
    if  len(data)<5:
        pass
    else:
        print("process data:",data)
    
# exception handling(try,except,finally)
try:
    dividend= int(input("Enter the dividend:"))
    divisor=int(input("Enter the divisor:"))

    result=dividend/divisor
except ValueError:
     print("Error:Invalid input. please enter integer only.")
except ZeroDivisionError:
    print("Error :cannot divide by zero")
finally:
    print("Division process completed.") 

    #EXERCISE 
    #Mental health rating 
    print("Welcome to students mental health survey")
responses={
       'low':"Your mental  health rating is low .It is important to priotize your mental health"
       '\n moderate:'"Your mental health rating is moderate.Consider implementing  additional health care"
       '\n high:'"Your mental  rating is high. Keep up the good work and self - care" 
}    
try:
       user_name=input("Please enter your name")
       responses['Name']=user_name
       Question= int(input("on the scale of 1to 10 , how would you rate your mental health?(1=low,5=moderate,10=high)"))
       responses["rate"]= int(Question)
except ValueError:
       print("invalid response.Please  enter a number")
       Question=input("on the scale of 1to 10 , how would you rate your mental health?(1=low,5=moderate,10=high)")
       responses["rate"]=  int(Question)
finally : 
    
   for Question,responses in responses.items():
        print(Question+':',responses)
              