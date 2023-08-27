# Harvard CS50 Lecture Note
## Lecture 0: Functions, Variables 

### Print Function
The print() function in Python is used to display text or other data to the console. You can use it to output messages, variables, or the results of calculations. Here's the basic syntax of the print() function:

> print(value1, value2, ..., sep=' ', end='\n', file=sys.stdout, flush=False)

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
#Output
@satishkarki ➜ /workspaces/HarvardCS50 (main) $ python hello.py
Hello, world!
Name: Alice Age: 30
One, Two, Three
This is on the same line as the previous line. This will be printed immediately.
@satishkarki ➜ /workspaces/HarvardCS50 (main) $ 
```

### F-String
F-strings allow you to embed expressions inside string literals, using curly braces {}
```python
name = "Alice"
age = 30

# Using an f-string to format the output
formatted_text = "My name is {} and I am {} years old.".format(name, age)
print(f"My name is {name} and I am {age} years old.")

# Output
My name is Alice and I am 30 years old.
```
**Special Cases**
```python
z = 1000000
formatted_z = f"{z:,}"
print(formatted_z)  # Output: "1,000,000"

z = 3.14159
formatted_z = f"{z:.2f}"
print(formatted_z)  # Output: "3.14"
```
### strip()
The strip() method in Python is used to remove leading and trailing whitespace (including spaces, tabs, and newline characters) from a string.
> string.strip([characters])

* string: This is the original string from which you want to remove whitespace.
* characters (optional): This parameter allows you to specify a set of characters that should be stripped from the string. If you provide it, strip() will remove any leading or trailing characters that are present in the specified set.

Here are some examples of how to use the strip() method:
```python
text = "   Hello, World!   "

# Basic usage to remove leading and trailing spaces
stripped_text = text.strip()
print(stripped_text)  # Output: "Hello, World!"

# Stripping specific characters
text = "###Python###"
stripped_text = text.strip("#")
print(stripped_text)  # Output: "Python"

# Stripping specific characters from both ends
text = "##***Python***##"
stripped_text = text.strip("#*")
print(stripped_text)  # Output: "Python"

# Strip newline characters
text = "\nThis is a test string.\n"
stripped_text = text.strip()
print(stripped_text)  # Output: "This is a test string."

# Strip multiple whitespace characters
text = "  \t   This has tabs and spaces  \n"
stripped_text = text.strip()
print(stripped_text)  # Output: "This has tabs and spaces"
```
Keep in mind that strip() only removes leading and trailing characters; it does not remove characters in the middle of the string. If you want to remove specific characters from anywhere in the string, you can use the replace() method or regular expressions.

### title()
Title case means that the first character of each word in the string is capitalized, while all other characters are in lowercase.
```python
text = "this is a sample string"

# Using title() to convert the string to title case
title_case_text = text.title()

print(title_case_text)  # Output: "This Is A Sample String"
```
### split()
The split() method in Python is used to split a string into a list of substrings based on a specified delimiter.
> string.split([separator[, maxsplit]])

* string: This is the original string that you want to split.
* separator (optional): This is the delimiter by which the string will be split. If you don't provide a separator, whitespace characters (spaces, tabs, and newline characters) are used as the default separator.
* maxsplit (optional): This parameter specifies the maximum number of splits to perform. By default, it's set to -1, which means all occurrences of the separator will be split. If you provide a positive integer value, it will limit the number of splits.

Here are some examples of how to use the split() method:
```python
text = "apple,banana,cherry"

# Splitting by comma (default separator)
fruits = text.split(',')
print(fruits)  # Output: ['apple', 'banana', 'cherry']

# Splitting by space
sentence = "This is a sample sentence."
words = sentence.split()
print(words)  # Output: ['This', 'is', 'a', 'sample', 'sentence.']

# Splitting by a custom separator
data = "John;Doe;30;New York"
info = data.split(';')
print(info)  # Output: ['John', 'Doe', '30', 'New York']

# Limiting the number of splits
text = "apple,banana,cherry,dates,figs"
limited_fruits = text.split(',', 2)
print(limited_fruits)  # Output: ['apple', 'banana', 'cherry,dates,figs']
```
### round()
The round() function in Python is used to round a number to a specified number of decimal places.
> round(number[, ndigits])

```python
# Rounding to the nearest whole number
num1 = 3.14159
rounded_num1 = round(num1)
print(rounded_num1)  # Output: 3

# Rounding to a specific number of decimal places
num2 = 2.71828
rounded_num2 = round(num2, 2)
print(rounded_num2)  # Output: 2.72

# Rounding negative numbers
num3 = -5.6789
rounded_num3 = round(num3, 1)
print(rounded_num3)  # Output: -5.7
```
### def()
```python
def function_name(parameters):
    # Function body
    # Code that performs the desired task
    return result  # Optional, if the function should return a value
```
```python
def hello(to="world"):
    """
    This function greets the specified person (or "world" by default).
    """
    return f"Hello, {to}!"

# Calling the function without an argument
message = hello()
print(message)  # Output: "Hello, world!"

# Calling the function with an argument
message = hello("Alice")
print(message)  # Output: "Hello, Alice!"
```
**def main()**
```python
def main():
    # Your program's logic goes here
    print("Hello, World!")

# This condition checks if the script is being run directly (not imported as a module)
if __name__ == "__main__":
    main()
```
Here's how this script works:

1. When you run this script directly, for example, by executing python script.py in the command line, Python starts executing the code from the top to the bottom.

2. Python encounters the def main(): line and defines a function named main. However, the code inside the main() function is not executed yet; Python only defines the function.

3. Python continues to the if __name__ == "__main__": condition. At this point, Python checks the __name__ variable. If the script is being run directly as the main program, Python sets __name__ to "__main__". If the script is being imported as a module into another script, __name__ will be set to the name of the script/module.

4. In this case, if you're running the script directly, the condition if __name__ == "__main__": evaluates to True because __name__ is "__main__" when the script is run directly.

5. When the condition is True, Python executes the code inside the block under if __name__ == "__main__":. In this example, it calls the main() function, and you see the message "This code is inside the main() function." printed to the console.

This mechanism allows you to structure your Python scripts in a way that separates code meant to be executed when the script is run as the main program from code meant to be used when the script is imported as a module.

For example, if you import this script into another script using import script, the main() function won't be automatically executed. Instead, you can call it explicitly if needed, and any other code outside the main() function won't be executed until you call it.

In summary, the if __name__ == "__main__": condition is a way to distinguish whether a Python script is being run directly or imported as a module, allowing you to control the execution of specific code blocks accordingly.