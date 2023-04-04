from quest1 import Stack


def main_func():
    base_stack = Stack()
    bracket_string = list(input())
    error = True
    for element in bracket_string:
        if element == "(" or element == "{" or element == "[":
            base_stack.push(element)
        else:
            if base_stack.is_empty():
                error = False
                break
            top = base_stack.peek()
            if (
                (top == "(" and element == ")")
                or (top == "[" and element == "]")
                or (top == "{" and element == "}")
            ):
                base_stack.pop()
            else:
                error = False
                break
    if base_stack.is_empty() and error:
        print("Сбалансированно")
    else:
        print("Несбалансированно")


if __name__ == "__main__":
    main_func()
