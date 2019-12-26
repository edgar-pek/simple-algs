[solution adoppted from Hacker's Delight, 11-1 Integer Square Root]

The method of computation is based on two bounds, the lower bound lo <= floor(sqrt(x)) + 1 and the upper bound 
hu >= floor(sqrt(x)), where x is the input number.
The computation maintains the lower and upper bound as a loop invariant in a variant of binary search where midpoint is
computed based on lo and h1 (see above). If the square of the midpoint is less than the argument x then the lower bound is 
updated to be close to midpoint value, otherwise the upper bound is updated to be close to the midpoint value. The loop 
terminates when lo == hi + 1
Time efficiency of solution: O(log n), space efficiency O(1)
