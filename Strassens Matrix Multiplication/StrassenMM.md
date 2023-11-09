# Strassen's Matrix Multiplication
*In order to keep things simple, we will mostly be working with square matrices with dimension $n = 2^m$. Methods to deal with matrices not of this form will be elaborated on later.*

## Matrix Multiplication and Complexity
Suppose we are given two matrices $A$ and $B$, and we want to multiply them. By definition, the product of the two matrices M is given by:

$$M_{ij} = \sum_{k=1}^{n} A_{ik}B_{kj}$$

When both $A$ and $B$ are $n \times n$, $M$ will also be $n \times n$. With $n^2$ entries in M, and each entry requiring $n$ additions and multiplications, the total number of required operations is $O(n^3)$. This naive approach is very general, and works for all matrices who's dimensions are compatible for multiplication. However, for the special case where both matrices are square, with dimensions that are powers of $2$, we can reduce the number of required operations from $O(n^3)$ down to $O(n^{2.8074})$.

## Basis of The Algorithm
Given two matrices $A$ and $B$ that are $n \times n$ where $n = 2^m$ for some $m$, both $A$ and $B$ can be decomposed into four sub-matrices:

```math
A = 
\begin{bmatrix}
a_{11} & a_{12} & a_{13} & a_{14} \\[0.3em]
a_{21} & a_{22} & a_{23} & a_{24} \\[0.3em]
a_{31} & a_{42} & a_{33} & a_{34} \\[0.3em]
a_{41} & a_{42} & a_{43} & a_{44} \\[0.3em]
\end{bmatrix} 

\longrightarrow

A_{11} = 
\begin{bmatrix}
a_{11} & a_{12}\\[0.3em]
a_{21} & a_{22}
\end{bmatrix}

A_{12} = 
\begin{bmatrix}
a_{13} & a_{14}\\[0.3em]
a_{23} & a_{24}
\end{bmatrix}

A_{21} = 
\begin{bmatrix}
a_{31} & a_{32}\\[0.3em]
a_{41} & a_{42}
\end{bmatrix}

A_{22} = 
\begin{bmatrix}
a_{33} & a_{34}\\[0.3em]
a_{43} & a_{44}
\end{bmatrix}
```

$$
B = 
\begin{bmatrix}
b_{11} & b_{12} & b_{13} & b_{14}\\[0.3em]
b_{11} & b_{12} & b_{13} & b_{14}\\[0.3em]
b_{11} & b_{12} & b_{13} & b_{14}\\[0.3em]
b_{11} & b_{12} & b_{13} & b_{14}\\[0.3em]
\end{bmatrix}

\longrightarrow

B_{11} = 
\begin{bmatrix}
b_{11} & b_{12}\\[0.3em]
b_{21} & b_{22}
\end{bmatrix}

B_{12} = 
\begin{bmatrix}
b_{13} & b_{14}\\[0.3em]
b_{23} & b_{24}
\end{bmatrix}

B_{21} = 
\begin{bmatrix}
b_{31} & b_{32}\\[0.3em]
b_{41} & b_{42}
\end{bmatrix}

B_{22} = 
\begin{bmatrix}
b_{33} & b_{34}\\[0.3em]
b_{43} & b_{44}
\end{bmatrix}
$$

Multiplying the two matrices $M = AB$, we can construct each sub-matrix of $M$ by multplying sub-matrices of $A$ and $B$, treating the sub-matrices as its own element in the matrix. The following is a visual aid from Inside Code's video to help conceptualize this idea.

![An example of this method of matrix multiplication](/Strassens%20Matrix%20Multiplication/matrix_quadrants_example.png)

In our case, we can compute the matrix $M$ as follows:

$$
M_{11} = A_{11}B_{11} + A_{12}B_{21}\\
M_{12} = A_{11}B_{12} + A_{12}B_{22}\\
M_{21} = A_{21}B_{11} + A_{22}B_{21}\\
M_{22} = A_{21}B_{12} + A_{22}B_{22}
$$

By now, a recursive nature to this problem is exposed. Any quadrant of $M$ is computed by finding the sum of two matrices, which themselves can be computed this way. As we can see, to compute the product of a matrix, we are required to compute 8 new matrices at each recursive step. To find computation complexity of this algorithm, we use the Master Theorem. 

The Master Theorem states that given a recurrence of the form $T(n) = aT(\frac{n}{b})+ f(n)$ for $a \geq 1$ and $b > 1$, the following statements are true:

Case 1: If $f(n) = O(n^{\log_ba-\epsilon})$ for some $\epsilon > 0$, then $T(n) = \Theta(n^{\log_ba})$.\
Case 2: If $f(n) = \Theta(n^{\log_ba})$, then $T(n) = \Theta(n^{\log_ba}\log n)$.\
Case 3: If $f(n) = \Omega(n^{\log_ba+\epsilon})$ for some $\epsilon > 0$ and $af(n/b)\leq cf(n)$ then $T(n) = \Theta(f(n))$.

*If you have never heard of or learned the Master Theorem, it is a nifty tool that to compute the complexity of recursive algorithms. Try it with common recursive algorithms such as merge sort to convince yourself the Master Theorem holds.*

In our case, $a=8$, $b=2$, and $f(n)=\Theta(n^2)$, giving us case 1. Thus, this recursive computation of $M=AB$ is tightly bounded by $n^{\log_2 8} = n^3$, and thus is $\Theta(n^3)$, which is not really an improvement to the naive method we started with.

## Strassen's Algorithm
Instead of computing 8 matrix multiplications, Strassen's Algorithm defines 7 matrices that we compute with matrix multiplication:

$$
C_1 = (A_{11}+A_{12})(B_{11}+B_{22})\\
C_2 = (A_{21}+A_{22})B_{11}\\
C_3 = A_{11}(B_{12}-B_{22})\\
C_4 = A_{22}(B_{21}-B_{11})\\
C_5 = (A_{11}+A_{12})B_{22}\\
C_6 = (A_{21}-A_{11})(B_{11}+B_{12})\\
C_7 = (A_{12}-A_{22})(B_{21}+B_{22})
$$

Then, to compute each quadrant of our solution $M$:

$$
M_{11} = C_1 + C_4 - C_5 + C_7\\
M_{12} = C_3 + C_5\\
M_{21} = C_2 + C_4\\
M_{22} = C_1 - C_2 + C_3 + C_6
$$

We do this recursively everytime we compute the multiplication for any $C_i$. This lets us do 7 multiplications instead of the 8 we described in the previous method. Using the Master Theorem again with $a=7, b=2$ and $f(n)=\Theta(n^2)$, we have case 1 again. The runtime is thus tightly bounded by $n^{\log_27} \approx n^{2.8074}$, meaning the algorithm is $\Theta(n^{2.8074})$. This is an improvement compared to the naive $\Theta(n^3)$ algorithm. Does this mean that Strassen's Algorithm is better?

## Caveats of Strassen's Algorithm
Although we derived the algorithm to have better time complexity, this algorithm is only better than the naive approach when the dimensions of the matrix exceed 10,000+. The computation of the time complexity neglects the amount of addition that is done when computing each of the 7 matrices, and in practice, the algorithm performs slower than the naive method on smaller matrices. Typically, the implementation of this algorithm would revert back to the brute force method when the sub-matrices are small enough where Strassen's algorithm becomes slower than the brute force method.

Furthermore, this algorithm only works on square matrices that are $n \times n$, and $n$ is a power of $2$. There are ways to apply this algorithm on matrices that don't follow this pattern such as adding padding to the matrix to make its dimensions a power of $2$. However, these methods of forcing a matrix to work with this algorithm incurs extra computational cost.
