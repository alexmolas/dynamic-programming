# Matrix Multiplication Optimization

In this project I will explore the different optimization 
techniques that exist when chosing the order in which
matrix multiplication is performed.

## Introduction:

Since matrix multiplication is associative the order 
in which the multiplications is performed does not 
affect the final result. In other words, no matter 
how the product is parenthesized, the result obtained 
will remain the same.

For example, for four matrics `A`, `B`, `C` and `D` we have:

```
ABCD = ((AB)C)D = A((BC)D) = (AB)(CD) = ...
```

However, the number of operations to perform is not the same in all the cases!

In this project I will investigate different techniques to decide which
is the multiplication order that minimizes de number
of operations to perform.