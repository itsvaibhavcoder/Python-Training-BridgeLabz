# Python Coding Guidelines

## 1. Python String Format
Using Python String Format in the Print function enhances the readability and maintainability of the code.

## 2. Naming Conventions

- **Global or Local Variables**: Should be in lower case and use an underscore to join words.
- **Constants in Python**: Should be in upper case and use an underscore to join words.
- **Function Names**: Should be in lower case and use an underscore to join words.
- **Module Names**: Should be in lower case and use an underscore to join words.
- **Package Names**: Should be in lower case and use an underscore to join words.
- **Class Names**: Should follow the CapWords convention.
- **Method Names**: Should be in lower case and use an underscore to join words.
- **Method Arguments**:
  - Every instance method should have `self` as its first argument.
  - Class methods should have their first argument named `cls`.

## 3. Descriptive Variable Names
- Avoid names that are too general or wordy. Maintain a good balance between the two.
  - **Bad**: `user_list`, `dict_to_store_defns_of_a_word`, `swapNums`, `moveInts`.
  - **Good**: `user_info`, `word_definitions`, `swap_numbers`, `move_integers`.
- Avoid naming things like “X”, “Y” or “Z”.
- Capitalize all letters of an abbreviation when using camelcase.
- Avoid names starting with digits. Combination of lowercase letters (a to z), uppercase letters (A to Z), digits (0 to 9), or an underscore (_) can be used.

## 4. Hard Coding Variables
Hardcoding values to variables within your code can create maintenance and scalability challenges.

## 5. Embracing Modularization
Writing monolithic scripts without breaking code into reusable functions or classes can make code difficult to test, debug, and maintain.

## 6. Proper Function Usage
Python Functions are blocks of code that are run only when called. Guidelines for Python functions:
1. Proper comments for the function.
2. Avoid the use of global variables.
3. Use function type annotations, default is `Any`.

## 7. Handling Exceptions
Ignoring exceptions or using bare `except:` clauses can hide bugs and lead to unexpected failures. Be specific about the exceptions you catch and handle, improving debugging and error resolution.
