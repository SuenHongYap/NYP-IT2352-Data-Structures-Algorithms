# NYP-IT2352-Data-Structures-Algorithms

In this individual assignment, there are 3 components (see a to d below) to this assignment:
  1. Part 1a: Sales Inventory – Basic Features
  2. Part 1b: Sales Inventory – Search and Sort Algorithms
  3. Part 2: Challenge Question on Algorithm

Part 1 is related to the development of a Sales Inventory. Part 2 is a challenge question on algorithm.

# Part 1: Sales Inventory

The purpose of the Sales Inventory is to allow the user to manage sales records. They can display, add, update and remove product records from the inventory, perform searching and sorting of records, and other additional features that improve the usefulness of the application for the user.

1. Sales Inventory – Basic Features
    1. Design a suitable data structure (e.g. by making use of Python list, dictionary, objects, etc.) to manage the product records. You are required to store the following product records with information such as: **record index, Product Name, Unit Price, Quantity and at least TWO OTHER information** of your choice. Each record will have the above attributes. The application inventory will store up to 20 records.
    2. Design a **menu** for the application to allow the user to perform the following:
        1. Add Record
        2. Update Selected Record
        3. Remove Record
        4. Display All Records
        5. Sort Record
        6. Search Record
        7. Exit Application
      3. Complete the (Add, Update, Remove and Display) operations
      
2. Sales Inventory – Search and Sort Algorithms. Add the following features to the Sales Inventory;
    1. Complete the Sort Record option. Student must implement 3 sorting algorithms. They are **Bubble, Selection and Insertion Sort** algorithms to sort records based on a sort key e.g. Product Name, Quantity etc. Student can decide on which sort key to apply.
    2. Complete the Search Record option. Student will apply 2 search algorithms. They are **Linear and Binary Search** algorithm to search for record based on a search key. Student will decide which search key but must implement both search algorithms.
    3. Student may add in bonus features such as exception handling, advanced algorithms etc.

# Part 2: Challenge Question on Algorithm

This challenge question will test you on the design and implementation of an **efficient algorithm** to solve the following problem.

Given a sequence of positive integers, **SEQ**, sorted in ascending order, design and implement an algorithm with Python to determine if there exist two integers **X and Y** in the sorted sequence such that **X XNOR Y = -1**.

(**NOTE**: A brute-force algorithm compares all possible pairs in the sorted sequence and check if they Exclusive NOR to -1. However, using this approach will only give you a minimal score.)

For example, if SEQ is provided to your program as follows:

**SEQ:**
| 1 | 2 | 3 | 3 | 4 | 4 | 4 | 10 | 10 | 10 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

The sample output is given below:
X=3, Y=3
X=4, Y=4
X=4, Y=4
X=4, Y=4
X=10, Y=10
X=10, Y=10
X=10, Y=10
Total match is 7.
