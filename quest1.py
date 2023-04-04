class Stack:
    def __init__(self):
        self.stack_list = []

    def is_empty(self):
        if len(self.stack_list) == 0:
            return True
        else:
            return False

    def push(self, element):
        self.stack_list.append(element)

    def pop(self):
        result = self.stack_list.pop(-1)
        return result

    def peek(self):
        result = self.stack_list[-1]
        return result

    def size(self):
        result = len(self.stack_list)
        return result


if __name__ == "__main__":
    first_stack = Stack()
    print(first_stack.is_empty())
    first_stack.push("One")
    print(first_stack.size())
    print(first_stack.pop())
    first_stack.push(1)
    first_stack.push(2)
    print(first_stack.peek())
