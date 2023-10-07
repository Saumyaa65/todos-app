import Functions

while (True):
    user_action=input("enter add, show, edit, complete or exit"+"\n")
    user_action=user_action.strip()

    if user_action.startswith("add"):
        todo = user_action[4:] + "\n"

        todos= Functions.open_read()
        todos.append(todo)
        Functions.open_write(todos)

    elif user_action.startswith("show"):
        todos= Functions.open_read()
        for index, todo in enumerate(todos):
            print(f"{index+1}-{todo}".strip('\n'))

    elif user_action.startswith("edit"):
        index=int(user_action[5:])
        index=index-1;
        new_todo=input("enter new todo\n") + "\n"

        todos= Functions.open_read()
        todos[index]=new_todo
        Functions.open_write(todos)

    elif user_action.startswith("complete"):
        index = int(user_action[9:])
        index = index - 1;

        todos= Functions.open_read()
        todos.pop(index)

        Functions.open_write(todos)

    elif user_action.startswith("exit"):
        break

    else:
        print("Sorry, you entered wrong input. Please try again.")

print ("bye")
