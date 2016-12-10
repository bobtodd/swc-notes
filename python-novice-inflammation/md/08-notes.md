
# Lesson 8 Notes: Defensive Programming

These are some notes for [Software Carpentry](https://software-carpentry.org/)'s tutorial [*Programming with Python*](http://swcarpentry.github.io/python-novice-inflammation/).  The web page for this lesson can be found [here](http://swcarpentry.github.io/python-novice-inflammation/08-defensive/).

## The Goal

> **Save time** in the **long run**: make **the computer** check for problems!

## Assertions: Make Sure Something Is True

In programming, **assume things will go wrong**.

So put in periodic checks of what ***should* be true** if things are running as expected.


```python
numbers = [1.5, 2.3, 0.7, -0.001, 4.4]
total = 0.0
for n in numbers:
    # make sure values are positive
    assert n > 0.0, 'Data should only contain positive values'
    
    # then keep going
    total += n
print('total is:', total)
```


    ---------------------------------------------------------------------------

    AssertionError                            Traceback (most recent call last)

    <ipython-input-1-7f179e18d400> in <module>()
          3 for n in numbers:
          4     # make sure values are positive
    ----> 5     assert n > 0.0, 'Data should only contain positive values'
          6 
          7     # then keep going


    AssertionError: Data should only contain positive values


`assert`'s functionality:

* if `True`: do nothing;
* if `False`: **stop everything**.

Note `assert` has room for a statement to tell you what's going on.

### Types of Assertions

There are three basic types:

* **precondition**: check before you compute;
* **postcondition**: check after you compute;
* **invariant**: always true at a certain point in the code.


```python
def normalize_rectangle(rect):
    '''Normalizes a rectangle so that it is at the origin and 1.0 units long on its longest axis.'''
    assert len(rect) == 4, 'Rectangles must contain 4 coordinates'
    
    # separate out the coordinates for use
    x0, y0, x1, y1 = rect
    
    # x0 should be left of x1
    assert x0 < x1, 'Invalid X coordinates'
    
    # y0 should be below y1
    assert y0 < y1, 'Invalid Y coordinates'
    
    dx = x1 - x0
    dy = y1 - y0
    if dx > dy:
        scaled = float(dx) / dy
        upper_x, upper_y = 1.0, scaled
    else:
        scaled = float(dx) / dy
        upper_x, upper_y = scaled, 1.0
    
    # Make sure the edges are less than 1 unit long
    assert 0 < upper_x <= 1.0, 'Calculated upper X coordinate invalid'
    assert 0 < upper_y <= 1.0, 'Calculated upper Y coordinate invalid'

    return (0, 0, upper_x, upper_y)
```

Preconditions check for bad input...


```python
# missing the fourth coordinate
print(normalize_rectangle( (0.0, 1.0, 2.0) ))
```


    ---------------------------------------------------------------------------

    AssertionError                            Traceback (most recent call last)

    <ipython-input-5-4909e9dbb33f> in <module>()
          1 # missing the fourth coordinate
    ----> 2 print(normalize_rectangle( (0.0, 1.0, 2.0) ))
    

    <ipython-input-2-ad2f8c31df82> in normalize_rectangle(rect)
          1 def normalize_rectangle(rect):
          2     '''Normalizes a rectangle so that it is at the origin and 1.0 units long on its longest axis.'''
    ----> 3     assert len(rect) == 4, 'Rectangles must contain 4 coordinates'
          4 
          5     # separate out the coordinates for use


    AssertionError: Rectangles must contain 4 coordinates



```python
# X axis inverted
print(normalize_rectangle( (4.0, 2.0, 1.0, 5.0) ))
```


    ---------------------------------------------------------------------------

    AssertionError                            Traceback (most recent call last)

    <ipython-input-6-7589de325545> in <module>()
          1 # X axis inverted
    ----> 2 print(normalize_rectangle( (4.0, 2.0, 1.0, 5.0) ))
    

    <ipython-input-2-ad2f8c31df82> in normalize_rectangle(rect)
          7 
          8     # x0 should be left of x1
    ----> 9     assert x0 < x1, 'Invalid X coordinates'
         10 
         11     # y0 should be below y1


    AssertionError: Invalid X coordinates


Postconditions catch bugs...


```python
print(normalize_rectangle( (0.0, 0.0, 1.0, 5.0) ))
```

    (0, 0, 0.2, 1.0)



```python
# wider than tall, i.e. dx > dy
print(normalize_rectangle( (0.0, 0.0, 5.0, 1.0) ))
```


    ---------------------------------------------------------------------------

    AssertionError                            Traceback (most recent call last)

    <ipython-input-8-2c31edf5cdde> in <module>()
          1 # wider than tall, i.e. dx > dy
    ----> 2 print(normalize_rectangle( (0.0, 0.0, 5.0, 1.0) ))
    

    <ipython-input-2-ad2f8c31df82> in normalize_rectangle(rect)
         23     # Make sure the edges are less than 1 unit long
         24     assert 0 < upper_x <= 1.0, 'Calculated upper X coordinate invalid'
    ---> 25     assert 0 < upper_y <= 1.0, 'Calculated upper Y coordinate invalid'
         26 
         27     return (0, 0, upper_x, upper_y)


    AssertionError: Calculated upper Y coordinate invalid


Oops!  We should have written:

```python
if dx > dy:
        scaled = float(dy) / dx  # not float(dx) / dy
        upper_x, upper_y = 1.0, scaled
```

That's an error that's **hard to detect** just by...

* reading...
* checking behavior...

It's much easier to put in `assert` and less time-consuming in the long run.

### Pro-Tips

Some basic points to keep in mind:

* Assertions help **check understanding**.
* **Fail early, fail often.**  Don't wait long between assertions, since that's more code to search for bugs.
* **Turn bugs into tests.** Once you find a bug, fix it and **leave an assertion in its place**.

## Test-Driven Development

> Decide what tests your function must satisfy, then write a function **that will pass those tests.**

Example: `range_overlap()`.  Given several intervals, find their intersection.

What tests should it pass?


```python
assert range_overlap([ (0.0, 1.0) ]) == (0.0, 1.0)
assert range_overlap([ (2.0, 3.0), (2.0, 4.0) ]) == (2.0, 3.0)
assert range_overlap([ (0.0, 1.0), (0.0, 2.0), (-1.0, 1.0) ]) == (0.0, 1.0)
```


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-9-d8be150fbef6> in <module>()
    ----> 1 assert range_overlap([ (0.0, 1.0) ]) == (0.0, 1.0)
          2 assert range_overlap([ (2.0, 3.0), (2.0, 4.0) ]) == (2.0, 3.0)
          3 assert range_overlap([ (0.0, 1.0), (0.0, 2.0), (-1.0, 1.0) ]) == (0.0, 1.0)


    NameError: name 'range_overlap' is not defined


Of course it fails... we haven't written the function yet!

**Bonus:** now we know what our input should look like.

But something's missing: what if they **don't overlap**?

```python
assert range_overlap([ (0.0, 1.0), (5.0, 6.0) ]) == ???
```

We have to **decide how to handle that case**.  Better to decide sooner rather than later.

And what if they **only touch at the endpoints**?

```python
assert range_overlap([ (0.0, 1.0), (1.0, 2.0) ]) == ???
```

**Decide at the beginning:**

* Overlaps must have **non-zero width**
* Return `None` for no overlap

That means we want

```python
assert range_overlap([ (0.0, 1.0), (5.0, 6.0) ]) == None
assert range_overlap([ (0.0, 1.0), (1.0, 2.0) ]) == None
```

Now let's try it...


```python
def range_overlap(ranges):
    '''Return common overlap among a set of [low, high] ranges.'''
    
    # Start somewhere
    lowest = 0.0
    highest = 1.0
    
    # Go through it input intervals
    for (low, high) in ranges:
        
        # if the left end is more to the right than "lowest", choose that
        lowest = max(lowest, low)
        
        # if the right end is more to the left than "highest", choose that
        highest = min(highest, high)
    return (lowest, highest)
```

Rather than check each assertion, **define a test function** that puts `range_overlap()` through its paces.


```python
def test_range_overlap():
    assert range_overlap([ (0.0, 1.0), (5.0, 6.0) ]) == None
    assert range_overlap([ (0.0, 1.0), (1.0, 2.0) ]) == None
    assert range_overlap([ (0.0, 1.0) ]) == (0.0, 1.0)
    assert range_overlap([ (2.0, 3.0), (2.0, 4.0) ]) == (2.0, 3.0)
    assert range_overlap([ (0.0, 1.0), (0.0, 2.0), (-1.0, 1.0) ]) == (0.0, 1.0)
```


```python
test_range_overlap()
```


    ---------------------------------------------------------------------------

    AssertionError                            Traceback (most recent call last)

    <ipython-input-12-cf9215c96457> in <module>()
    ----> 1 test_range_overlap()
    

    <ipython-input-11-5d4cd6fd41d9> in test_range_overlap()
          1 def test_range_overlap():
    ----> 2     assert range_overlap([ (0.0, 1.0), (5.0, 6.0) ]) == None
          3     assert range_overlap([ (0.0, 1.0), (1.0, 2.0) ]) == None
          4     assert range_overlap([ (0.0, 1.0) ]) == (0.0, 1.0)
          5     assert range_overlap([ (2.0, 3.0), (2.0, 4.0) ]) == (2.0, 3.0)


    AssertionError: 


All we know is **the first test fails**.  But that's something...

But notice...

* our choice of `lowest` will get updated...
    * to 0.0, then
    * to 5.0, while
* our choice of `highest` will get updated...
    * to 1.0, then
    * to 1.0.

That'll leave us with an interval (5.0, 1.0), which we don't want.

Maybe we should **initialize** our function's parameters **from the data**, rather than with fixed values...


```python

```
