# Gaussian Elimination

- Gauss elimination is a method for solving systems of linear equations by repeatedly eliminating variables until a single variable remains, which can then be solved.
- This is a Python implementation of the Gaussian Elimination algorithm for solving systems of linear equations.

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Problem Statement 1](#problem_statement_1)
- [Problem Statement 2](#problem_statement_2)
- [Solution](#solution)
- [Usage](#usage)
- [Contributing](#contributing)

## Introduction

Gaussian Elimination is a fundamental numerical method used for solving systems of linear equations. This project provides a Python implementation of this algorithm to help you solve linear systems efficiently.

## Features

- Solving Linear Systems
- Easy-to-use Python library.
- Well-documented code for understanding and customization.

* Solving Linear Systems
  - This code repository includes a function/code (part (a)) that can be used to solve linear systems of the form A x<sup>&rarr;</sup>  = b<sup>&rarr;</sup>, where A = (aij) and b<sup>&rarr;</sup> = (bj). In the context of this problem, A is a tridiagonal matrix with specific values, and b<sup>&rarr;</sup> is a vector with specific components.

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.x installed on your system.

## Installation

You can install this package using `pip`:

```
pip install numpy
pip install pandas
```

## Problem_Statement_1
### Gauss elimination using partial pivoting

Solve the following linear system using the provided function/code:
```
Define your coefficient matrix 'A' and the right-hand side vector 'b'
A = [
    [2, -1, 1],
    [1, 2, -1],
    [3, 2, 3]
]

b = [8, 7, 15]

#Use the Gaussian Elimination function to solve the system
solution = gauss_elimination(A, b)

#Find the solution for x.
```

## Problem_Statement_2
### Gauss elimination using partial pivoting

Solve the following linear system using the provided function/code:
'
A x<sup>&rarr;</sup> = b<sup>&rarr;</sup>

Where:
- A is a 100x100 matrix with a special structure:
  - aij = bj = 0, except when 1 ≤ i, j ≤ 100, aij and bj will be set as follows:
    - aij = 5 if i = j
    - aij = aj,j−1 = aj,j+1 = 1 if i = j ± 1
  - All other elements aij and bj are set to 0.
- b is a 100-dimensional vector with bj = 1 for j = 50, and bj = 0 for all other values of j.
'


## Solution

The solution vector x<sup>&rarr;</sup> = (xj) will be computed using the provided function/code. This solution vector will be plotted as a function of j to visualize the results.

You can run the code to solve this linear system and generate the plot of the solution vector x<sup>&rarr;</sup>.
![Figure_1](https://github.com/nikhil9066/Gauss-Elimination/assets/36182930/cc991b2f-90fd-4625-8cf0-839b10b40898)

## Usage
 Just run the code it's all built-in.

## Contributing
Contributions are welcome! If you'd like to contribute to this project, please follow these steps:

- Fork the repository.
- Create a new branch with a descriptive name.
- Make your changes.
- Test your changes.
- Create a pull request, explaining your changes.
