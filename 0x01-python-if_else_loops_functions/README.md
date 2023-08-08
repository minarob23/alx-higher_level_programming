# 0x01. Python - if/else, loops, functions

# Learning Objectives
At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

# General
* Why Python programming is awesome?
* Why indentation is so important in Python?
* How to use the if, if ... else statements?
* How to use comments?
* How to affect values to variables?
* How to use the while and for loops?
* How is Python’s for different from C‘s?
* How to use the break and continues statements?
* How to use else clauses on loops?
* What does the pass statement do, and when to use it?
* How to use range?
* What is a function and how do you use functions?
* What does return a function that does not use any return statement?
* Scope of variables?
* What’s a traceback?
* What are the arithmetic operators and how to use them?

# Requirements
# Python Scripts
* Allowed editors: vi, vim, emacs
* All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
* All your files should end with a new line
* The first line of all your files should be exactly #!/usr/bin/python3
* A README.md file, at the root of the folder of the project, is mandatory
* Your code should use the pycodestyle (version 2.8.*)
* All your files must be executable
* The length of your files will be tested using wc
# C Scripts
* Allowed editors: vi, vim, emacs
* All your files will be compiled on Ubuntu 20.04 LTS using gcc, using the options -Wall -Werror -Wextra -pedantic -std=gnu89
* All your files should end with a new line
* Your code should use the Betty style. It will be checked using betty-style.pl and betty-doc.pl
* You are not allowed to use global variables
* No more than 5 functions per file
* In the following examples, the main.c files are shown as examples. You can use them to test your functions, but you don’t have to push them to your repo (if you do we won’t take them into account). We will use our own main.c files at compilation. Our main.c files might be different from the one shown in the examples
* The prototypes of all your functions should be included in your header file called lists.h
* Don’t forget to push your header file
* All your header files should be include guarded

![image](https://github.com/minarob23/alx-higher_level_programming/assets/102999008/0b5ba708-feaa-40d7-9244-8cb8afc719e5)

## Tasks :page_with_curl:

* **0. Positive anything is better than negative nothing** `mandatory`
  * Python program that assigns a random signed number to the variable `number` each time it is executed and prints whether `number` is positive or negative.
  * Prints the number followed by:
    * If the number is greater than 0: `is positive`
    * If the number is 0: `is zero`
    * If the number is less than 0: `is negative`
    * Followed by a new line.
 

* **1. The last digit** `mandatory`
  * Python program that assigns a random signed number to the variable `number` each time it is executed and prints its last digit.
  * Prints the string `Last digit of [number] is [last_digit]` followed by:
    * If the number is greater than 5: `and is greater than 5`
    * If the number is 0: `and is 0`
    * If the number is less than 6 and not 0: `and is less than 6 and not 0`
    * Followed by a new line.
    

* **2. I sometimes suffer from insomnia. And when I can't fall asleep, I play what I call the alphabet game** `mandatory`
  * Python program that prints the alphabet in lowercase, not followed by a new line.
  * Using only one `print` and one loop.
  * Storing characters in variables or importing modules not allowed.

* **3. When I was having that alphabet soup, I never thought that it would pay off** `mandatory`
  * Python program that prints the alphabet in lowercase, followed by a new line.
  * Using only one `print` and one loop.
  * Without storing characters in variables or importing modules.
  * Prints every letter except for `q` and `e`.

* **4. Hexadecimal printing** `mandatory`
  * Python program that prints all numbers from `0` to `98` in decimal and hexadecimal.
  * Using only one `print` and one loop.
  * Without storing numbers or strings in variables or importing modules.
  * Printing format: `[decimal] = [hexadecimal]`

* **5. 00...99** `mandatory`
  * Python program that prints numbers from `0` to `99` two digits each.
  * Numbers are separated by `, `, except for the last number, which is followed by a new line.
  * Using no more than two `print` functions and one loop.
  * Without storing numbers or strings in variables or importing modules.

* **6. Inventing is a combination of brains and materials. The more brains you use, the less material you need** `mandatory`
  * Python program that prints all possible different combinations of two digits in ascending order.
  * Numbers are separated by `, `, except for the last number, which is followed by a new line.
  * The two digits must be different - `01` and `10` are considered identical.
  * Using no more than three `print` functions and two loops.
  * Without storing numbers or strings in variables or importing modules.

* **7. islower** `mandatory`
  * Python function that checks for lowercase characters.
  * Returns `True` if `c` is lowercase, `False` otherwise.
  * Without importing modules or using `str.upper()` or `str.isupper()`.

* **8. To uppercase** `mandatory`
  * Python function that prints a string in
  uppercase followed by a new line.
  * Using no more than two `print` functions and one loop.
  * Without importing modules or using `str.upper()` or `str.isupper()`.

* **9. There are only 3 colors, 10 digits, and 7 notes; its what we do with them that's important** `mandatory`
  * Python function that prints the last digit of a number.
  * Returns the value of the last digit.
  * Without importing modules.

* **10. a + b** `mandatory`
  * 10-add.py: Python function that returns the addition of two integers.
  * Without importing modules.

* **11. a ^ b** `mandatory`
  * Python function that returns `a` to the power of `b`.
  * Without importing modules.

* **12. Fizz Buzz** `mandatory`
  * Python function that prints the numbers from `1` to `100` followed by a space.
  * For multiples of three, `Fizz` is printed instead of the number.
  * For multiples of five, `Buzz` is printed instead of the number.
  * For multiples of three and five, `FizzBuzz` is printed instead of the number.
  * Without importing modules.

* **13. Insert in sorted linked list** `mandatory`
  * C function that inserts a number into a sorted linked list.
  * If the function fails, returns `NULL`.
  * Otherwise, returns the address of the new node.
  * Helper files:
    * linked_lists.c: C functions handling linked lists for testing
    * 13-insert_number.py (provided by Holberton School).
    * lists.h: Header file containing definitions and prototypes for all types and functions used in linked_lists.c and 13-insert_number.py.
    

* **14. Smile in the mirror** `#advanced`
  * 100-print_tebahpla.py: Python program that prints the alphabet in reverse order, alternating lowercase and uppercase, not followed by a new line.
  * Using only one `print` and one loop.
  * Without storing characters in variables or importing modules.

* **15. Remove at position** `#advanced`
  * 101-remove_char_at.py: Python function that creates a copy of a string without the character at position `n`.
  * Without importing modules.

* **16. ByteCode -> Python #2** `#advanced`
  * 102-magic_calculation.py: Python function matching exactly a
  bytecode provided by Holberton School.


