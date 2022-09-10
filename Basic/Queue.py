from collections import deque

queue = deque()

# insert(5) - insert(2) - insert(3) - insert(7) - delete() - insert(1) - insert(4) - delete()
queue.append(5)
queue.append(2)
queue.append(3)
queue.append(7)
queue.popleft()
queue.append(1)
queue.append(4)
queue.popleft()

print(queue) # [3,7,1,4]
queue.reverse()
print(queue) # [4,1,7,3]
