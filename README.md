# Simple Calculator + 2x2 Matrix Calculator (Built by Anubhav Jha as part of the Python Essentials evaluated course project.)

A simple command-line calculator application built in Python that performs basic arithmetic operations and 2x2 matrix operations. This project demonstrates fundamental Python programming concepts such as functions, loops, conditionals, lists, user input, and mathematical operations.

## Overview

The program provides a menu-driven interface where the user can choose between basic arithmetic operations and 2x2 matrix operations.

For basic calculations, the program supports **Addition, Subtraction, Multiplication, and Division**.

For matrices, the program supports **2x2 Matrix Addition, 2x2 Matrix Subtraction, and 2x2 Matrix Multiplication**.

The program continues running until the user selects the Exit option.

## Features

* Menu-driven command-line interface
* Addition of two numbers
* Subtraction of two numbers
* Multiplication of two numbers
* Division of two numbers
* Division-by-zero error handling
* 2x2 matrix addition
* 2x2 matrix subtraction
* 2x2 matrix multiplication
* Uses loops to process matrix elements
* Displays matrix results in a readable format
* Handles invalid menu choices
* Allows the user to perform multiple calculations in one run

## Technologies / Tools Used

* **Language:** Python 3
* **Concepts used:** Functions, `input()`, `print()`, conditionals (`if`/`elif`/`else`), `while` loops, `for` loops, nested loops, lists, variables, type casting using `float()`, and return values
* **Environment:** Runs from any terminal with Python 3 installed
* **Version Control:** Git & GitHub

## Project Structure

```text
calculator-project/
│
├── main.py       # Complete calculator program (entry point)
├── README.md           # Project documentation (this file)
└── screenshots/        # Screenshots of the program running
```

## How to Install & Run

### Prerequisites

* Python 3.7 or above installed on your system
* A terminal or command prompt
* Git installed if you want to clone the repository

You can check your Python installation using:

```bash
python --version
```

or:

```bash
python3 --version
```

### Steps

1. **Clone the repository**

```bash
git clone https://github.com/{your-username}/{your-repo-name}
cd {your-repo-name}
```

2. **Run the program**

```bash
python calculator.py
```

On some systems, use:

```bash
python3 calculator.py
```

3. **Follow the on-screen prompts**

The program displays the following menu:

```text
=== Simple Calculator + 2x2 Matrix Calculator ===
Options:
1. Add two numbers
2. Subtract two numbers
3. Multiply two numbers
4. Divide two numbers
5. 2x2 Matrix Addition
6. 2x2 Matrix Subtraction
7. 2x2 Matrix Multiplication
8. Exit
```

Enter a number from `1` to `8` to select an operation.

No external Python libraries or packages are required. The project uses only Python's built-in functionality.

## Instructions for Testing

To manually test the program:

1. Run:

```bash
python calculator.py
```

2. Test each of the basic arithmetic operations:

   * Select `1` and test addition.
   * Select `2` and test subtraction.
   * Select `3` and test multiplication.
   * Select `4` and test division.

3. Test division by zero:

   * Select option `4`.
   * Enter any number as the first number.
   * Enter `0` as the second number.
   * The program should display:

```text
Error: cannot divide by zero
```

4. Test matrix addition:

   * Select option `5`.
   * Enter two 2x2 matrices.
   * Confirm that corresponding elements are added correctly.

5. Test matrix subtraction:

   * Select option `6`.
   * Enter two 2x2 matrices.
   * Confirm that corresponding elements are subtracted correctly.

6. Test matrix multiplication:

   * Select option `7`.
   * Enter two 2x2 matrices.
   * Confirm that the multiplication result is calculated correctly.

7. Test invalid input:

   * Enter a menu option outside `1-8`.
   * The program should display:

```text
Invalid choice. Enter 1-8.
```

8. Test the exit option:

   * Select option `8`.
   * The program should display:

```text
Bye!
```

and terminate.

## Example

### Basic Addition

```text
Choose (1-8): 1
First number: 25
Second number: 15
Result: 40.0
```

### 2x2 Matrix Addition

For example, if the user enters:

```text
A = [1  2]
    [3  4]

B = [5  6]
    [7  8]
```

The program displays:

```text
Result Matrix (A + B):
   6.000    8.000
  10.000   12.000
```

### 2x2 Matrix Multiplication

For:

```text
A = [1  2]
    [3  4]

B = [5  6]
    [7  8]
```

The program displays:

```text
Result Matrix (A * B):
  19.000   22.000
  43.000   50.000
```

## Mathematical Operations

### Addition

The program adds two numbers using the `add()` function:

```text
a + b
```

### Subtraction

The program subtracts the second number from the first:

```text
a - b
```

### Multiplication

The program multiplies two numbers:

```text
a * b
```

### Division

The program divides the first number by the second. Division by zero is checked before performing the calculation.

### Matrix Addition

Each corresponding element of matrices A and B is added:

```text
R[i][j] = A[i][j] + B[i][j]
```

### Matrix Subtraction

Each corresponding element of matrix B is subtracted from matrix A:

```text
R[i][j] = A[i][j] - B[i][j]
```

### Matrix Multiplication

Matrix multiplication uses nested loops to calculate each element of the resulting matrix:

```text
R[i][j] = A[i][0] * B[0][j] + A[i][1] * B[1][j]
```

## Error Handling

The program handles division by zero by checking whether the second number is zero before performing division.

If the user attempts to divide by zero, the program displays:

```text
Error: cannot divide by zero
```

The program also handles invalid menu selections by displaying:

```text
Invalid choice. Enter 1-8.
```

## Limitations

* Matrix operations are limited to 2x2 matrices.
* The program is command-line based and does not have a graphical user interface.
* Calculation history is not saved.
* The program expects numeric input when numbers or matrix elements are requested.
* No external mathematical libraries are used.

## Future Improvements

Possible improvements for future versions include:

* Support for matrices of different dimensions
* Additional mathematical operations
* Calculation history
* Better validation for non-numeric input
* Support for more matrix operations such as transpose and determinant
* Graphical user interface
* Saving calculation results to a file

## Author

Built as a Python CLI project to demonstrate fundamental Python programming concepts, arithmetic calculations, and 2x2 matrix operations.
