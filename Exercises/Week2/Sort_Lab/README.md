# Sorting Lab

[![Run on Repl.it](https://repl.it/badge/github/upperlinecode/<INSERT_GITHUB_EXTENSION>)](https://repl.it/github/upperlinecode/<INSERT_GITHUB_EXTENSION>)

## Contents

- [Intro](#intro)
- [The Lab](#the-lab)
- [Hints & Resources](#resources)

## Intro

If you haven't already, take a couple of minutes to familiarize yourself with the ["Sort the Cards" app](https://sortinggame.emmanuelrodri23.repl.co/). Notice how as you attempt to sort the cards in order from least to greatest, the 'observations', 'cycles', and 'moves' counters go up. Also, notice how they all have a price. Sorting items can be costly in different ways which means the algorithm we use to sort them will vary based on the demands.

In the lab, you will be asked to code up your algorithms and make new plans for different demands. 

## The Lab

> Note: There are many built in sorting algorithms that exist in many programming languages. While these are tools you can (and should!) use when programming, you should **NOT** use them for today's lab. 

### Sorting Algorithms

Two sets of sample data have been provided in the `sample_data.py` file. Write all your code in the `sort_lab.py` file.

If you don't remember a particular sorting algorithm, explore the documentation on [Sorting and Searching Algorithms](https://www.programiz.com/dsa/bubble-sort)

1. Create an algorithm that does an insertion sort of the sample `numbers` list from smallest to largest.
2. Create an algorithm that does an bubble sort of the sample `numbers` list from smallest to largest.
3. Create an algorithm that does a selection sort of the sample `numbers` list from smallest to largest
4. Pause and discuss. Which algorithm is the most "efficient"? Explain your answer considering how each handles:
    - Number of observations
    - Number of iterations/cycles
    - Number of movements of items
5. **Spicy**: Update your three algorithms to sort values in `numbers` from largest to smallest.
6. **Spicier**: Update your three algorithms to sort the list of `student` dictionaries by a provided key (name, age, or occupation).
    ```python
    sort(sample_data.students, "occupation") 
    # returns list sorted based on their occupation
    ```
7. Create a merge sort algorithm to sort the list of `numbers`.
8. Create a merge sort algorithm to sort the list of student dictionaries by a provided key (name, age, or occupation).

## Resources

- **Programiz**: [Sorting and Searching Algorithms](https://www.programiz.com/dsa/bubble-sort)