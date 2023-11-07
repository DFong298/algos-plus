# Strassen's Matrix Multiplication
*In order to keep things simple, we will mostly be working with square matrices with dimension $n = 2^m$. Methods to deal with matrices not of this form will be elaborated on later.*

## Matrix Multiplication and Complexity
Suppose we are given two matrices $A$ and $B$, and we want to multiply them. By definition, the product of the two matrices M is given by:

$$M_{ij} = \sum_{k=1}^{n} A_{ik}B_{kj}$$

When both $A$ and $B$ are $n \times n$, $M$ will also be $n \times n$. With $n^2$ entries in M, and each entry requiring $n$ additions and multiplications, the total number of required operations is $O(n^3)$. This naive approach is very general, and works for all matrices who's dimensions are compatible for multiplication. However, for the special case where both matrices are square, with dimensions that are powers of $2$, we can reduce the number of required operations from $O(n^3)$ down to $O(n^{2.8074})$.

## The Algorithm
