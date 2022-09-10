stack = []

# insert(5) - insert(2) - insert(3) - insert(7) - delete() - insert(1) - insert(4) - delete()
stack.append(5)
stack.append(2)
stack.append(3)
stack.append(7)
stack.pop()
stack.append(1)
stack.append(4)
stack.pop()

print(stack) # [5,2,3,1]
print(stack[::-1]) # [1,3,2,5]
