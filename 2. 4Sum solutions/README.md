# 4Sum Solutions

In this part I implement three kinds of solution, and use [leetcode](https://leetcode.com/problems/4sum/) as an assessment platform to ensure correctness and efficiency.

## Solution1 - DFS
This was the concept performed during interview, a brute force way to enumerate all the combinations.

The complexity is `combination(n, 4)`, approximately `n^4`, in which `n` is the length of `nums`.

## Solution2 - 3Sum based
After Solution1, I started to realize that it may be divided and conquered, then came up with the following thoughts.
```
for i in range(len(nums) - 3):
    3Sum(...)
```
Since under a loop, number of digits need to be found is 3, exactly the same as 3Sum.
The complexity of 3Sum is `n^2` in my solution, so the entire complexity is `n^3`.

In leetcode assessment, it can faster than approximately 25% submissions.

## Solution3 - 2Sum based
This solution is almost the same as previous one, just add another nested loop.
```
for i in range(len(nums) - 3):
    for j in range(len(nums) - 2):
        2Sum(...)
```
The complexity of 2Sum is `n`, so the entire complexity is `n^3`, same as previous, but I tried to add some improvements to make it a little faster, [#62](https://github.com/tp6vup54/questions-in-interview/blob/master/2.%204Sum%20solutions/Solution.py#L62), [#65](https://github.com/tp6vup54/questions-in-interview/blob/master/2.%204Sum%20solutions/Solution.py#L65), [#68](https://github.com/tp6vup54/questions-in-interview/blob/master/2.%204Sum%20solutions/Solution.py#L68) and [#70](https://github.com/tp6vup54/questions-in-interview/blob/master/2.%204Sum%20solutions/Solution.py#L70), they help to ignore some unnecessary iterations.

These little improvements make it faster than approximately 50% submissions.
