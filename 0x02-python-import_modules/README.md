# 0x02. Python - import & modules

# Learning Objectives
At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

# General
* Why Python programming is awesome?
* How to import functions from another file?
* How to use imported functions?
* How to create a module?
* How to use the built-in function dir()?
* How to prevent code in your script from being executed when imported?
* How to use command line arguments with your Python programs?

# Requirements

# General
* Allowed editors: vi, vim, emacs
* All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
* All your files should end with a new line
* The first line of all your files should be exactly #!/usr/bin/python3
* A README.md file, at the root of the folder of the project, is mandatory
* Your code should use the pycodestyle (version 2.8.*)
* All your files must be executable
* The length of your files will be tested using wc

![image](https://github.com/minarob23/alx-higher_level_programming/assets/102999008/3aa79c0b-c30a-4859-bfa6-2c8bcf01f42e)

# Tasks:
* **0. Import a simple function from a simple file**
  * 0-add.py: Python program that imports the function `def add(a, b):` from these file and prints the result of the addition `1 + 2 = 3`.
  * Output: `<a value> + <b value> = <add(a, b) value>` followed by a new line.

* **1. My first toolbox!**
  * 1-calculation.py: Python program that imports functions from the file 1-calculation.py and prints the result of the addition, subtraction, multiplication and division of `10` and `5`.
  * Output: `<a value> <operator> <b value> = <operation(a, b) value>` followed by a new line.

* **2. How to make a script dynamic!**
  * 2-args.py: Python program that prints the number of and list of its arguments.
  * Output: `[Number of arguments] argument` (if number is one) or `arguments` (otherwise), followed by:
    * `:` (or `.` if no argumets were passed), followed by
    * A new line, followed by
    * One argument per line - the position of the argument (starting at `1`) followed by `:` followed by the argument value and another new line.

* **3. Infinite addition**
  * 3-infinite_add.py: Python program that prints the result of the addition of all arguments.
  * Output: Sum of the arguments followed by a new line.

* **4. Who are you?**
  * 4-hidden_discovery.py Python program that prints all the names defined by the compiled module `hidden_4.pyc`.
  * Output: One name per line in alphabetical order.
  * Names starting with `__` are not printed.

* **5. Everything can be imported**
  * 5-variable_load.py: Python program that imports the variable `a` from the file 5-variable_load.py and prints its value.

* **6. Build my own calculator!**
  * 100-my_calculator.py: Python program that imports all functions from the file 100-my_calculator.py and handles basic operations.
  * Usage: `./100-my_calculator.py <a> <operator> <b>` followed by a new line.
  * Output: `<a> <operator> <b> = <result>` followed by a new line.
  * The parameter `operator` can be:
    * `+` for addition
    * `-` for subtraction
    * `*` for multiplication
    * `/` for division
  * If the operator is none of the above, the function prints `Unknown operator.  Available operators: +, -, *, and /` followed by a new line and exits  with a status value of `1`.
  * If the number of arguments is not three, the program prints `Usage: ./100-my_calculator.py <a> <operator> <b>` followed by a new line and exits with a status value of `1`.

* **7. Easy print**
  * 101-easy_print.py: Python program that prints `#pythoniscool` followed by a new line in the standard output.
  * Without using `print`, `eval`, `open`, or `sys`.

* **8. ByteCode -> Python #3**
  * 102-magic_calculation.py: Python function matching exactly a bytecode provided by Holberton School.

* **9. Fast alphabet**
  * 103-fast_alphabet.py: Python program that prints the alphabet in uppercase, followed by a new line.
  * Without using loops, conditoinals, `str.join()`, string literals, or system calls.
