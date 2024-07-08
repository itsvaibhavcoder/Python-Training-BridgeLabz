# Python Programming Notes - Day 1

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

## Python Operators 
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
## Modularization 
Modularization in Python can be achieved using `functions`, `classes`, `modules`, and `packages`. It involves breaking down a large program into smaller, manageable, and reusable pieces of code.

### Example:
```python
# Using a function

def greet(name):
    return f"Hello, {name}!"

print(greet("Alice"))

# Using a class

class Greeter:
    def __init__(self, name):
        self.name = name

    def greet(self):
        return f"Hello, {self.name}!"

greeter = Greeter("Bob")
print(greeter.greet())

# Using a module (saved in greet_module.py)

def greet(name):
    return f"Hello, {name}!"

# Using a package (folder structure with __init__.py)

# my_package/
#     __init__.py
#     greeter.py
# greeter.py
def greet(name):
    return f"Hello, {name}!"
```

## Python Blocks
Python uses indentation to define a block of code. This block of code could be:

## Function Block
```python
def func():
    print("This is a function block.")
```

## Condition Blocks
```python
if True:
    print("This is an if block.")

while True:
    print("This is a while block.")
    break
```

## Loop Blocks
```python
for i in range(5):
    print(f"This is a for loop block: {i}")

while True:
    print("This is a while loop block.")
    break
```

## Exception Blocks
```python
try:
    x = 1 / 0
except ZeroDivisionError:
    print("This is an exception block.")
```

## Python Functions
A function is a block of code which only runs when it is called. You can pass data, known as parameters, into a function. In Python, indentation is crucial as it defines the block of code.

Example:
```python
# Defining a function
def greet(name):
    print(f"Hello, {name}!")

# Calling a function
greet("Charlie")

# Function with parameters
def add(a, b):
    return a + b

result = add(5, 3)
print(result)
```
## Key Points
Functions are defined using the `def` keyword.
`Indentation` is used to define the body of the function.
Functions can have `parameters` to pass data.
Functions can return values using the `return` statement.

## Hard Coding
Hard coding refers to the practice of embedding fixed data directly into the source code. It should generally be avoided as it makes the code less flexible for future changes. However, it can be acceptable for values that are constants and will never change, such as the value of PI.

### Example
```python
# Hardcoded value of PI
PI = 3.14159265359

# Example of using PI
radius = 5
area = PI * (radius ** 2)
print(f"Area of the circle is: {area}")
```

## Python Built-In input() Function
The input() function is a Python built-in function designed to receive user input from the standard input (typically the keyboard). It returns the input as a string.

Example:
```python
# Using input() to receive user input
name = input("Enter your name: ")
print(f"Hello, {name}!")
```

## Standard Input (stdin)
Standard input (stdin) is a commonly used term in programming, denoting the default input device that a program utilizes to retrieve data. Typically, this is the keyboard, but it can also be a file or another input device.

Example:
```python

# Receiving input from the standard input (keyboard)
age = input("Enter your age: ")
print(f"You are {age} years old.")
```
##  Type Casting
Type casting is the method to convert a Python variable's datatype into a certain data type to perform the required operation. There are two types of type casting in Python:

`Implicit Type Casting:` Automatically performed by the Python interpreter.
`Explicit Type Casting:` Performed manually by the programmer.

Examples:
`Implicit Type` Casting:
```python
# Python automatically converts int to float
num_int = 10
num_float = 10.5

result = num_int + num_float
print(f"Result is {result} and type is {type(result)}")
```

`Explicit Type` Casting:
```python
# Manually converting one data type to another
num_str = "100"
num_int = int(num_str)

print(f"num_int is {num_int} and type is {type(num_int)}")

# Converting float to int
num_float = 10.5
num_int = int(num_float)

print(f"num_int is {num_int} and type is {type(num_int)}")
```
## Python Error Handling
When an error or exception occurs mainly at runtime, Python will normally stop and generate an error message. Handling such errors or exceptions during program execution is called Error Handling.

