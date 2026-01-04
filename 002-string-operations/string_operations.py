# String Operations and f-strings
# Date: December 2024

# Using f-strings for string formatting
new_user = 'Ramesh'
new_app = 'Photoshop'

print(f'Once upon a time, there was a {new_app} User named {new_user}')
print(f'Erik wasted months on soul-draining tasks in {new_app}')
print(f'Until one day {new_user} said: Enough!')
print(f'And by accident he discovered that he could automate his {new_app} work with python')
print(f'But {new_user} knew nothing about python.')
print(f'And so, {new_user} has begun his programming journey.')

print('-' * 50)

# Using string.replace() method
text = """
Once upon a time, there was a Revit User named Erik
Erik wasted months on soul-draining tasks in Revit
Until one day Erik said: Enough!
And by accident he discovered that he could automate his Revit work with python
But Erik knew nothing about python.
And so, Erik has begun his programming journey.
"""
new_text = text.replace('Erik', 'Ramesh')
print(new_text)

print('-' * 50)

# String concatenation
greeting = "Hello "
name = "Alice"
print(greeting + name)

# Different ways to format strings
name = 'John'
print(f'Hello, {name}! Welcome to the adventure game.')  # f-string
print('Hello my name is {}'.format(name))  # .format() method

print('-' * 50)

# Multi-line output tricks
print('Hello')
print('-' * 100)

# String membership testing
message = 'A cat sitting on its tail began to tell a tale about its tail'
print('tail' in message)  # True
print('cat' in message)   # True
print('brick' in message) # False

print('-' * 50)

# String comparison
a = 'Grace Hayden: What I love about my Mahindra XUV700'
b = 'By now, you have no doubt read that the 2026 Toyota HiLux is essentially a major update.'
print('Are the strings equal?', a == b)
print('Are the strings different?', a != b)
