def viewtask(a):
  if len(a)==0:
    print("No tasks available")
    return
  for i in range(1,len(a)+1):
     print(f"{i}. {a[i-1]}")

def addtask(a):
  n = input("\nEnter the task you want to add : ")
  a.append(n)

  with open("tasks.txt", "a") as f:
    f.write(n + "\n")


def deletetask(a):
  try :
  
    n = int(input("Enter the task number you want to delete : "))

    if n<1 or n>len(a):
      print("Value out of Bound!")

    b = a.pop(n-1)
    with open("tasks.txt", "w") as f:
      for task in a:
        f.write(task + "\n")
      
    print(f"\nThe deleted task is '{b}'\nTask deleted Successfuly.")

  except ValueError:
    print("\nValueError occurred!\nEnter a valid integer value.")

#use while loop then only addition problem will be solved.
print("Your tasks are stored pefectly in this program.")
print("To add, delete and view your tasks press :\n1. To view tasks\n2. To add a new task\n3. To delete a task\n4. To exit the program")

with  open("tasks.txt", "r") as f:
  task = f.read()
# print(repr(task))
s = task.splitlines()
t = list(s)

while True:
  try:
    a = int(input("\nEnter the choice : "))

    if a == 1: 
      viewtask(t)

    elif a == 2:
      addtask(t)
      print("\n")

    elif a == 3:
      deletetask(t)
  
    elif a == 4:
      print("\nExiting the program......\nExited Successfuly!")
      break

    else: 
      print("\nInvalid Entry! Please read the instructions carefully.")
    
  except ValueError:
    print("ValueError occurred!\nEnter a valid integer value.")