### Example:
```python
# Example of error handling
try:
    x = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero!")'
```

## Python Runtime Errors
Errors that occur at runtime (after passing the syntax test) are called exceptions or runtime errors. Python creates an exception object for well-defined errors like ValueError, NameError, etc. It's important to handle both specific errors and generic errors.

Example:
```python
# Example of handling specific and generic errors
try:
    value = int("abc")
except ValueError:
    print("ValueError: Cannot convert string to integer")
except Exception as e:
    print(f"An error occurred: {e}")
```
## Python `try:` and `except:` Block
Python executes code in the `try`: block as a “normal” part of the program. In case of any error, the code in the `except`: block is executed.

Example:
```python
# Example of try and except block
try:
    numbers = [1, 2, 3]
    print(numbers[5])
except IndexError:
    print("IndexError: List index out of range")

# Example with multiple exceptions
try:
    result = 10 / int(input("Enter a number: "))
except ZeroDivisionError:
    print("Cannot divide by zero!")
except ValueError:
    print("Invalid input! Please enter a valid number.")
```

# Python Programming Notes - Day 2

## Standard Input (stdin)
Standard input is a commonly used term in programming, denoting the default input device that a program utilizes to retrieve data. Typically, this is the keyboard, but it can also be a file or another input device.

## Python Built-In input() Function
The `input()` function is a Python built-in function designed to receive user input from the standard input. When the user types and presses the return key, the input provided by the user is captured.

### Example:
```python
user_input = input("Enter something: ")
print(f"You entered: {user_input}")
```

## Formatted String Literal (f-string)
An f-string looks very much like a typical Python string except that it’s prepended by the character f'' or F''. The magic of f-strings is that you can embed Python expressions directly inside them by using curly braces {}. The expression is evaluated and converted to string representation, and the result is interpolated into the original string in that location.

Example:
```python
name = "Alice"
age = 30
print(f"Name: {name}, Age: {age}")
```
## Outcome of Executing help(print)
help is a Python built-in function to get more helpful information about Python built-in functions. The execution of help(print) results in the following:
```python
print(value, ..., sep=' ', end='\n', file=sys.stdout, flush=False)
```

value: Can print multiple values to a stream or by default to the standard output (the terminal or screen).
sep: The separator, by default an empty text ' '.
end: Ends by default with a new line indicated by '\n'.

Example:
```python
print("Hello", "World", sep='-', end='!')
# Output: Hello-World!
```
## help(input)
The help(input) function provides details about the input function. In the context of certain environments like Google Colab, it may use raw_input(prompt='') method of google.colab._kernel.Kernel instance, overriding the standard Python library input implementation.

Example:
```python
help(input)
```
## Python Data Types
Data types define the kind of data that can be stored in memory for a variable. In Python, data types are implicitly assigned. All built-in data types belong to Python classes. They can be categorized as either:

### Primitive Data Types
- **int**: Integer values
- **float**: Floating-point values
- **str**: String values
- **bool**: Boolean values (True or False)

### Derived Data Types
- **list**: Ordered, mutable collection of items
- **dict**: Unordered, mutable collection of key-value pairs
- **set**: Unordered, mutable collection of unique items
- **tuple**: Ordered, immutable collection of items

## Python Explicit Type Conversion
Type conversion is converting from one data type to another. Explicit type conversion is achieved through Python's built-in functions such as `int()`, `float()`, and `str()`.

### Example:
```python
num_str = "123"
num_int = int(num_str)  # Converts string to integer
num_float = float(num_str)  # Converts string to float
num_str_again = str(num_int)  # Converts integer back to string
```

## Python Constant
Constants are types of variables whose values cannot be altered or changed after initialization. These values are universally proven to be true and they cannot be changed over time.

Example:
```python
PI = 22 / 7
```
Naming Convention to define constants is all caps.
Python constants are declared and initialized at the beginning of the program as global variables or preferably in different modules/files.

