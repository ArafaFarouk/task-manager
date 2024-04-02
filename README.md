
**Simple Task Manager**

This Python program provides a user-friendly way to manage your tasks. It allows you to:

* Add tasks to a list
* Mark tasks as completed
* View all tasks (completed and incomplete)
* Exit the program

**Getting Started**

1. **Save the code:** Save the provided code as a Python file (e.g., `task_manager.py`).
2. **Run the program:** Open a terminal or command prompt, navigate to the directory where you saved the file, and run the following command:

   ```bash
   python task_manager.py
   ```

**Using the Program**

The program will display a menu with the following options:

```
1 - Add task to a list
2 - Mark task as complete
3 - View tasks
4 - Quit
```

Enter the number corresponding to the desired option:

* **1. Add task to a list:** When you select this option, you'll be prompted to enter a task description. The task will be added to your list with an "incomplete" status.
* **2. Mark task as complete:** This option allows you to mark completed tasks. The program will show a list of all incomplete tasks. Enter the number of the task you want to mark as complete. If you enter an invalid number, the program will display an error message.
* **3. View tasks:** This option displays all tasks in your list, indicating their completion status using a checkbox symbol (✔) for completed and an "X" symbol (❌) for incomplete tasks.
* **4. Quit:** Enter "4" to exit the program.

**Example Usage**

```
1 - Add task to a list
Enter a task: Buy groceries
task added to the list successfully

1 - Add task to a list
Enter a task: Finish report
task added to the list successfully

3 - View tasks
1. Buy groceries ❌
2. Finish report ❌

2 - Mark task as complete
Enter task number to complete: 1
task marked as complete

3 - View tasks
1. Buy groceries ✔
2. Finish report ❌

4 - Quit
Program exited
```

**Notes:**

* The program currently does not allow editing or deleting tasks. These features can be added in future enhancements.
* You can exit the program at any time by entering "4".
