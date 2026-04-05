#114. 📝 To-Do List Manager

todo_list = []

choice = input("Enter Your Choice (add/remove/display/quit): ")

if choice.lower() == 'add':
    task = input("Enter Task to add: ")
    todo_list.append(task)

elif choice.lower() == 'remove':
    task = input("Enter Task to remove: ")
    if task in todo_list:
        todo_list.remove(task)
    else:
        print("❌ Task not found in the list")

elif choice.lower() == 'display':
    if todo_list:
        print("Your To-Do List:")
        for task in todo_list:
            print(task)
    else:
        print("Your To-Do List is Empty")

elif choice.lower() == 'quit':
    print("👋 Thanks for using To-Do List Manager. Goodbye!")

else:
    print("❌ Invalid Choice")
