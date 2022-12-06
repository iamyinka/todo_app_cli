user_prompt = "Enter a todo >> "

todos = []

while True:
    user_input = input("Type add, show or exit, to continue [x:]>> ")

    match user_input:
        case 'add':
            todo = input(user_prompt)
            todos.append(todo)

        case 'show':
            print(todos)
        
        case "exit":
            break