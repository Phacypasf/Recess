#create a list with 5 items (nameds of people ) and write a python program to output the 2nd item
people=['brenda', 'Sarah', 'Joan','Claire','Mercy']
second_item=people[1]
print(second_item)
#Write a python program to change the value of the first  item to a new  a new value
#  
people[0]='Gloria'
print("modified:",people)
#write a python program tomadd a sixth item to the list
people=people+["Fred"]
print("modified:",people)
#write a python to add "Bathel as the 3rd  item  from the list"
people.insert(2,"Bathel")
print("modified:",people)
# write  a program to remove  the 4th item from the list
del people[3]
print("modified:",people)
#use negative  indexing to print the last item in your list
last=people[-1]
print("Last:",last)
#create  a new list with 7 items and use a range of indexes to print  the 3rd  and the 4th and the 5th item
fruits=['mangoes','oranges','apples','pears','grapes','bananas','tomatoes','onions']
third_item=fruits[2]
fourth_item=fruits[3]
fifth_item=fruits[4]
print("\n3rd:",third_item)
print( "\n4th:",fourth_item)
print("\n5th:",fifth_item  )

#write a list of countries and make a copy of it
countries=['Uganda','Kenya','Rwanda']
copied=list(countries)
print ("copy:",countries)
#write   a  program to loop through the list of countries
for states in countries:
    print(states)
# Write a list of animal names and sort them in descending and ascending order
animal=["antelope","cow","dog","donkey"]
animal.sort()
print("ascending:",animal)
animal.sort(reverse=True)
print("descending:",animal)
# using the list above , write a python program to output only animal names with the letter'a' in them
for animals in animal:
    if animals[0]=='a':
        print (animals)

# write two lists , one containing ypur first names and the other you second names .join the two lists
first_name=["Brenda"]
second_name=["Acan"]
joined=first_name + second_name
print(joined)


#Exercise two
x=("samsung"  "iphone","tecno","redmi")
favourite= x[1]
print("Favourite:",favourite)
#2
second_last_item=[-2]
print("Second_last_item:",second_last_item)
#3
updated=list(x)
updated[1]="itel"
print("updated:",x)
#4
x=x+("Hawei",)
print("added:",x)
#5
for item in x:
    print(item)
#6
x=x[1:]
print("first item removed:",x)
#7
cities=tuple(['kampala','Entebbe','Jinja','Mbarara'])
print("Cities:",cities)
#8
phone1,phone2,phone3=x
print("unpacked:",phone1, phone2, phone3, )
#9
print(cities[1:4])
#10
first_names=("John","Jane")
second_names=("Doe","Smith")
joined=first_names+second_names
print(joined)
#11
colors=("red","blue","pink")
multiplied=colors*3
print(multiplied)
#12
tuple=(1,3,7,8,7,5,4,6,8,5)
count_8=tuple.count(8)
print(count_8)

#Exercise 3
#1
favourite_beverages=set(["coffee","tea","juice"])
print("favourite:",favourite_beverages)
#2
favourite_beverages.add("water")
favourite_beverages.add("soda")
print(favourite_beverages)
#3
myset={"oven","kettle","microwave","refrigerator"}
if "microwave" in myset:
    print("is present")
else:
    print("not present")

 #4 
myset.remove("kettle")
print (myset)      
#5
for item in myset:
    print(item)

#6
myset=myset.union(["blender","toaster"])
print(myset)
#7
ages={25,30,35}
first_names={"Joan","Braib","Liz"}
joined=ages.union(first_names)
print(joined)

#Exercise 4
#1
interger=10
string="years old"
cont=str(interger)+ string
print(cont)
#2
txt="Hello,Uganda!"
output=txt.strip()
print(output)
#3 convert thevalue of txt  to uppercase
uppercase=txt.upper()
print("Uppercase String:",uppercase)
#4 Replace the character 'U' with 'V' in the string
replaced=txt.replace("U","V")
print("String with replaced caharacter:",replaced)
#5
y ="Iam proudly Uganadan"
range_of_characters=y[1:4]
print("Range of Characters:",range_of_characters)
#6
x='All"Data Scientists" are cool!'
print("corrected code:",x)

#EXERCISE5
1. #Print the value of the  shoe size
shoes={"brand":"Nick",
       "color":"black",
          "size":40

}
shoe_size=shoes["size"]
print("shoe_size:",shoe_size)
2# change the value"Nick" to"Adidas"
shoes["brand"]="Adidas"
print("updated brand:",shoes["brand"])
3#Add a key
shoes["type"]="sneakers"
print("updated dictionary:",shoes)
4#Return a list of all the keys
list=list(shoes.keys())
print("List of keys:",list)
5#Return a list of all values
for value in shoes.values():
    print(value)
6#check if size exists
if " size" in shoes:
    print("exists")
else:
    print("doesnot exist")   
7#Loop through the dictionary
for key, value in shoes.items():
     print(key,":",value)  
8#Remove color
shoes.pop("color")
print(shoes)  
9#Empty the dictionary
shoes.clear()
print(shoes)
10#Create a dictionary and its copy
original={"name":"John","age":30} 
copy=dict(original) 
print(copy)   
11#Nested dictionary
nested={"person1":{
    "name":"John",
    "age":30},
    "person2":{
        "name":"Jane",
        "age":25
    }
}
print (nested)
