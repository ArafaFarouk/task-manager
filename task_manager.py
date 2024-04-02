tasks = []

def main():
  
  message ="""
  1- add taske to a list 
  2- mark task as complete
  3- view tasks
  4- quit"""
 
  while True:
    print(message)
    choice = input("enter your choice: ")
  
    if choice == "1":
      add_task()
    elif choice == "2":
      mark_task_complete()
    elif choice == "3":
      view_tasks(tasks)
    elif choice == "4":
      break
    else:
      print("invalid choice , please enter a number between 1 and 4")
  
def add_task():
  # get task from user 
  task = input("Enter a task: ")
  
  # defin task status as not completed
  task_info = {"task": task, "completed": False} 
  
  # add task to the list of tasks
  tasks.append(task_info)
  print("task addes to the list succesfully")
  
def mark_task_complete():
  # get list of incomplete tasks 
  incomplete_tasks = [task for task in tasks if task["completed"] == False]
  
  # if len (incomplete_tasks) == 0:
  #   print("no tasks to mark as complete")
  #   return
  # "يقوم الكود التالى بنفس مهمة الكود السابق "تأكد من وجود مهام لتمكينها
  if not incomplete_tasks:
    print("no tasks to mark as complete")
    return
    
  # show incompleted tasks to user
  for i, task in enumerate(incomplete_tasks):
    print(f"{i+1}- {task['task']}")
    print("-"*30)
    
  # get task index from user
  try:
    task_index = int(input("Enter task number to complete: "))
    # mark task as complete
    incomplete_tasks[task_index -1]["completed"] = True
    # print message to user 
    print("task marked as complete")
  except ValueError:
    print("invalid input , please enter a number")
  except IndexError:
    print("pleas enter a number between 1 and", len(incomplete_tasks))
          
def view_tasks(tasks_list):
  # if there are no tasks to view, print message & return
  if not tasks_list:
    print ("No tasks to view")
    return
  for i, task in enumerate(tasks_list):
  #   if task["completed"]:
  #     status = "✔"
  #   else:
  #     status = "❌"
  # يقوم الكود التالى بنفس مهمة الكود السابق عرض حالة المهمة 
    status = "✔" if task["completed"] else "❌"
    print(f"{i+1}.{task['task']}{status}")

if __name__ == "__main__" :
  main()
  


    
  