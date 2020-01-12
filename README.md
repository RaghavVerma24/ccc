# CCC

<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->

**Table of Contents** _generated with [DocToc](https://github.com/thlorenz/doctoc)_

-   [CCC](#ccc)
    -   [Time left: 31 Days](#time-left-31-days)
    -   [Competition date: Febuary 12](#competition-date-febuary-12)
    -   [Roadmap](#roadmap)
        -   [Week 1](#week-1)
        -   [Week 2](#week-2)
        -   [Week 3 and 4](#week-3-and-4)
        -   [Week 5](#week-5)
    -   [Todo](#todo)
    -   [Websites](#websites)
    -   [CCC information](#ccc-information)
        -   [Past competitions](#past-competitions)
        -   [Solutions](#solutions)
    -   [Problems](#problems)
        -   [Towers of hanoi](#towers-of-hanoi)
    -   [Topics](#topics)
        -   [Asymptotic notation](#asymptotic-notation)
        -   [Data structures](#data-structures)
            -   [Linked lists](#linked-lists)
            -   [Graphs](#graphs)
        -   [Algorithms](#algorithms)
            -   [Binary search](#binary-search)
            -   [Selection sort](#selection-sort)
            -   [Insertion sort](#insertion-sort)
            -   [Mergesort](#mergesort)
            -   [Quicksort](#quicksort)
            -   [Breadth-first search](#breadth-first-search)
            -   [Depth-first search](#depth-first-search)
    -   [Dynamic programming](#dynamic-programming)
        -   [Memoization](#memoization)
    -   [Cheatsheets](#cheatsheets)
    -   [Resources](#resources)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

## Time left: 31 Days

## Competition date: Febuary 12

## Roadmap

### Week 1

-   Find resources
-   Learn what needs to be learned
-   make notes

### Week 2

-   Do leetcode and hackerrank problems

### Week 3 and 4

-   Do problems for the last 5+ years

### Week 5

-   Prep for contest

## Todo

## Websites

-   leetcode.com
-   hackerrank.com

## CCC information

-   https://www.cemc.uwaterloo.ca/contests/computing.html
-   https://cemc.uwaterloo.ca/contests/computing/details.html
-   http://compsci.ca/blog/getting-ready-for-the-canadian-computing-competition/
-   https://www.cemc.uwaterloo.ca/contests/computing/examples.html

### Past competitions

-   https://www.cemc.uwaterloo.ca/contests/past_contests.html

### Solutions

-   https://github.com/topics/canadian-computing-competition
-   https://dmoj.ca/

## Problems

### Towers of hanoi

-   https://www.geeksforgeeks.org/c-program-for-tower-of-hanoi/
-   https://www.khanacademy.org/computing/computer-science/algorithms/towers-of-hanoi/a/towers-of-hanoi

## Topics

### Asymptotic notation

-   https://www.khanacademy.org/computing/computer-science/algorithms#asymptotic-notation
-   https://learnxinyminutes.com/docs/asymptotic-notation/
-   https://www.bigocheatsheet.com/
-   http://web.mit.edu/16.070/www/lecture/big_o.pdf
-   https://stackoverflow.com/questions/2307283/what-does-olog-n-mean-exactly

### Data structures

#### Linked lists

-   https://www.geeksforgeeks.org/data-structures/linked-list/

#### Graphs

-   https://www.khanacademy.org/computing/computer-science/algorithms/graph-representation/a/describing-graphs
-   http://web.cecs.pdx.edu/~sheard/course/Cs163/Doc/Graphs.html
-   https://www.geeksforgeeks.org/graph-data-structure-and-algorithms/
-   https://softwareengineering.stackexchange.com/questions/168058/what-are-graphs-in-laymens-terms
-   https://hackernoon.com/graphs-in-cs-and-its-traversal-algorithms-cfee5533f74e

### Algorithms

#### Binary search

-   https://www.khanacademy.org/computing/computer-science/algorithms/binary-search/a/binary-search

1. Let min = 1 max = n.
2. Guess the average of max and min, rounded down so that it is an integer.
3. If you guessed the number, stop. You found it!
4. If the guess was too low, set min to be one larger than the guess.
5. If the guess was too high, set max to be one smaller than the guess.
6. Go back to step two.

#### Selection sort

-   https://www.khanacademy.org/computing/computer-science/algorithms/sorting-algorithms/a/selection-sort-pseudocode

1. Find the smallest card. Swap it with the first card.
2. Find the second-smallest card. Swap it with the second card.
3. Find the third-smallest card. Swap it with the third card.
4. Repeat finding the next-smallest card, and swapping it into the correct position until the array is sorted.

#### Insertion sort

-   https://www.khanacademy.org/computing/computer-science/algorithms/insertion-sort/a/insertion-sort-pseudocode

1. Call insert to insert the element that starts at index 1 into the sorted subarray in index 0.
2. Call insert to insert the element that starts at index 2 into the sorted subarray in indices 0 through 1.
3. Call insert to insert the element that starts at index 3 into the sorted subarray in indices 0 through 2.
4. …
5. Finally, call insert to insert the element that starts at index n-1n−1n, minus, 1 into the sorted subarray in indices 0 through n-2n−2n, minus, 2.

#### Mergesort

-   https://www.khanacademy.org/computing/computer-science/algorithms/merge-sort/a/divide-and-conquer-algorithms

1. Divide by finding the number qqq of the position midway between ppp and rrr. Do this step the same way we found the midpoint in binary search: add ppp and rrr, divide by 2, and round down.
2. Conquer by recursively sorting the subarrays in each of the two subproblems created by the divide step. That is, recursively sort the subarray array[p..q] and recursively sort the subarray array[q+1..r].
3. Combine by merging the two sorted subarrays back into the single sorted subarray array[p..r].

#### Quicksort

-   https://www.khanacademy.org/computing/computer-science/algorithms/quick-sort/a/overview-of-quicksort

#### Breadth-first search

-   https://www.khanacademy.org/computing/computer-science/algorithms/breadth-first-search/a/breadth-first-search-and-its-uses

#### Depth-first search

## Dynamic programming

-   https://blog.usejournal.com/top-50-dynamic-programming-practice-problems-4208fed71aa3
-   https://www.geeksforgeeks.org/dynamic-programming/
-   https://learnxinyminutes.com/docs/dynamic-programming/

### Memoization

-   https://www.khanacademy.org/computing/computer-science/algorithms/recursive-algorithms/a/improving-efficiency-of-recursive-functions
-   https://www.geeksforgeeks.org/memoization-1d-2d-and-3d/

## Cheatsheets

-   https://github.com/aspittel/coding-cheat-sheets
-   https://github.com/TSiege/Tech-Interview-Cheat-Sheet

## Resources

-   https://www.khanacademy.org/computing/computer-science/algorithms/algorithms-more-learning/a/where-to-go-from-here
-   https://docs.python.org/3/
-   https://github.com/yangshun/tech-interview-handbook
-   https://github.com/aspittel/coding-cheat-sheets
-   https://github.com/TheAlgorithms/Python
-   https://github.com/enkidevs/curriculum
-   https://github.com/turingschool/data_structures_and_algorithms
-   https://github.com/tayllan/awesome-algorithms
-   https://github.com/ossu/computer-science
-   https://teachyourselfcs.com/
-   https://spin.atomicobject.com/2015/05/15/obtaining-thorough-cs-background-online/
