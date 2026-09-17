# Checkpoint 3 Learning Notes

## Lists

- A list can store multiple values in one variable.
- Lists are ordered, mutable, and can store different data types.
- Items are separated by commas.
- Indexing allows access to individual items.
- The first item starts at index `0`.
- A `for` loop can go through each item one at a time.

### List Methods Practiced

- `append()` - adds an item to the end by default.
- `insert()` - inserts an item at a chosen position.
- `remove()` - removes a specific value.
- `index()` - returns the position of a value.
- `count()` - counts how many times a value appears.

## Tuples

- A tuple stores multiple values in one variable like a list.
- Tuples are immutable.
- Values cannot be directly changed, added, or removed.
- Tuple values are indexed and can be accessed individually.
- A `for` loop can go through tuple values one at a time.
- To change tuple contents, convert the tuple to a list, make the change, then convert it back to a tuple.

## Dictionary Methods

- `clear()` - clears the dictionary.
- `copy()` - creates a copy of the dictionary.
- `keys()` - returns only the keys.
- `values()` - returns only the values.
- `items()` - returns the key-value pairs.
- `update()` - updates an existing key-value pair and can merge another dictionary.

### Looping Through Dictionary Values

- `.values()` gets all values from a dictionary.
- The loop goes through those values one at a time.
- The loop variable temporarily holds the current value.
- The indented code runs once for each value.
- The dictionary keys are not returned by `.values()`.

### Looping Through Key-Value Pairs

- `.items()` gets both keys and values.
- The loop goes through each key-value pair one at a time.
- One variable can hold the key while another holds its value.
- The indented code runs once for each pair.

## Sets

- A set is a built-in Python data structure.
- It can store multiple unique values in one variable.
- Sets use curly brackets `{ }`.
- Sets are unordered.
- Duplicate values are not kept.
- Sets do not use indexing.
- Loop through a set to access its values individually.

### Set Methods Practiced

- `add()` - adds one item.
- `update()` - adds multiple elements.
- `clear()` - clears the set.
- `pop()` - removes an arbitrary element.
- `remove()` - removes a specific element and raises an error if it is not present.
- `discard()` - removes an element without raising that same error if it is missing.
- `intersection()` - returns values that exist in both sets as a new set.
- `union()` - combines unique values from two or more sets into a new set.

## Split and Join

### `.split()`

- Splits one string into multiple pieces.
- Returns the pieces as a list.
- A separator can be chosen.
- Whitespace is the default separator.

### `.join()`

- Combines multiple strings into one string.
- You choose what goes between each item.
- Common separators include spaces, commas, and dashes.

**Memory aid:** `split = take apart`, `join = put together`.

## Modules

- A module is a Python file that contains reusable code.
- A module can include functions, classes, and variables.
- Modules can be imported into other Python programs.
- Modules help avoid rewriting the same code and help keep code organized.
- Use `import` to bring a module into a program.
- Built-in modules come with Python.
- Custom modules are Python files you create yourself.

## `random` Module

- Built into Python.
- Used to generate random or pseudo-random values.
- Import with `import random`.
- Can generate random numbers, select a random item, or shuffle a list.

Functions practiced:

- `random.randint()`
- `random.choice()`
- `random.shuffle()`
- `random.random()`

## `datetime` Module

- Built into Python.
- Used to work with dates and times.
- Can get the current date and time.
- Can create a specific date or time.
- Can access year, month, day, hour, minute, and second.
- Can perform date/time calculations.
- Uses format codes to control how dates and times are displayed.
- `strftime()` formats a date/time into a string.

### Format Codes Practiced

- `%Y` - 4-digit year
- `%m` - month number
- `%d` - day
- `%A` - full weekday
- `%B` - full month
- `%H` - 24-hour clock hour
- `%I` - 12-hour clock hour
- `%M` - minutes
- `%S` - seconds
- `%p` - AM/PM

## Custom Modules

- Create a Python file that can be imported into another program.
- For the practice completed in this checkpoint, the custom module was saved in the same directory as the main file.
- A function can be created inside the custom module and then imported for use in the main program.

## `pip` and `pip3`

- `pip` is Python's package installer.
- It installs external packages/libraries that do not come built into Python.
- It downloads packages from the Python Package Index (PyPI) by default.
- It is usually run from the terminal or command prompt.
- `pip3` is used to install packages for Python 3.
- `pip3` can be useful when a system has multiple Python versions and `pip` may point to a different installation.
- On many newer systems, `pip` and `pip3` may point to the same Python 3 installer.

## `time` Module

- Built into Python.
- Used for time-related operations.
- Import with `import time`.
- `time.sleep()` pauses the program for a specified number of seconds.
- `time.time()` returns the current time as a timestamp in seconds since the Unix epoch.
- Can be used to measure how long code takes to run.
- Useful for adding delays or pauses.
- `datetime` is generally more appropriate for more complex date/calendar work.
