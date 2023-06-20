# TITLE

[![Run on Repl.it](https://repl.it/badge/github/upperlinecode/<INSERT_GITHUB_EXTENSION>)](https://repl.it/github/upperlinecode/<INSERT_GITHUB_EXTENSION>)

## Contents

- [Intro](#intro)
- [The Lab](#the-lab)
- [Hints & Resources](#hints--resources)
- [Extensions](#extensions)

## Intro

If you haven't already, take a couple of minutes to familiarize yourself with the ["Sort the Cards" app](https://sortinggame.emmanuelrodri23.repl.co/). Notice how as you attempt to sort the cards in order from least to greatest, the 'observations', 'cycles', and 'moves' counters go up. Also, notice how they all have a price. Sorting items can be costly in different ways which means the algorithm we use to sort them will vary based on the demands.

In the lab, you will be asked to code up your algorithms and make new plans for different demands. 

## The Lab

> Note: First, we'll be demoing Selection Sort, and how to turn the idea into code. Then, we will guide students in doing the same for Insertion sort and one of the algorithms they made in the lesson (if applicable). 

**Coding Selection Sort**
1. Explain selection sort to students. The idea behind Selection Sort is to look for the smallest number and place it in the first slot. Then, look for the next smallest and put it in the second slot, and so on until the list is sorted. 
2. Have students try this method for about a minute in the "Sort the Cards" app before showing them the code.
    ```py
    sample_list = [5, 2, 1, 3, 4]
    sorted_list = []

    for i in range(len(sample_list)):
        smallest = sample_list[0]
        for element in sample_list:
            if element < smallest:
                smallest = element
        sorted_list.append(sample_list.pop(smallest))
    ```
    _NOTE: we know this is not the most efficient "in-place" way of selection sorting, but it is easy to read, and used as an example of mind to code._
3. Have students turn and talk to their partner explaining to each other what is happening here step by step. 
4. Now, explain Insertion Sort using the "Sort the Cards" app; The idea behind Insertion Sort is that you look at the next element in the list, pluck it out, and shift the previous elements that are greater than the plucked out element. Then, insert the element back into the list at the right spot.

5. Fork; At this point, consider forking the class.
    - With the students that feel ready, they can start the extensions -- the first being to code Insertion Sort. 
    - For those that would like extra assistance, you can go back and explain Selection Sort more in depth and/or guide them through the first few steps of Insertion Sort. 
    
    If you feel your class overall will need extra support after coding Insertion sort, consider having students return after attempting Insertion Sort for a show and tell.

```py
# One way to code Insertion Sort
sample_list = [5, 2, 1, 3, 4]

for i in range(1, len(sample_list)):
    this_value = sample_list[i]

    pointer = i-1
    while pointer >= 0 and sample_list[pointer] > this_value:
        sample_list[pointer+1] = sample_list[pointer]
        pointer -= 1

    sample_list[pointer+1] = this_value
```

## Hints & Resources

- **Programiz**: [Sorting and Searching Algorithms](https://www.programiz.com/dsa/bubble-sort)

## Extensions

**Mild**
- Discuss the steps for implementing Insertion Sort with your partner. Use the "Sort the Cards" app if you need to visualize. Then, code Insertion Sort. _HINT: print your list at each iteration to make sure it is sorting as expected_
- Using the `students` dictionary in the `sample_data.py`, create a function that can sort it by age.