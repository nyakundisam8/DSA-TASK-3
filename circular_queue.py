# Create a circular queue
class CircularQueue:
    def __init__(self, size):
        self.size = size
        self.queue = [None] * size
        self.front = -1
        self.rear = -1

    # Insert an element
    def enqueue(self, item):
        if (self.rear + 1) % self.size == self.front:
            print("Queue is full")
            return

        if self.front == -1:
            self.front = 0

        self.rear = (self.rear + 1) % self.size
        self.queue[self.rear] = item

    # Remove an element
    def dequeue(self):
        if self.front == -1:
            print("Queue is empty")
            return

        item = self.queue[self.front]
        self.queue[self.front] = None

        if self.front == self.rear:
            self.front = self.rear = -1
        else:
            self.front = (self.front + 1) % self.size

        return item

    # Display queue
    def display(self):
        print(self.queue)


# Create queue of size 5
cq = CircularQueue(5)

cq.enqueue(10)
cq.enqueue(20)
cq.enqueue(30)
cq.display()

print("Deleted:", cq.dequeue())
cq.enqueue(40)
cq.display()