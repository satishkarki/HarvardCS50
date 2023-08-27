# Harvard CS50 Lecture Note
## Lecture 0: Functions, Variables 

### Print Function
The print() function in Python is used to display text or other data to the console. You can use it to output messages, variables, or the results of calculations. Here's the basic syntax of the print() function:

```python
print(value1, value2, ..., sep=' ', end='\n', file=sys.stdout, flush=False)
```
* value1, value2, ...: These are the values you want to print. You can pass one or more values separated by commas. Python will automatically convert them to strings and display them.

* sep: It's an optional parameter that specifies the separator between values. By default, it's a space ' '.

* end: It's also an optional parameter that specifies what to print at the end. By default, it's a newline character '\n', which means each print() call ends with a new line. You can change it to something else if you want the next print() to appear on the same line.

* file: You can specify a different output file by providing a file object here. By default, it's set to sys.stdout, which means it prints to the console.

* flush: This is a Boolean flag (True or False) that determines whether the output should be flushed (written to the file or console) immediately or buffered. By default, it's set to False, meaning the output is buffered.

Here are some examples of how to use the print() function:

```Python
# Printing a simple message
print("Hello, world!")

# Printing multiple values
name = "Alice"
age = 30
print("Name:", name, "Age:", age)

# Changing the separator
print("One", "Two", "Three", sep=', ')

# Changing the end character
print("This is on the same line as the previous line.", end=' ')

# Flushing the output
print("This will be printed immediately.", flush=True)

```
```python
@satishkarki ➜ /workspaces/HarvardCS50 (main) $ python hello.py
Hello, world!
Name: Alice Age: 30
One, Two, Three
This is on the same line as the previous line. This will be printed immediately.
@satishkarki ➜ /workspaces/HarvardCS50 (main) $ 

```



