print("Hello! Good Morning!")
print("Lets start coding for today!!")

def get_todos(filepath):
    with open(filepath, 'r') as file_local:
        todo_local = file_local.readlines()
    return todo_local

while True:
    user_action = input("Enter type add , show ,edit or exit:")
    user_action = user_action.strip()

    if user_action.startswith("add"):
        try:
            todo = user_action[4:]

            todos = get_todos("todos.txt")

            todos.append(todo + '\n')

            with open("practice/list.txt", 'w') as file:
                file.writelines(todo)
        except ValueError:
            print("Your command is not valid.")
            continue

    elif user_action.startswith('show'):

        todos = get_todos("todos.txt")

        for index, item in enumerate(todos):
            item = item.strip('\n')
            row = f"{index + 1}.{item}"
            print(row)

    elif user_action.startswith('edit'):
        try:
            number = int(user_action[5:])
            print(number)

            number = number - 1

            todos = get_todos("todos.txt")

            edited_list = input("Enter new todo: ")
            todos[number] = edited_list + '\n'

            with open('practice/list.txt', "w") as file:
                file.writelines(todo)
        except IndexError:
            print("Your commmand is not valid.")
            continue

    elif user_action.startswith('exit'):
        break

    else:
        print("Command not valid:")

print("THANK YOU FOR CODING!!!")




