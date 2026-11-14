
#include <stdio.h>
#define MAX 5

int deque[MAX];
int front = -1;
int rear = -1;

// Check whether the deque is full
int isFull() {
    return ((front == 0 && rear == MAX - 1) ||
            (front == rear + 1));
}

// Check whether the deque is empty
int isEmpty() {
    return (front == -1);
}

// a. Insert an element at the front
void insertFront(int value) {
    if (isFull()) {
        printf("Deque Overflow!\n");
        return;
    }

    if (isEmpty()) {
        front = rear = 0;
    }
    else if (front == 0) {
        front = MAX - 1;
    }
    else {
        front--;
    }

    deque[front] = value;
    printf("%d inserted at front.\n", value);
}

// b. Insert an element at the rear
void insertRear(int value) {
    if (isFull()) {
        printf("Deque Overflow!\n");
        return;
    }

    if (isEmpty()) {
        front = rear = 0;
    }
    else {
        rear = (rear + 1) % MAX;
    }

    deque[rear] = value;
    printf("%d inserted at rear.\n", value);
}

// c. Delete an element from the front
void deleteFront() {
    if (isEmpty()) {
        printf("Deque Underflow!\n");
        return;
    }

    printf("Deleted from front: %d\n", deque[front]);

    if (front == rear) {
        front = rear = -1;
    }
    else {
        front = (front + 1) % MAX;
    }
}

// d. Delete an element from the rear
void deleteRear() {
    if (isEmpty()) {
        printf("Deque Underflow!\n");
        return;
    }

    printf("Deleted from rear: %d\n", deque[rear]);

    if (front == rear) {
        front = rear = -1;
    }
    else if (rear == 0) {
        rear = MAX - 1;
    }
    else {
        rear--;
    }
}

// Display deque elements
void display() {
    if (isEmpty()) {
        printf("Deque is empty!\n");
        return;
    }

    int i = front;

    printf("Deque elements: ");

    while (1) {
        printf("%d ", deque[i]);

        if (i == rear)
            break;

        i = (i + 1) % MAX;
    }

    printf("\n");
}

// Main function
int main() {
    insertRear(10);
    insertRear(20);
    insertFront(5);

    display();

    deleteFront();
    deleteRear();

    display();

    return 0;
}
