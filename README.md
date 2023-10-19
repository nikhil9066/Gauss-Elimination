# gaussElimination
Gauss elimination is a method for solving systems of linear equations by repeatedly eliminating variables until a single variable remains, which can then be solved for.

## Solving Linear Systems

This code repository includes a function/code (part (a)) that can be used to solve linear systems of the form A⃗x = ⃗b, where A = (aij) and ⃗b = (bj). In the context of this problem, A is a tridiagonal matrix with specific values, and ⃗b is a vector with specific components.

### Problem Statement

Solve the following linear system using the provided function/code:

A⃗x = ⃗b

Where:
- A is a 100x100 matrix with a special structure:
  - aij = bj = 0, except when 1 ≤ i, j ≤ 100, aij and bj will be set as follows:
    - aij = 5 if i = j
    - aij = aj,j−1 = aj,j+1 = 1 if i = j ± 1
  - All other elements aij and bj are set to 0.
- ⃗b is a 100-dimensional vector with bj = 1 for j = 50, and bj = 0 for all other values of j.

### Solution

The solution vector ⃗x = (xj) will be computed using the provided function/code. This solution vector will be plotted as a function of j to visualize the results.

You can run the code to solve this linear system and generate the plot of the solution vector ⃗x.

## Usage

Please refer to the documentation or code files for instructions on how to use the provided function/code to solve the linear system and generate the plot.

