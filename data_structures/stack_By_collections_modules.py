from collections import deque

stack = deque()
print(type(stack))

stack.append(9)
print("top = ", stack[-1])
stack.append(7)
print("top = ", stack[-1])
stack.append(0)
print("top = ", stack[-1])
stack.append(5)
print(stack)

print("top = ", stack[-1])

print(stack.pop())
print(stack.pop())
print(stack.pop())
print(stack.pop())
# print(stack.pop())            #error-->empty stack

# " To check stack is empty"
print(not stack)