#length of set
my_set={1,2,3}
length=len(my_set)
print(length)
#How to access items in aset
   #iterating over aset
my_set={1,2,3,4}
for item in my_set:
     print(item)
     #checking for the presence of an item
     my_set={1,2,5,7}
     if 2 in my_set:
       print("Item 2 is present in  the set")
#How to add items to a set
#add()method
my_set={12,13,14}
my_set.add(15)
print(my_set)
#update()method
my_set={1,2,3,4}
my_set.update([5])
print(my_set)
#adding two sets together
#union ()method
set1={1,5}
set2={2,4}
combined_set=set1.union(set2)
print(combined_set)



