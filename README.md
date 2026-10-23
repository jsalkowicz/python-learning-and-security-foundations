# Python Learning and Security Foundations

I am using this repository to document my hands-on Python learning as I work through a guided beginner course and build toward security-focused scripting and automation.

The goal is to keep a clear record of what I practiced, what I built, what I changed, and what I learned as the course progresses.

> **Training note:** The exercises in this repository come from guided Python training. I am not presenting the course exercises as original software projects. When I make my own changes to an exercise, I call them out in the section notes.

## Progress

| Section | Focus | Status |
| --- | --- | --- |
| 1 | Python Fundamentals & Conditional Logic | ✅ Complete |
| 2 | Loops & Functions | ✅ Complete |
| 3 | Data Structures | ✅ Complete |
| 4 | Modules, Files & Exceptions | ✅ Complete |
| 5 | System Operations & Practical Scripting | 🟡 In Progress |
| 6 | Basic Networking | ⬜ Planned |

## Python Fundamentals & Conditional Logic

This section starts with running basic Python programs and moves through strings, variables, data types, operators, user input, type casting, and conditional logic.

The two main guided exercises were:

- a **Simple Calculator** that accepts numeric input and performs arithmetic operations
- an **Authentication System** that uses multiple inputs and conditional logic to decide whether authentication succeeds or fails

I also modified the authentication exercise by adding a third input and an additional failure message.

➡️ [View the Python Fundamentals & Conditional Logic documentation](01-python-fundamentals-and-conditional-logic/README.md)

## Loops & Functions

This section adds repeated execution and reusable code.

I practiced `for` and `while` loops, `range()`, `break`, `continue`, function definitions, parameters and arguments, return values, and variable scope.

The main guided project was a function-based calculator. I added a modulus option as an extra operation to practice extending the existing logic.

➡️ [View the Loops & Functions documentation](02-loops-and-functions/README.md)

## Modules, Files & Exceptions

This section focused on working with files and handling errors in Python. I practiced opening and reading text files in several different ways, working with file paths, using the `with` statement, creating and writing files, and handling runtime errors without immediately stopping the program.

Some of the main concepts I practiced were:

- opening files with `open()` and read mode (`"r"`)
- reading file contents with `read()`, `readline()`, and `readlines()`
- limiting `read()` to a specific number of characters
- using relative and absolute file paths
- using raw strings for Windows file paths
- reading multiple lines with loops
- using the `with` statement to automatically close files
- understanding syntax errors, runtime errors, and tracebacks
- handling exceptions with `try`, `except`, and `finally`
- catching specific exceptions such as `ZeroDivisionError`
- creating and writing files with write mode (`"w"`)
- using `write()` and `writelines()`

One troubleshooting issue I ran into was a `unicodeescape` error when using a full Windows file path. I learned that Python can interpret backslashes as escape characters, and I fixed the issue by using a raw string for the path.

I also learned that `readlines()` returns a list of lines rather than one large string. When looping through those lines, I used `end=""` with `print()` to avoid adding extra blank lines because the file lines could already contain newline characters.

➡️ [View the Modules, Files & Exceptions documentation](04-modules-files-exceptions/README.md)

## System Operations & Practical Scripting

This section is in progress and currently covers the beginning of Python's built-in `os` module.

So far I have practiced:

- checking the current working directory with `os.getcwd()`
- listing files and folders with `os.listdir()`
- looping through directory contents
- changing Python's working directory with `os.chdir()`
- creating a directory with `os.mkdir()`
- removing an empty directory with `os.rmdir()`
- verifying filesystem changes from PowerShell

I also learned that some functions can successfully perform an action while returning `None`, and that running a script before saving the latest editor changes can make it look like updated code did not run.

➡️ [View the System Operations & Practical Scripting documentation](05-system-operations-practical-scripting/README.md)

## Current Direction

I am learning Python as a foundation for AI security engineering and analysis.

The skills in this repository will eventually support work such as:

- processing security logs and AI telemetry
- working with REST APIs and JSON
- interacting with AI and LLM APIs
- analyzing security test results
- automating repetitive security tasks
- working with AI evaluation datasets
- building AI security testing tools
- detecting risky behavior or abnormal conditions
- producing useful security-focused output and reports

My original AI security projects will be kept separate from these guided Python course exercises once I reach that stage.

## Course Source

Guided training: **Python for Beginners with Hands-On Projects**, available through freeCodeCamp on YouTube.

Course: https://youtu.be/oDOw5tB3Udw
