
# Lesson 7 Notes: Errors and Exceptions

These are some notes for [Software Carpentry](https://software-carpentry.org/)'s tutorial [*Programming with Python*](http://swcarpentry.github.io/python-novice-inflammation/).  The web page for this lesson can be found [here](http://swcarpentry.github.io/python-novice-inflammation/07-errors/).

## The Goal

> Read & analyze error messages

## Traceback Example


```python
import errors_01
```


    ---------------------------------------------------------------------------

    ImportError                               Traceback (most recent call last)

    <ipython-input-1-56eb787402eb> in <module>()
    ----> 1 import errors_01
    

    ImportError: No module named 'errors_01'


**NB: Software Carpentry (we) needs to fix this example!** Where's the package?

Two points:

* Look at the **arrows**
    * They point to the lines of code **where things went wrong**
* Look at the **last line**
    * That tells you what **kind** of error you have

## Pro-Tip: Google It!

A simple logic of analysis:

* Look at the arrows
    * Did you write those functions?
        * **Yes:** check that you wrote them correctly.
        * **No:** cut and paste the last line into Google
            * Chances are, you're not the only person to wonder about this error

Benefits:

* [Stack Exchange](http://stackexchange.com/), in particular [Stack Overflow](http://stackoverflow.com/), will probably have answered a similar question
* You'll find a **variety of programming levels**
    * ... usually something close to but slightly above your level, so **you'll learn to program better**

### Important Point: Get Used to Errors!

> If you're doing something you haven't done before -- which you *should*, because you're doing *research* -- then you will **constantly make errors**

## Syntax Errors

Syntax errors in Python are the same as they are in English:

> It there's an error in syntax, it means what you wrote is **jibberish.**

That is, the program can't make sense of what you wrote.

This may happen because of

* misspellings
* forgetting proper punctuation
* incorrect keywords
* forgetting to indent
* etc.


```python
def some_function()
    msg = "Hello, World!"
    print(msg)
        return msg
```


      File "<ipython-input-3-1c4d77edaaf1>", line 1
        def some_function()
                           ^
    SyntaxError: invalid syntax



The compiler **shows us where the error is**: no colon.


```python
# fix the colon issue
def some_function():
    msg = "Hello, World!"
    print(msg)
        return msg
```


      File "<ipython-input-4-11104524affb>", line 5
        return msg
        ^
    IndentationError: unexpected indent



Goofball!  What's that extra indentation for?!?!

Note: the computer is **more specific** this time, calling this an `IndentationError`.

### Watch out:  Tabs != Spaces

Things may look like they have the same indentation, but if they **mix tabs and spaces** this will give an error.

## Variable Name Errors


```python
# variable not previously defined
print(a)
```


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-5-167691ebc2be> in <module>()
          1 # variable not previously defined
    ----> 2 print(a)
    

    NameError: name 'a' is not defined


### Common Causes


```python
# you meant to use a string
print(hello) # instead of print('hello')
```


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-6-150ac216b9ef> in <module>()
          1 # you meant to use a string
    ----> 2 print(hello) # instead of print('hello')
    

    NameError: name 'hello' is not defined



```python
# forget to create a variable before using it
for number in range(10):  # where's the 'count = 0' before the loop?
    count = count + number
print("The count is:", count)
```


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-7-e04f308a32e9> in <module>()
          1 # forget to create a variable before using it
          2 for number in range(10):  # where's the 'count = 0' before the loop?
    ----> 3     count = count + number
          4 print("The count is:", count)


    NameError: name 'count' is not defined



```python
# typo
Count = 0 # note: capitalized
for number in range(10):
    count = count + number
print("The count is:", count)
```


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-8-e519a917147a> in <module>()
          2 Count = 0 # note: capitalized
          3 for number in range(10):
    ----> 4     count = count + number
          5 print("The count is:", count)


    NameError: name 'count' is not defined


## Index Errors


```python
# index goes out of range

letters = ['a', 'b', 'c']

for i in range(4):
    print('letter is: ', letters[i])
```

    letter is:  a
    letter is:  b
    letter is:  c



    ---------------------------------------------------------------------------

    IndexError                                Traceback (most recent call last)

    <ipython-input-10-15479f037226> in <module>()
          4 
          5 for i in range(4):
    ----> 6     print('letter is: ', letters[i])
    

    IndexError: list index out of range



```python
# index went too far
len(letters)
```




    3



## File Errors

Common errors:

* no file
* wrong permissions


```python
# maybe wrong path
file_handle = open('my_file.txt', 'r')
```


    ---------------------------------------------------------------------------

    FileNotFoundError                         Traceback (most recent call last)

    <ipython-input-13-2a58c0aa41d6> in <module>()
          1 # maybe wrong path
    ----> 2 file_handle = open('my_file.txt', 'r')
    

    FileNotFoundError: [Errno 2] No such file or directory: 'my_file.txt'


You might also open with one permission but try to use another:

```python
file_handle = open('my_file.txt', 'w') # opened with write permissions
file_handle.read() # trying to read
```


```python

```
