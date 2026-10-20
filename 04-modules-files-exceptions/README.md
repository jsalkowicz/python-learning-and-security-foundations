# Section 4 — Modules, Files & Exceptions

**Status:** Complete  
**Type:** Guided Python learning and practice

## Overview

This section focused on file handling and exception handling in Python. I practiced reading text files in several ways, working with file paths, using the `with` statement, creating and writing files, and handling errors more cleanly with `try`, `except`, and `finally`.

The exercises came from guided Python training. I am not presenting the course exercises as original software projects. These notes document what I practiced, what I changed, what confused me at first, and what I learned.

## Reading files

I started by opening a file with:

```python
file = open("testfile.txt", "r")
```

The `"r"` means read mode.

At first I printed the variable that held the opened file:

```python
print(file)
```

That did not print the contents of the file. Python printed information about the open file object instead, including the filename, mode, and encoding.

To read the actual contents, I used:

```python
print(file.read())
```

I also stored the result of `.read()` in a variable before printing it:

```python
file = open("testfile.txt", "r")
content = file.read()
print(content)
file.close()
```

Storing the contents in a variable makes the data reusable later instead of only displaying it immediately.

### Reading a specific number of characters

I learned that `.read()` can also take a number:

```python
content = file.read(5)
```

This reads up to five characters starting from the file's current position.

## Relative and absolute file paths

I practiced opening a file in the same working directory using a relative path:

```python
open("testfile.txt", "r")
```

I also opened a file using a full Windows path. My first attempt caused a `unicodeescape` syntax error because Python interpreted the backslashes as escape characters.

I fixed it by making the path a raw string:

```python
open(r"C:\Users\example\Desktop\myfile.txt", "r")
```

This was a useful troubleshooting example because Windows paths come up often when working with files.

## Reading one line at a time

I used `.readline()` to read one line from a file at a time:

```python
content = open("testfile.txt", "r")
print(content.readline())
print(content.readline())
```

The first call reads the first line. The second call continues from the current file position and reads the next line.

I then used a loop so I did not have to repeat the same statement:

```python
content = open("testfile.txt", "r")

for i in range(2):
    print(content.readline())
```

This connected file handling back to the loop concepts I learned earlier.

## Using `with`

I learned that the `with` statement is a cleaner way to work with files:

```python
with open("testfile.txt", "r") as content:
    print(content.read())
```

When the indented block finishes, Python closes the file automatically. This reduces the chance that I leave a file open by mistake.

## `readlines()`

I used:

```python
lines = content.readlines()
```

to read all lines into a list.

For example, a two-line file can produce a list similar to:

```python
["this is a test file.\n", "this is the second line of text."]
```

Each item is one line. `\n` represents a newline character.

I then looped through the list:

```python
content = open("testfile.txt", "r")
lines = content.readlines()

for i in lines:
    print(i, end="")
```

I was initially confused about why `end=""` was being used. The lines read from the file can already contain newline characters, while `print()` normally adds another newline. Using `end=""` prevents extra blank lines from being added.

## Types of errors

I practiced the difference between syntax errors and runtime errors.

### Syntax error

A syntax error happens when Python cannot understand the structure of the code. In my exercise, I deliberately added extra characters after a valid statement and got:

```text
SyntaxError: invalid syntax
```

The program could not run because the code itself was not valid Python syntax.

### Runtime error / exception

I then ran:

```python
print(12 / 0)
```

The syntax was valid, so Python started executing the program. The failure happened during execution and raised:

```text
ZeroDivisionError: division by zero
```

The traceback showed the file, line number, and statement that caused the exception.

## `try` and `except`

I used `try` and `except` so a runtime error could be handled instead of immediately stopping the program:

```python
try:
    print(32 / 0)
except:
    print("That is not going to work")
```

I then practiced catching a specific exception:

```python
try:
    print(32 / 0)
except ZeroDivisionError as error:
    print(error)
```

`as error` stores the exception information in a variable, and printing it displayed Python's original message:

```text
division by zero
```

Catching a specific exception makes it clearer what problem the code is expecting.

## `finally`

I learned that a `finally` block runs whether the `try` block succeeds or an exception occurs.

```python
try:
    print(32 / 0)
except ZeroDivisionError as error:
    print(error)
finally:
    print("This part always runs")
```

This is useful for cleanup work that should happen no matter what, such as releasing a resource.

## Creating and writing files

I created a file and wrote text to it with write mode:

```python
file = open("testingfile.txt", "w")
file.write("My name is John")
file.close()
```

If the file does not exist, `"w"` can create it. If the file already exists, write mode can overwrite its existing contents, so it needs to be used carefully.

I also learned that `.write()` does not automatically add a newline.

## `writelines()`

`writelines()` can write multiple strings from a list or another iterable:

```python
lines = [
    "First line\n",
    "Second line\n",
    "Third line\n"
]

file = open("testingfile.txt", "w")
file.writelines(lines)
file.close()
```

One detail I learned is that `writelines()` does not automatically add line breaks, so I need to include `\n` myself when I want each string on its own line.

## What I did not understand right away

- Printing the file variable prints the file object, not the contents.
- `.read()` is what actually retrieves the contents.
- Windows backslashes can be interpreted as escape characters in a normal Python string.
- `readline()` continues from the current position instead of restarting at the top.
- `readlines()` returns a list rather than one large string.
- The lines returned from a file can already contain `\n`, which is why `print(..., end="")` can prevent extra blank lines.
- A syntax error is different from a runtime exception.
- `as error` gives me access to the exception message.
- `finally` runs at the end whether the operation succeeds or fails.

## Why this matters for security and AI security

File handling and error handling are basic building blocks for later security work. Security scripts often need to read logs, configuration files, JSON, output from tools, or datasets. They also need to handle missing files, bad input, API failures, and other unexpected conditions without failing in an uncontrolled way.

These same foundations will be useful later when I work with AI-security logs, evaluation datasets, model or application configuration, API responses, and security-test results.

## Evidence

Selected sanitized screenshots are stored in:

`evidence/screenshots/`

Raw screenshots are kept separately from the public GitHub-ready package.
