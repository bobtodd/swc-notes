
# Lesson 0: Short Introduction to Programming in Python

These are some notes as I go through [Data Carpentry](http://www.datacarpentry.org)'s tutorial [*Data Analysis and Visualization in Python*](http://www.datacarpentry.org/python-ecology-lesson/), which I plan to use as my teaching example for Instructor Training Checkout.  The web page for this lesson can be found [here](http://www.datacarpentry.org/python-ecology-lesson/00-short-introduction-to-Python).

## Setup

Before we get started, go to [this page](http://www.datacarpentry.org/python-ecology-lesson/) to make sure you have a Python setup that will work for these lessons.  The upshot is

> install [Anaconda](https://www.continuum.io/downloads).

We'll be using the [Jupyter Notebook](http://jupyter.org/) for most of this.  So make sure you have a **modern web browser**: e.g. Chrome, Firefox, Safari.

Also make sure you have these **data files**:

* [`surveys.csv`](https://ndownloader.figshare.com/files/2292172),
* [`species.csv`](https://ndownloader.figshare.com/files/3299483).

Personally I save these in a subfolder called `data/`.

Now let's get started!

## Goal

> Familiarize ourselves with the **basic structures** of Python

## Advantages of Python

Python's main advantages:

* **Open Source**
* **Cross-platform**
* **"Batteries Included"** -- libraries for common tasks
* Multiple **programming paradigms**
* **Large community** -- i.e. you can get lots of help!

## Environment: Interpreter

Two basic ways to use Python:

1. **Python interpreter:** Best.  Calculator.  Ever!
2. **Executing scripts:** save programs in files `my_script.py`.

Interpreter invoked from the command line:

```bash
$ python
Python 3.5.2 | packaged by conda-forge | (default, Jul 26 2016, 01:37:38) 
[GCC 4.2.1 Compatible Apple LLVM 6.0 (clang-600.0.54)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> 2 + 2
4
>>> print("Hello, World")
Hello, World
>>> exit()
```

Running a script from the command line:

```bash
$ python my_script.py
```

## Data Types: Built-In

### Strings

The Python `string` data type holds **characters**.

Note that **numbers can be characters**: with the band name "Blink 183", you're **not trying to do math** with the numbers.  They're just text.

We enclose strings in **single** or **double quotes**.

Examples:

* `"Dollywood"`
* `'US3'`
* `'If it ain\'t broke, don\'t fix it.'`
    * Note `[space]` is a character
    * Note that the apostrophe in "ain't" looks like a single quote, so we need to use `\` to **escape** it (tell the computer it's not a quote)

### Integers (Ints)

The Python `int` data type holds **integers**, i.e. positive or negative **whole numbers**.

These numbers are **not text**.  Rather they're used for **math**.

You write an `int` as you would any whole number:

* `42`
* `-7`
* `1146`
    * Note: **no commas** to group digits

### Floating Point Numbers (Floats)

The Python `float` data type holds **decimal numbers**, i.e. **real numbers**.

Again, these are **not text**, but rather used for **math**.

We always write `float`s using the **decimal point** and **not fraction** notation:

* `1.25`
    * Not 1 1/4 or 5/4
* `.333`
    * Also `0.33`
    * You **can't write 1/3**, so you have to **pick a level of precision**
* `-73.065`
    * Negative numbers too

## Variables

Python variables are **names you can assign** to quantities you **want to reuse**.

The variable names are **strings of text**: they can contain letters and digits.

You **assign** a value to a variable using the equal sign `=`, technically the **assignment operator**.

### Intuition

The basic idea:

* **variable** <==> **bucket**
* **assigned value** <==> **contents**

### Examples


```python
text = "Data Carpentry"
number = 42
pi_value = 3.1415
```

But note:

> the variable **assumes the type** of the data it stores!

So above:

* `text` is a **string**
* `number` is an **int**
* `pi_value` is a **float**

In the Python interpreter, **write the variable** and hit `[return]` to display its value:

```python
>>> text
"Data Carpentry"
```

In a program, use **`print()`**:


```python
print(text)
```

    Data Carpentry



```python
print(number)
```

    42


## Operators

Python has the usual **calculator** operators `+, -, *, /`, plus some **new ones**.


```python
3 + 2
```




    5




```python
3 - 2
```




    1




```python
3 * 2
```




    6




```python
3 / 2 # regular division
```




    1.5




```python
3 // 2 # integer divisions
```




    1




```python
3 % 2 # modulo
```




    1




```python
13 % 5
```




    3




```python
3 ** 2 # power
```




    9



We also have **comparison operators**: `<, >, ==, !=, <=, >=`.


```python
3 > 4
```




    False



And **logical operators**: `and, or, not`.


```python
True and True
```




    True




```python
True and False
```




    False




```python
True or False
```




    True




```python
not True
```




    False



## Sequential Data Types

### Lists

The Python `list` data structure holds a **collection** of elements **in order**.  Access each one by an **index**.


```python
stuff = [1, 2, 3, 'yesterday']
```


```python
stuff[1]
```




    2




```python
stuff[0]
```




    1




```python
stuff[-1]
```




    'yesterday'



Use a **`for` loop** to access elements one at a time:


```python
for thing in stuff:
    print(thing)
```

    1
    2
    3
    yesterday


**NB:** note the **indentation**

**Append** an element to the end of the list:


```python
stuff.append(4)
print(stuff)
```

    [1, 2, 3, 'yesterday', 4]


**NB:** note the use of **dot notation** to use methods associated with an **object**.

**Note to self:** the use of "object" comes out of nowhere.  We'll have to see if this leads to complications...

To find out available methods, get **`help()`**:


```python
help(stuff)
```

    Help on list object:
    
    class list(object)
     |  list() -> new empty list
     |  list(iterable) -> new list initialized from iterable's items
     |  
     |  Methods defined here:
     |  
     |  __add__(self, value, /)
     |      Return self+value.
     |  
     |  __contains__(self, key, /)
     |      Return key in self.
     |  
     |  __delitem__(self, key, /)
     |      Delete self[key].
     |  
     |  __eq__(self, value, /)
     |      Return self==value.
     |  
     |  __ge__(self, value, /)
     |      Return self>=value.
     |  
     |  __getattribute__(self, name, /)
     |      Return getattr(self, name).
     |  
     |  __getitem__(...)
     |      x.__getitem__(y) <==> x[y]
     |  
     |  __gt__(self, value, /)
     |      Return self>value.
     |  
     |  __iadd__(self, value, /)
     |      Implement self+=value.
     |  
     |  __imul__(self, value, /)
     |      Implement self*=value.
     |  
     |  __init__(self, /, *args, **kwargs)
     |      Initialize self.  See help(type(self)) for accurate signature.
     |  
     |  __iter__(self, /)
     |      Implement iter(self).
     |  
     |  __le__(self, value, /)
     |      Return self<=value.
     |  
     |  __len__(self, /)
     |      Return len(self).
     |  
     |  __lt__(self, value, /)
     |      Return self<value.
     |  
     |  __mul__(self, value, /)
     |      Return self*value.n
     |  
     |  __ne__(self, value, /)
     |      Return self!=value.
     |  
     |  __new__(*args, **kwargs) from builtins.type
     |      Create and return a new object.  See help(type) for accurate signature.
     |  
     |  __repr__(self, /)
     |      Return repr(self).
     |  
     |  __reversed__(...)
     |      L.__reversed__() -- return a reverse iterator over the list
     |  
     |  __rmul__(self, value, /)
     |      Return self*value.
     |  
     |  __setitem__(self, key, value, /)
     |      Set self[key] to value.
     |  
     |  __sizeof__(...)
     |      L.__sizeof__() -- size of L in memory, in bytes
     |  
     |  append(...)
     |      L.append(object) -> None -- append object to end
     |  
     |  clear(...)
     |      L.clear() -> None -- remove all items from L
     |  
     |  copy(...)
     |      L.copy() -> list -- a shallow copy of L
     |  
     |  count(...)
     |      L.count(value) -> integer -- return number of occurrences of value
     |  
     |  extend(...)
     |      L.extend(iterable) -> None -- extend list by appending elements from the iterable
     |  
     |  index(...)
     |      L.index(value, [start, [stop]]) -> integer -- return first index of value.
     |      Raises ValueError if the value is not present.
     |  
     |  insert(...)
     |      L.insert(index, object) -- insert object before index
     |  
     |  pop(...)
     |      L.pop([index]) -> item -- remove and return item at index (default last).
     |      Raises IndexError if list is empty or index is out of range.
     |  
     |  remove(...)
     |      L.remove(value) -> None -- remove first occurrence of value.
     |      Raises ValueError if the value is not present.
     |  
     |  reverse(...)
     |      L.reverse() -- reverse *IN PLACE*
     |  
     |  sort(...)
     |      L.sort(key=None, reverse=False) -> None -- stable sort *IN PLACE*
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes defined here:
     |  
     |  __hash__ = None
    


Also **`dir()`**...


```python
dir(stuff)
```




    ['__add__',
     '__class__',
     '__contains__',
     '__delattr__',
     '__delitem__',
     '__dir__',
     '__doc__',
     '__eq__',
     '__format__',
     '__ge__',
     '__getattribute__',
     '__getitem__',
     '__gt__',
     '__hash__',
     '__iadd__',
     '__imul__',
     '__init__',
     '__iter__',
     '__le__',
     '__len__',
     '__lt__',
     '__mul__',
     '__ne__',
     '__new__',
     '__reduce__',
     '__reduce_ex__',
     '__repr__',
     '__reversed__',
     '__rmul__',
     '__setattr__',
     '__setitem__',
     '__sizeof__',
     '__str__',
     '__subclasshook__',
     'append',
     'clear',
     'copy',
     'count',
     'extend',
     'index',
     'insert',
     'pop',
     'remove',
     'reverse',
     'sort']



Methods with **double underscores** are special.  For example **`__add__`** defines how the `+` operator works.

### Tuples

A Python `tuple` is like a `list`, but it is **immutable**.


```python
a_tuple = ('Bob', 'Stephen', 'Alison')
a_list = ['Bob', 'Stephen', 'Alison']
```

#### Exercise


```python
a_list[2] = 'Erika'
print(a_list)
```

    ['Bob', 'Stephen', 'Erika']



```python
a_tuple[2] = 'Erika'
print(a_tuple)
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-32-d7c492b39603> in <module>()
    ----> 1 a_tuple[2] = 'Erika'
          2 print(a_tuple)


    TypeError: 'tuple' object does not support item assignment


## Dictionaries

The Python dictionary (`dict`) collects **pairs of items**.  We have terms for the elements of the pair:

* **key**: the thing you think of as the "index" or the "locator" for the data you want;
* **value**: the actual data you want.

The key can be any **number or string**.  The keys are **not ordered**.


```python
to_remember = {"first": "Teddy", 1: "Betty", '1': [1,2,3]}
```


```python
to_remember["first"]
```




    'Teddy'




```python
to_remember['1'].append(4)
```


```python
to_remember
```




    {1: 'Betty', 'first': 'Teddy', '1': [1, 2, 3, 4]}




```python
to_remember[1].append(4)
```


    ---------------------------------------------------------------------------

    AttributeError                            Traceback (most recent call last)

    <ipython-input-37-21f864a27250> in <module>()
    ----> 1 to_remember[1].append(4)
    

    AttributeError: 'str' object has no attribute 'append'


**NB**: a number like `1` and a string like `'1'` are **completely different** and so yield **different keys**.

Looping over dictionaries requires some thought.


```python
for key, value in to_remember.items():
    print(key, "->", value)
```

    1 -> Betty
    first -> Teddy
    1 -> [1, 2, 3, 4]


or...


```python
for key in to_remember.keys():
    print(key, "->", to_remember[key])
```

    1 -> Betty
    first -> Teddy
    1 -> [1, 2, 3, 4]


### Exercise

Change the value assigned to one of the keys in the dictionary you created.

## Functions

Functions allow you to **reuse code**.  You can **pass arguments** -- that is, values or data -- and the function will **repeat the operations** on the new data.

Key points:

* start with the keyword **`def`**
* **indent** the body
* use the keyword **`return`** to output the result


```python
def add_function(a, b):
    result = a + b
    return result
```


```python
z = add_function(20, 22)
print(z)
```

    42



```python

```
