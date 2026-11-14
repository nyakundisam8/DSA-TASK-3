class Queue:
    def __init__(self, capacity=5):
        self.capacity = capacity
        self.items = []

    def enqueue(self, x):
        if len(self.items) == self.capacity:
            print("Queue Overflow")
        else:
            self.items.append(x)
            print(f"Enqueued {x}")

    def dequeue(self):
        if not self.items:
            print("Queue is Underflow")
            return None
        x = self.items.pop(0)
        print(f"Dequeued {x}")
        return x

    def display(self):
        print("Queue (front -> rear):", self.items)

 # demonstrates the enqueue and the dequeue functions


def q5_demo():
    print("\n=== Q5: Queue enqueue/dequeue ===")
    q = Queue(3)
    for x in (1, 2, 3, 4):
        q.enqueue(x)
    q.display()
    q.dequeue()
    q.dequeue()
    q.display()
