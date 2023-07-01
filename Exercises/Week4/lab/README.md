# Big O Lab

**GOAL**: Complete the practice problems in `main.py`. As you complete problems, you can find the solutions on this document. Attempt the problems before looking at the solutions!

**NOTE ON RUNNING CODE**: To run code in the `slushy.py` file, type the following in the terminal:
```bash
python3 slushy.py
```

<details>

<summary><strong>Questions 1 to 3 solution</strong></summary>

1. `O(n)` --> Big O Linear
2. `O(1)` --> Big O independent
3. `O(n^2)` --> Big O squared

</details>
 
<details>

<summary><strong>Questions 5 solutions</strong></summary>

1. `practice1(n)` --> `O(n)`
2. `practice2(n)` --> `O(n^2)`
3. `practice3(n)` --> `O(n)`
4. `practice4(n)` --> `O(1)`
5. `practice5(n)` --> `O(n)`
6. `practice6(n)` --> `O(1)`
7. `practice7(n)` --> `O(log n)`
8. `practice8(n)` --> `O(n^2)`
9. `practice9(n)` --> `O(n)`
10. `practice10(n)` --> `O(n^3)`
11. `practice11(n)` --> `O(n)`
12. `practice12(n)` --> `O(n)`

</details>


<details>

<summary><strong>Questions 6 solution</strong></summary>

You may have noticed that `finaA` was a linear search and `findB` is doing a Binary Search. These have the following Big O:
- Linear search has a time complexity of `O(n)`. 
- Binary search has a special time complexity of `O(log n)`. 

</details>

# Big O Interview Questions

>[Sampled and modified from this repository](https://github.com/Devinterview-io/big-o-notation-interview-questions).

1. What is Big O notation?

<details>

<summary><strong>Show Answer</strong></summary>

Big-O notation (also called "asymptotic growth" notation) is a relative representation of the complexity of an algorithm. It shows how an algorithm scales based on input size. We use it to talk about how thing scale. Big O complexity can be visualized with this graph:

Source: stackoverflow.com

</details>

2. What the heck does it mean if an operation is O(log n)?

<details>

<summary><strong>Show Answer</strong></summary>

O(log n) means for every element, you're doing something that only needs to look at log N of the elements. This is usually because you know something about the elements that let you make an efficient choice (for example to reduce a search space). The most common attributes of logarithmic running-time function are that:

the choice of the next element on which to perform some action is one of several possibilities, and only one will need to be chosen or the elements on which the action is performed are digits of n.

Most efficient sorts are an example of this, such as merge sort. ​It is O(log n) when we do divide and conquer type of algorithms e.g binary search. Another example is quick sort where each time we divide the array into two parts and each time it takes O(N) time to find a pivot element. Hence it N O(log N)

Plotting log(n) on a plain piece of paper, will result in a graph where the rise of the curve decelerates as n increases:

Source: stackoverflow.com   

</details>

3. What exactly would an O(n2) operation do?

<details>

<summary><strong>Show Answer</strong></summary>

O(n2) means for every element, you're doing something with every other element, such as comparing them. Bubble sort is an example of this.

Source: stackoverflow.com   

</details>

4. When talking about Big O, what do we mean by worst case for an algorithm?

<details>

<summary><strong>Show Answer</strong></summary>

Big-O is often used to make statements about functions that measure the worst case behavior of an algorithm. Worst case analysis gives the maximum number of basic operations that have to be performed during execution of the algorithm. It assumes that the input is in the worst possible state and maximum work has to be done to put things right.

Source: stackoverflow.com   

</details>

5. Why do we use Big O notation to compare algorithms?

<details>

<summary><strong>Show Answer</strong></summary>

The fact is it's difficult to determine the exact runtime of an algorithm. It depends on the speed of the computer processor. So instead of talking about the runtime directly, we use Big O Notation to talk about how quickly the runtime grows depending on input size.

With Big O Notation, we use the size of the input, which we call n. So we can say things like the runtime grows “on the order of the size of the input” (O(n)) or “on the order of the square of the size of the input” (O(n2)). Our algorithm may have steps that seem expensive when n is small but are eclipsed eventually by other steps as n gets larger. For Big O Notation analysis, we care more about the stuff that grows fastest as the input grows, because everything else is quickly eclipsed as n gets very large.

</details> 


6. Explain the difference between O(1) vs O(n) space complexities

<details>

<summary><strong>Show Answer</strong></summary>

Let's consider a traversal algorithm for traversing a list.

O(1) denotes constant space use: the algorithm allocates the same number of pointers irrespective to the list size. That will happen if we move (reuse) our pointer along the list.
In contrast, O(n) denotes linear space use: the algorithm space use grows together with respect to the input size n. That will happen if let's say for some reason the algorithm needs to allocate 'N' pointers (or other variables) when traversing a list.
Source: stackoverflow.com   


</details>

7. Provide an example of O(1) algorithm

<details>

<summary><strong>Show Answer</strong></summary>

Say we have an array of n elements:

int array[n];
If we wanted to access the first (or any) element of the array this would be O(1) since it doesn't matter how big the array is, it always takes the same constant time to get the first item:

x = array[0];
Source: stackoverflow.com   

</details>

8. What is the time complexity of this code snippet?

```javascript
for (int i = 0; i < n; i++){
    if(array[i] == numToFind){ 
        return i; 
    }
}
```

<details>

<summary><strong>Show Answer</strong></summary>

This would be O(n) since at most we would have to look through the entire list to find our number. The Big-O is still O(n) even though we might find our number the first try and run through the loop once because Big-O describes the upper bound for an algorithm.

Source: stackoverflow.com   

</details>

9. Consider the following function: `f(x) = log n + 3n`. What is the big O notation of this function?

<details>

<summary><strong>Show Answer</strong></summary>

It is simply O(n).

When you have a composite of multiple parts in Big O notation which are added, you have to choose the biggest one. In this case it is O(3n), but there is no need to include constants inside parentheses, so we are left with O(n).

Source: stackoverflow.com   

</details>

10. What is complexity of push and pop for a Stack implemented using a LinkedList?

<details>

<summary><strong>Show Answer</strong></summary>

O(1). Note, you don't have to insert at the end of the list. If you insert at the front of a (singly-linked) list, they are both O(1).

Stack contains 1,2,3:

[1]->[2]->[3]
Push 5:

[5]->[1]->[2]->[3]
Pop:

[1]->[2]->[3] // returning 5
Source: stackoverflow.com   

</details>