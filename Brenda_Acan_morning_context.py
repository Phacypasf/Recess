#Context Manager
#context manager is an object that defines a temporary context of a block of code.
#Example1
#Demonstrate  a context manager to open a file and returns a context manager instance
#def open_file(filename):
    #open a file and return a context manager instance
 #   file=open(filename,"r")

   # def __enter__():
    #  return file 
   

    #def   __exit__(self,exc_type,exc_value,exc_tb):
     #  file.close()

      # return __enter__.__exit__
    
#with open_file("my_file.txt")  as f:
   #contents=f.read()

#Example2 Demonstrate a context Manager
import time

from isoduration import DurationFormattingException
class Timer:
   def __enter__(self):
      self.start_time=time.time()

   def __exit__(self,exc_type,exc_value,traceback):
      end_time = time.time()
      execution_time = end_time - self.start_time
      print(f"The time for this execution {execution_time} seconds elapsed")      

with Timer():
   #measure the execution  time
   time.sleep(2)

#Example3
# multithreading and multiprocessing
#techniques that can be used to improve the performance of a python program
# Multithreading is a technique where multiple threads are created  with  single program
# Multiprocessing is a technique  where multiple threads a re connected   
#Multithreading
import threading

def task(name):
   print(f"Running task{name}")


#Create multiple threads
threads=[]
for i in range(10):
   t= threading.Thread(target=task,args=(f"Thread{i}",))
   threads.append(t)
   t.start()
#  wait for all threads to finish
for t in threads:
   t.join() 

#Example4
# Multiprocessing
# Demonstrate
#import multiprocessing
#def process_task(name):
 #  print(f"processing task{name}")

#create a pool of  processes
#pool =multiprocessing.Pool(processes=5)     

#submit multiple task to the pool
#for i in range(6):
 #  pool.apply_async(process_task,args=(f"process{i}",))


#pool.close()
#pool.join()   


#Example5
#multithreading and multiprocessing
import threading
import multiprocessing

def task(name):
   print(f"Running task{name}on thread{ threading.current_thread().name} with process{multiprocessing.current_process().name}" )
#create multiple threads to run
   threads=[]
for i in range(4):
   t= threading.Thread(target=task,args=(f"Thread{i}",))
   threads.append(t)
   t.start()
#  wait for all threads to finish
for t in threads:
   t.join() 

#Assingnment
#1a)Show a context manager for file handling that automatically opens and closes a file
#b)Show a context Manager for managing  a database connection
#c)Show a multithreading and multiprocessing that allows us to run  the function for the different amounts of time
#1a)
class FileHandler:
   def __init__(self,filename,):
      self.filename=filename
   
      
   def __enter__(self):
      self.file=open(self.filename,"w")
      return self.file
   def __exit__(self,exc_type,exc_val,exc_tb):
       if self.file:
          self.file.close()




with FileHandler("Hello.txt") as file:
  
 file.write("hello,world!")
   
#b)
import sqlite3
class DatabaseManager:
   def __init__(self,db_name):
      self.db_name=db_name

   def __enter__(self):
      self.connection=sqlite3.connect(self.db_name)
      return self.connection
   def __exit__(self,exc_type,exc_val,exc_tb):
      if self.connection:
         self.connection.close()

with DatabaseManager("Cast.db")as db:
   cursor=db.cursor()
   cursor.execute("CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY,name TEXT)")         
   cursor.execute("INSERT INTO users(name) VALUES ('Brenda')")
   db.commit()

#c)import threading
import  multiprocessing
import time

def function(duration):
    print(f"starting function for {duration} seconds")
    time.sleep(duration)
    print(f"Function completed for {duration} seconds")

if __name__=="__main__":
    threads=[]
    durations=[2,4,6,8,10]


    for duration in durations:
        thread=threading.Thread(target=function,args=(duration,))       
        thread.start()
        threads.append(thread)


    for thread in threads:
        thread.join()


    print("Multithreading completed")


    processes=[]
    durations=[1,3,5,7,9]

    for duration in durations:
     process =multiprocessing.Process(target=function,args=(duration,))   
     process.start()
     processes.append(process)    

    for process in processes:
       process.join()
    print("multiprocessing completed")     
