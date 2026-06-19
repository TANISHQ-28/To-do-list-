def viewtask(a):
  if len(a)==0:
    print("No tasks available")
  for i in range(1,len(a)+1):
     print(f"{i}. {a[i-1]}")
  

def addtask(a):
  n = input("\nEnter the task you want to add : ")
  a.append(n)

def deletetask(a):
  try :
  
    n = int(input("Enter the task number you want to delete : "))

    if n<1 or n>len(a):
      print("Value out of Bound!")

    for i in range(1, len(a)+1):
      if (i-1) == n-1:
        b = a.pop(i-1)
    print(f"\nThe deleted task is '{b}'\nTask deleted Successfuly.")

  except ValueError:
    print("\nValueError occurred!\nEnter a valid integer value.")


#use while loop then only addition problem will be solved.
print("Your tasks are stored pefectly in this program.")
print("To add, delete and view your tasks press :\n1. To view tasks\n2. To add a new task\n3. To delete a task\n4. To exit the program")
l1 = ["Python Project","Hit the gym", "Meditate"]

while True:
  try:
    a = int(input("\nEnter the choice : "))

    if a == 1: 
      viewtask(l1)

    elif a == 2:
      addtask(l1)
      print("\n")

    elif a == 3:
      deletetask(l1)
  
    elif a == 4:
      print("\nExiting the program......\nExited Successfuly!")
      break

    else: 
      print("\nInvalid Entry! Please read the instructions carefully.")
    
  except ValueError:
    print("ValueError occurred!\nEnter a valid integer value.")


