# Python Programming Notes

## 1. Hello World Program
The initial program to write is always the 'Hello World.' A successful execution of this program, displaying 'Hello World' in the standard output, ensures that all the required environmental settings are in place.

```python
print("Hello, World!")
```

## 2. Standard Output (stdout)
stdout stands for Standard Output. It is represented by the stdout stream, which is frequently attached to the console or terminal. It makes it possible for programs to show the user information or results.

## 3. Python Built-In Function print()
The print() function in Python is a built-in function designed to output text enclosed in quotes to the standard output.

```python
print("This is an example of the print function.")
```

## 4. Python Comments
In Python programs, comments are indicated by the # symbol. These comments are ignored by the CPU during execution of the program.

```python

# This is a single-line comment

"""
This is a multi-line comment
spanning multiple lines.
"""

# Example of using comments in code
print("Hello, World!")  # This will print Hello, World! to the console
```
## Additional Notes : 
Ensure that Python is installed and properly configured on your system.
Use a text editor or an Integrated Development Environment (IDE) to write and run your Python code.

# How Python Code is Executed

Python code execution involves several steps from writing the code to seeing the output. This process includes interpreting the code, executing it, and managing the flow of execution. Below are the key steps involved in Python code execution:

## 1. Writing the Code
Python code is written in plain text files with a `.py` extension. You can use any text editor or Integrated Development Environment (IDE) to write your Python code.

```python
# Example of a simple Python script
print("Hello, World!")
```
## 2. Source Code to Bytecode
When you run a Python script, the Python interpreter first compiles the source code (.py files) into bytecode (.pyc files). Bytecode is a low-level representation of your source code that is platform-independent. This step is done automatically and transparently by the interpreter.

## 3. Execution by Python Virtual Machine (PVM)
The bytecode is then executed by the Python Virtual Machine (PVM). The PVM interprets the bytecode and performs the actual operations described by your code. This involves interacting with the underlying operating system and hardware to execute tasks such as reading/writing files, printing to the screen, or performing calculations.

## 4. Handling Import Statements
If your Python code imports other modules or packages, the interpreter locates these modules, compiles them into bytecode (if not already done), and then executes their code. This allows you to reuse code across different scripts and projects.

```python

import math

# Example of using an imported module
print(math.sqrt(16))
```
## 5. Managing Execution Flow
Python manages the flow of execution through the code by following control structures such as loops, conditionals, and function calls. The interpreter keeps track of the current state and context to ensure that the code executes correctly and efficiently.

```python
# Example of control flow in Python
for i in range(5):
    if i % 2 == 0:
        print(f"{i} is even")
    else:
        print(f"{i} is odd")
```
## 6. Error Handling
During execution, if the interpreter encounters any errors (syntax errors, runtime errors, etc.), it raises exceptions. Python provides mechanisms to handle these exceptions gracefully, allowing the program to recover or exit cleanly.

```python
# Example of error handling in Python
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero!")
```

## Python Variables
A variable is simply a name given to a memory location that holds the value assigned to the variable. In Python, you can create a variable by assigning a value to a name.

```python
# Example of variable assignment
message = "Hello, World!"
number = 42
pi = 3.14
```

## Python Variable Scope
In Python, we can declare variables in three different scopes: `local scope`, `global scope`, and `nonlocal scope`.

`Local Scope:` Variables declared inside a function are in the local scope and can only be accessed within that function.

```python
def my_function():
    local_var = "I am local"
    print(local_var)

my_function()
# print(local_var)  # This will cause an error because local_var is not accessible outside the function
```
`Global Scope:` Variables declared outside any function are in the global scope and can be accessed from anywhere in the code.

```python
global_var = "I am global"
def my_function():
    print(global_var)

my_function()
print(global_var)
```
`Nonlocal Scope:` Variables declared inside a nested function, whose scope is not local or global, are in the nonlocal scope.

```python
def outer_function():
    outer_var = "I am outer"
    
    def inner_function():
        nonlocal outer_var
        outer_var = "I am changed"
        print(outer_var)
    
    inner_function()
    print(outer_var)

outer_function()
```

## Python Operators :
Operators are special symbols that perform operations on variables and values. They are used to perform computations and manipulations on data. Some common types of operators in Python include:

`Arithmetic Operators:` Used to perform mathematical operations.
```python
a = 10
b = 5
print(a + b)  # Addition
print(a - b)  # Subtraction
print(a * b)  # Multiplication
print(a / b)  # Division
print(a % b)  # Modulus
print(a ** b) # Exponentiation
print(a // b) # Floor division
```

`Assignment Operators:` Used to assign values to variables.
```python
x = 10
x += 5  # Equivalent to x = x + 5
x -= 3  # Equivalent to x = x - 3
x *= 2  # Equivalent to x = x * 2
x /= 4  # Equivalent to x = x / 4
x %= 3  # Equivalent to x = x % 3
x **= 2 # Equivalent to x = x ** 2
x //= 2 # Equivalent to x = x // 2
```

`Comparison Operators:` Used to compare values.
```python
a = 10
b = 5
print(a == b)  # Equal to
print(a != b)  # Not equal to
print(a > b)   # Greater than
print(a < b)   # Less than
print(a >= b)  # Greater than or equal to
print(a <= b)  # Less than or equal to
```

`Logical Operators:` Used to combine conditional statements.
```python
a = True
b = False
print(a and b)  # Logical AND
print(a or b)   # Logical OR
print(not a)    # Logical NOT
```

`Bitwise Operators:` Used to perform bit-level operations.
```python
a = 10  # 1010 in binary
b = 4   # 0100 in binary

print(a & b)  # Bitwise AND
print(a | b)  # Bitwise OR
print(a ^ b)  # Bitwise XOR
print(~a)     # Bitwise NOT
print(a << 1) # Bitwise left shift
print(a >> 1) # Bitwise right shift
```