## Python Multiplication and Power Operator
Multiplication Operator (*): Used to multiply two values.
Power Operator ()**: Used to raise a number to the power of another number.
Example:
```python
result_mult = 5 * 3  # Multiplication
result_pow = 2 ** 3  # Power (2 raised to the power of 3)
```

## Python Operator Precedence
In Python, the order of operations follows the same principles as PEMDAS.

`PEMDAS` is an acronym that stands for:

P: Parentheses
E: Exponents
M: Multiplication
D: Division
A: Addition
S: Subtraction
Expressions inside parentheses are evaluated first, followed by exponents, then multiplication and division (from left to right), and finally addition and subtraction (from left to right).

Example:
```python
result = (2 + 3) * 2 ** 2 / 2 - 5  # Evaluates to 5.0
```

## Python Format Specifier for Floating-Point Numbers
For formatting float variables as strings with a format specifier expression like {number:.2f}:
: separates the number from the format specifier .2f.
.2 specifies the number of digits to be displayed after the decimal point.
f indicates that the value should be formatted as a floating-point number.
Example:

```python
number = 3.14159
formatted_number = f"{number:.2f}"  # Formats to '3.14'
```
##  Python Operators
Operators are special symbols that perform operations on variables and values. They include:

### Arithmetic Operators
- **Addition (+)**: Adds two values.
- **Subtraction (-)**: Subtracts one value from another.
- **Multiplication (*)**: Multiplies two values.
- **Division (/)**: Divides one value by another.
- **Modulus (%)**: Returns the remainder of the division.
- **Power (**)**: Raises a number to the power of another number.

### Example:
```python
sum_result = 5 + 3  # Addition
diff_result = 5 - 3  # Subtraction
prod_result = 5 * 3  # Multiplication
quot_result = 5 / 3  # Division
mod_result = 5 % 3  # Modulus
pow_result = 2 ** 3  # Power
```

## Assignment Operators
Assignment (=): Used to assign a value to a variable.
Example:
```python

x = 10
y = 5
```
## Comparison Operators
Equal (==): Checks if two values are equal.
Not Equal (!=): Checks if two values are not equal.
Greater Than (>): Checks if one value is greater than another.
Less Than (<): Checks if one value is less than another.
Greater Than or Equal To (>=): Checks if one value is greater than or equal to another.
Less Than or Equal To (<=): Checks if one value is less than or equal to another.

Example:
```python
a = 10
b = 5
result = a == b  # False
result = a != b  # True
result = a > b  # True
result = a < b  # False
result = a >= b  # True
result = a <= b  # False
```

## Logical Operators
and: Returns True if both statements are true.
or: Returns True if one of the statements is true.
not: Reverses the result, returns False if the result is true.
Example:
```python
a = True
b = False
result = a and b  # False
result = a or b  # True
result = not a  # False
```

## Bitwise Operators
AND (&): Sets each bit to 1 if both bits are 1.
OR (|): Sets each bit to 1 if one of two bits is 1.

Example:
```python
a = 5  # 0101 in binary
b = 3  # 0011 in binary
result = a & b  # 0001 (1 in decimal)
result = a | b  # 0111 (7 in decimal)
```

## Special Operators
is: Returns True if both variables are the same object.
is not: Returns True if both variables are not the same object.
Example:
```python
x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

result = x is z  # True
result = x is y  # False
result = x == y  # True
result = x is not y  # True
```

## Conditional Operation
The conditional operation allows testing a condition in a single line, replacing the multiline if-else structure and making the code compact. It predominantly uses Comparison Operators and Logical Operators.

Example:
```python
a = 10
b = 20
max_value = a if a > b else b  # max_value will be 20
```
## Python Shorthand If Else
If you have only one condition to execute, one for if, and one for else, you can put it all on the same line using Python shorthand.

Example:
```python
gender = 'male'
pronoun = 'his' if gender == 'male' else 'her'
```
