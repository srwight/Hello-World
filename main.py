'''
Hello World

Topics:
- Data Types: str
- Functions
- - The print() function

Welcome to python!

Python stores data in variables. These variables can hold data in many forms. It can store integers (int), decimals (float), boolean values (bool), and strings (str). These are its 'primitive' data types. It can also store more complex combinations of data, as well as methods to interact with the data, but for now we are going to focus on these four data types.

integer:      int       positive, negative, or zero. 
                        Does not include any fractional portion
decimals:     float     positive, negative, or zero. 
                        Always includes a decimal. 2. is a float.
boolean:      bool      True or False ; Must be capitalized.
strings:      str       strings of characters. 
                        Denoted by pairs of single or double quotes
                        immutable - cannot be changed; BUT
                        can be reassigned

Storing data isn't enough, though. You also need a way to tell the computer how to interact with the data. This is done through functions.

In this lesson, we focus on one specific function: print()
and one specific data type: a string.

Consider the following line of code:

'''

print('Welcome to Python')

'''
It should be fairly straightforward what this will do. That's one of the beautiful things about Python - It's designed to be as human-readable as possible.

But let's break down what's happening.

You have two things going.
1: print()
print is a function. A function has a name (print), and it has arguments enclosed in a pair of parentheses.
2: 'Welcome to Python'
'Welcome to Python' is a string. We know this because it is denoted with quotes - in this case, single quotes.

'Welcome to Python' is an argument being passed to the function print.

So with that line of code, we are telling the computer to find the function called print, and to run it using the string 'Welcome to Python' as its only argument.

Add a call to the print function below. You will need to do so outside of the three single quotes; triple quotes are a way to denote a special type of string which will be ignored by python (and which is why I am using them to set my comments aside.)
'''
# YOUR CODE HERE

# END YOUR CODE
'''
In the above example, we passed a string directly to the function. But we can also send print a variable. Consider the following code:

# Add a triple (single) quote above this line.

my_string = 'Some day my prints will come!'
print(my_string)

# Add a triple (single) quote below this line.

What do you suppose happens when you run that code?
Add the triple-quotes where indicated and see if you were right.

Notice that when we pass my_string to the print function, we do not put it in quotes. What would happen if we did? Feel free to experiment.

### SPECIAL CHARACTERS ###

There are a few special characters to know about in strings. each of them is denoted with a backslash (\) character followed by a single letter or character. They are as follows:

\n      new line
\r      return to the beginning of this line
\t      tab
\\      include an actual backslash in your string
\'      include a quote mark in your string
        (this is only necessary if your string is denoted by single quotes.)
\"      include a double quote mark in your string
        (this is only necessary if your string is denoted by double quotes.)

There may be a few others, but these are the ones I run across most often.

These can be quite useful. Consider the following:

# Add a triple (single) quote above this line.

print('Every\nword\nis\non\na\nnew\nline!')

print('\t\t1\t\t2\t\t3')
print('a\t\t1a\t\t2a\t\t3a')
print('b\t\t1b\t\t2b\t\t3b')

print('The \'print\' function is pretty useful!')

print('C:\\Windows\\Program Files\\')

# Add a triple (single) quote below this line.

### MULTIPLE ARGUMENTS ###

The print function can be passed multiple arguments at once, separated by commas. Not all functions can do this, but print can. By default, each argument is printed separated by a space. 

# Add a triple (single) quote above this line.

print('Hello','there,','how','are','you?')

a = 'this?'
b = 'Can'
c = 'unscramble'
d = 'Python'

print(b,d,c,a)

# Add a triple (single) quote below this line.

### KEYWORD ARGUMENTS ###

There are four keyword arguments you can pass to print. They are passed as a key-value pair in the format:

key=value

These keyword arguments are:
end       a string added to the end of your print
sep       the string output between arguments
file      where the print is sent - defaults to the screen
flush     if True, forcibly push everything from the
          buffer to its destination.

You will rarely ever use 'file' or 'flush'. 'end' and 'sep', though can be very useful. We've already discussed the default value for 'sep'. What do you suppose is the default value for 'end'?

What do you suppose the output will be for the following?

# Add a triple (single) quote above this line.

print(a,b,c,d, sep='')

print(b, end='\t')
print(d, end='\t')
print(c, end='\t')
print(a)

# Add a triple (single) quote below this line.

Play around a little. Write a few print statements. Use variables if you want. Have fun!

'''