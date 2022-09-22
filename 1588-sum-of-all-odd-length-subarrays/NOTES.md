in example 1, len(arr) = 5, elements are counted 3,4,5,4,3 times respectively
in example 2, len(arr) = 2, each element is counted 1 time
​
is there an algebraic approach?
​
​
own examples:
​
arr = [1, 2, 3, 4]
sub arrays:
1
2
3
4
1 2 3
2 3 4
for len 4, each elements are counted 2, 3, 3, 2 times respectively
result =
​
arr = [1, 2, 3, 4, 5, 6]
sub arrays:
1
2
3
4
5
6
1 2 3
2 3 4
3 4 5
4 5 6
1 2 3 4 5
2 3 4 5 6
for len 6, elements are counted 3, 5, 6, 6, 5, 3 times respectively