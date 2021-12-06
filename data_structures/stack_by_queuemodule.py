from queue import LifoQueue

stack = LifoQueue(4)       # argument to limit the size of stack
print(type(stack))

stack.put(4)

# print(stack[-1])     --------------->will not work as LifoQueue is not subscriptable

stack.put(8)
stack.put(68)
stack.put(89)
# stack.put(90,timeout=1)         # stack is now full

print(stack.get())
print(stack.get())
print(stack.get())
print(stack.get())
stack.get(timeout=0.1)             # stack is now empty