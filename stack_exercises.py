from collections import deque

class Stack:
    def __init__(self):
        self.container = deque()

    def push(self,value):
        self.container.append(value)

    def pop(self):
        return self.container.pop()

    def peek(self):
        if self:
            return self.container[-1]

    def is_empty(self):
        return len(self.container) == 0

    def __len__(self):
        return len(self.container)

# 1
def reverse_string(string):
    stack = Stack()
    for let in string:
        stack.push(let)

    t = ''
    while not stack.is_empty():
        t += stack.pop()

    return t

print(reverse_string("We will conquere COVID-19"))


# 2

def is_balanced(string):
    hashmap = {
        '(' : ')',
        '[' : ']',
        '{' : '}'
    }
    stack = Stack()

    for sym in string:
        if sym in hashmap.keys():
            stack.push(hashmap[sym])

        if sym in hashmap.values():
            if stack.peek() != sym:
                return False
            else:
                stack.pop()

    return True


print(is_balanced("({a+b})"))
print(is_balanced("))((a+b}{"))
print(is_balanced("((a+b))"))
print(is_balanced("))"))
print(is_balanced("[a+b]*(x+2y)*{gg+kk}"))
print(is_balanced("([)]"))
