# Data Structures and Algorithms: Task 3

## Overview

This repository contains the solutions to selected questions of **Data Structures and Algorithms (DSA) Task 3**. The solutions are implemented in **Python** (Questions 1, 4, 5 and 6) and **C** (Question 7). The other questions were handwritten and will be presented as a scan pdf.

---

## Table of Contents

1. [Repository Structure](#repository-structure)
2. [Summary of Questions](#summary-of-questions)
3. [Question 1: Circular Queue](#question-1-circular-queue-python)
4. [Question 2: Applications of Stacks](#question-2-applications-of-stacks)
5. [Question 4: Recursive Programs](#question-4-recursive-programs-python)
6. [Question 5: Enqueue and Dequeue](#question-5-enqueue-and-dequeue-python)
7. [Question 6: Sparse Matrix Using Arrays](#question-6-sparse-matrix-using-arrays-python)
8. [Question 7: Double-Ended Queue (Deque)](#question-7-double-ended-queue-deque-c)
9. [Programming Languages Used](#programming-languages-used)
10. [Concepts Demonstrated](#concepts-demonstrated)
11. [How to Run](#how-to-run)

---

## Repository Structure

| File | Question | Language |
|------|----------|----------|
| `circular_queue.py` | Question 1 | Python |
| `sum_of_first_N_numbers.py` | Question 4(a) | Python |
| `factorial.py` | Question 4(b) | Python |
| `Nth_fibonacci_term.py` | Question 4(c) | Python |
| `Nterms_of_fibonacci_series.py` | Question 4(d) | Python |
| `Q5_enqueueanddequeue.py` | Question 5 | Python |
| `sparse_matrix.py` | Question 6 | Python |
| `double_ended_enqueue.c` | Question 7 | C |

---

## Summary of Questions

| Question | Topic | Type |
|----------|-------|------|
| 1 | Circular Queue | Implementation (Python) |
| 2 | Applications of Stacks | Theory |
| 4 | Recursive Programs | Implementation (Python) |
| 5 | Enqueue and Dequeue Operations | Implementation (Python) |
| 6 | Sparse Matrix Using Arrays | Implementation (Python) |
| 7 | Double-Ended Queue (Deque) | Implementation (C) |

---

## Question 1: Circular Queue (Python)

**File:** `circular_queue.py`

A Circular Queue is implemented in Python. It overcomes the memory wastage problem associated with linear queues by reusing empty spaces through the circular movement of the front and rear pointers.

---

## Question 2: Applications of Stacks

A stack is a linear data structure that follows the **Last In, First Out (LIFO)** principle. It is commonly used in:

- Function calls
- Expression evaluation
- Undo operations
- Browser history management

---

## Question 4: Recursive Programs (Python)

Recursive functions are implemented to solve the following problems.

| Part | Problem | File | Description |
|------|---------|------|-------------|
| (a) | Sum of First N Natural Numbers | `sum_of_first_N_numbers.py` | Calculates the sum of natural numbers from 1 to N using recursion. |
| (b) | Factorial | `factorial.py` | Calculates the factorial of a given number using recursion. |
| (c) | Nth Fibonacci Term | `Nth_fibonacci_term.py` | Finds a specific term in the Fibonacci sequence using recursion. |
| (d) | N Terms of Fibonacci Series | `Nterms_of_fibonacci_series.py` | Generates the first N terms of the Fibonacci sequence. |

---

## Question 5: Enqueue and Dequeue (Python)

**File:** `Q5_enqueueanddequeue.py`

Basic queue operations are implemented in Python:

- **Enqueue:** Adds an element to the rear of the queue.
- **Dequeue:** Removes an element from the front of the queue.

---

## Question 6: Sparse Matrix Using Arrays (Python)

**File:** `sparse_matrix.py`

A sparse matrix representation is implemented using arrays in Python. Only the non-zero elements are stored, together with their row and column positions. This reduces memory usage compared to storing the entire matrix.

---

## Question 7: Double-Ended Queue (Deque) (C)

**File:** `double_ended_enqueue.c`

A Double-Ended Queue is implemented using arrays in C. The program supports four main operations:

1. Front Insertion
2. Rear Insertion
3. Front Deletion
4. Rear Deletion

The implementation uses a circular array to manage queue elements efficiently.

---

## Programming Languages Used

- **Python:** Questions 1, 4, 5 and 6
- **C:** Question 7

---

## Concepts Demonstrated

- Linear and circular queues
- Stack data structures
- Recursion
- Fibonacci sequence
- Sparse matrix representation
- Array-based data structures
- Double-ended queue operations

---

## How to Run

**Python programs** (requires Python 3):

```bash
python <filename>.py
```

Example:

```bash
python circular_queue.py
```

**C program** (requires a C compiler such as GCC):

```bash
gcc double_ended_enqueue.c -o double_ended_enqueue
./double_ended_enqueue
```
