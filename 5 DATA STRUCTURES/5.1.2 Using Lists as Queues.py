from collections import deque

# Lists can also be used as queues however they are not efficient for this purpose.
# The designated queue data structure is more fit for purpose.

# Convert list to queue
q = deque([4, 2, 9])
print(q)
q.append(3)
print(q)
print(q.popleft())
print(q.popleft())
print(q.popleft())
q.append(5)
print(q)
