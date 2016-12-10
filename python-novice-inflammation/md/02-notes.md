
# Lesson 2 Notes: Repeating Actions with Loops

These are some notes for [Software Carpentry](https://software-carpentry.org/)'s tutorial [*Programming with Python*](http://swcarpentry.github.io/python-novice-inflammation/).  The web page for this lesson can be found [here](http://swcarpentry.github.io/python-novice-inflammation/02-loop/).

## The Goal

> Repeat the process of making graphs for each data set.

## Start with the Basics: Iterate through a Word

A `string` is a data collection:

* a collection of characters
* in order.

So access them with an index.


```python
word = 'lead'
```


```python
word[2]
```




    'a'




```python
# the clunky way
print(word[0])
print(word[1])
print(word[2])
print(word[3])
```

    l
    e
    a
    d


### Drawbacks

* scaling:
    * good luck with that for a string that's got 1000 characters!
* fragility:
    * problems if `word` only has 3 characters


```python
word = 'tin'
print(word[0])
print(word[1])
print(word[2])
print(word[3])
```

    t
    i
    n



    ---------------------------------------------------------------------------

    IndexError                                Traceback (most recent call last)

    <ipython-input-4-a51226538da7> in <module>()
          3 print(word[1])
          4 print(word[2])
    ----> 5 print(word[3])
    

    IndexError: string index out of range


### Saving Grace: Loop


```python
word = 'lead'
for char in word:
    print(char)
```

    l
    e
    a
    d



```python
word = 'oxygen'
for char in word:
    print(char)
```

    o
    x
    y
    g
    e
    n


The basic outline:

```python
for variable in collection:
    do_something(variable)
```

Note the ***indentation!***

The process:

* `word = 'tin'`
* `for char in word:`
    * Step 1: `char = 't'`
        * `print(char)`
            * That is, `print('t')`
    * Step 2: `char = 'i'`
        * `print(char)`
            * That is, `print('i')`
    * Step 3: `char = 'n'`
        * `print(char)`
            * That is, `print('n')`
    * No more elements in `word`
        * So `break`, that is, stop the loop

## More Advanced: Updating Variables

An example of using a `for` loop to update a variable.


```python
length = 0
for vowel in 'aeiou':
    length = length + 1
print('There are', length, 'vowels')
```

    There are 5 vowels


Explanation:

* `length = 0`
    * `length` is a container for a number
        * Initial value 0
* `for vowel in 'aeiou':`
    * `'aeiou'` has 5 elements, so this will loop 5 times
    * in each step, `vowel` takes a new value
    * `length = length + 1`
        * This gets executed every time `vowel` takes a new value, so 5 times
        * Step 1:
            * `length = 0`, then add 1
                * 0 + 1 = 1
                * Save in `length` again
                * So now `length = 1`
        * Step 2:
            * `length = 1`, then add 1
                * 1 + 1 = 2
                * Save in `length` again
                * So now `length = 2`
        * Step 3:
            * `length = 2`, then add 1
                * 2 + 1 = 3
                * Save in `length` again
                * So now `length = 3`
        * Step 4:
            * `length = 3`, then add 1
                * 3 + 1 = 4
                * Save in `length` again
                * So now `length = 4`
        * Step 5:
            * `length = 4`, then add 1
                * 4 + 1 = 5
                * Save in `length` again
                * So now `length = 5`
    * no more vowels in `'aeiou'`, so stop the loop
* The last value `length` has is 5


### Take Care: Variable Persistence

Check this out:


```python
letter = 'z'
for letter in 'abc':
    print(letter)
print('after the loop, letter is', letter)
```

    a
    b
    c
    after the loop, letter is c



```python
for other_letter in 'abc':
    print(other_letter)
print('after the loop, other_letter is', other_letter)
```

    a
    b
    c
    after the loop, other_letter is c


The variable used for the iteration exists *after* (outside) the loop.  You can still use it.

## Pro-Tip: Don't Reinvent the Wheel

Actually Python already has a function for this.  And it's *fast!*


```python
print(len('aeiou'))
```

    5



```python

```
