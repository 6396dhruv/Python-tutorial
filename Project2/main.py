# calculator with saving history

def show_history():
    file = open("history.txt", "r")
    lines = file.readlines()
    if len(lines) ==0:
        print("No history found!")
    else:
        for line in reversed(lines):
            print(line.strip())
    file.close()

def clear_history():
    file = open("history.txt", "w")
    file.close()
    print("History cleared.")

def save_history(equation, result):
    file = open("history.txt", 'a')
    file.write(equation + "=" + str(result) + "\n")
    file.close()

def calculate(user_input):
    parts = user_input.split()
    if len(parts)!= 3:
        print("Invalid input. use format number operator number (eg- 6+6)")
        return
    num1 = float(parts[0])
    op = parts[1]
    num2 = float(parts[2])

    if op == "+":
        result = num1 + num2
    elif op == "-":
        result = num1 - num2
    elif op == "*":
        result = num1 * num2
    elif op == "/":
        if num2 == 0:
            print("You can not divide with zero")
            return
        result = num1 / num2
    else:
        print("Invalid operator.")
        return
    
    if int(result) == result:
        result = int(result)
    print("Result: ", result)
    save_history(user_input, result)

def main():
    print("Simple Calculator (type history, clear or exit)")
    while True:
        user_input = input("Enter calculations (+ - * /) or command (history, clear and exit) = ")
        if user_input == "exit":
            print("Good Bye!")
            break
        elif user_input == "history":
            show_history()
        elif user_input == "clear":
            clear_history()
        else:
            calculate(user_input)

main()


 

