
# Lesson 5 Notes: Making Choices

These are some notes for [Software Carpentry](https://software-carpentry.org/)'s tutorial [*Programming with Python*](http://swcarpentry.github.io/python-novice-inflammation/).  The web page for this lesson can be found [here](http://swcarpentry.github.io/python-novice-inflammation/05-cond/).

## The Goal

> * Use conditionals
> * Evaluate expressions with `and` or `or`

## Conditionals

Check if some condition holds:

* **true**: do one thing;
* **false**: do something else.

That's it.


```python
num = 37

if num > 100:
    print('greater')
else:
    print('not greater')

print('done')
```

    not greater
    done


### Features

#### `else` Is Optional


```python
num = 53

print('before conditional...')

# Nothing happens if condition not satisfied and no 'else'
if num > 100:
    print('53 is greater than 100')

print('... after conditional')
```

    before conditional...
    ... after conditional


#### Chaining `if`s: `elif`

Logic:

* if A is true, do something;
    * else
        * if B is true, do something
            * else
                * if C is true, do something
                    * else
                        * ...

Flatten this out:

* if A is true, do something; else
* if B is true, do something; else
* if C is true, do something; else
* ...


```python
num = -3

if num > 0:
    print(num, "is positive")
elif num == 0:
    print(num, "is zero")
else:
    print(num, "is negative")
```

    -3 is negative


##### Equal Signs

Note:

* `=` means "assignment";
* `==` means "equality".

#### Use `and` for Combined Conditions


```python
if (1 > 0) and (-1 > 0):
    print('both parts are true')
else:
    print('at least one part is false')
```

    at least one part is false


#### Use `or` for Alternative Conditions


```python
if (1 < 0) or (-1 < 0):
    print('at least one test is true')
```

    at least one test is true


## Application: Check for Suspicious Data

We want to avoid data where

* the maxima rise linearly by day,
    * i.e. the first day is 0 and day 20 is 20;
* the minima are consistently 0,
    * i.e. the sum of all the minima is 0.


```python
import numpy
```


```python
# Check first file
data = numpy.loadtxt(fname='data/inflammation-01.csv', delimiter=',')

if numpy.max(data, axis=0)[0] == 0 and numpy.max(data, axis=0)[20] == 20:
    print('Suspicious looking maxima!')
elif numpy.sum(numpy.min(data, axis=0)) == 0:
    print('Minima add up to zero!')
else:
    print('Seems OK!')
```

    Suspicious looking maxima!



```python
# Check third file
data = numpy.loadtxt(fname='data/inflammation-03.csv', delimiter=',')

if numpy.max(data, axis=0)[0] == 0 and numpy.max(data, axis=0)[20] == 20:
    print('Suspicious looking maxima!')
elif numpy.sum(numpy.min(data, axis=0)) == 0:
    print('Minima add up to zero!')
else:
    print('Seems OK!')
```

    Minima add up to zero!



```python

```
