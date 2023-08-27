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


# removing the leading and trailing whitespaces and capitalize the first letter
name1=input("Enter your Full Name\n")
name1 =name1.strip().title()
print (f"Hi {name1}, I just removed space from your name.")