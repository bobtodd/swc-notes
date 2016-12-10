
# Lesson 3 Notes: Storing Multiple Values in Lists

These are some notes for [Software Carpentry](https://software-carpentry.org/)'s tutorial [*Programming with Python*](http://swcarpentry.github.io/python-novice-inflammation/).  The web page for this lesson can be found [here](http://swcarpentry.github.io/python-novice-inflammation/03-lists/).

## The Goal

> Create, index, and slice lists.

## Basics: Form & Content

Lists keep a group of values: use **square** brackets, separate by commas.


```python
odds = [1, 3, 5, 7]
print('odds are:', odds)
```

    odds are: [1, 3, 5, 7]


Access with indices.


```python
# Note the cool notation "-1" for last element
# (i.e. "1 from the back")
print('first and last:', odds[0], odds[-1])
```

    first and last: 1 7


It's a collection -- so ***loop!***


```python
for number in odds:
    print(number)
```

    1
    3
    5
    7


## A Nicety: Lists Are *Mutable*

*Mutable* means you can change it.  We can muck around with lists.


```python
names = ['Newton', 'Darwing', 'Turing'] # typo in Darwin's name
print('names is originally:', names)
names[1] = 'Darwin' # correct the name
print('final value of names:', names)
```

    names is originally: ['Newton', 'Darwing', 'Turing']
    final value of names: ['Newton', 'Darwin', 'Turing']


Not so much with strings -- they're *immutable*.


```python
name = 'Darwin'
name[0] = 'd'
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-5-cb94b05a418a> in <module>()
          1 name = 'Darwin'
    ----> 2 name[0] = 'd'
    

    TypeError: 'str' object does not support item assignment


### Be Careful: You Might Change Something Behind the Scenes

Suppose two variables refer to the same data.  If you use one variable to change the data, that will change the other variable as well.


```python
list1 = [1, 2, 3]
list2 = list1
```


```python
list1[1] = 0
```


```python
print(list1)
```

    [1, 0, 3]



```python
print(list2)
```

    [1, 0, 3]


The value of `list2` got changed even though we didn't touch it!

## Lists Can Contain Anything

Lists can contain any data type, including other lists.


```python
x = [['pepper', 'zucchini', 'onion'],
     ['cabbage', 'lettuce', 'garlic'],
     ['apple', 'pear', 'banana']]
```

The first (0th) element of the list `x` is itself a list.


```python
print(x[0])
```

    ['pepper', 'zucchini', 'onion']


The first (0th) element of that list is a string.


```python
print(x[0][0])
```

    pepper


## Things You Can Do to Lists

Add things on the tail end.


```python
odds.append(11)
print('odds after adding a value:', odds)
```

    odds after adding a value: [1, 3, 5, 7, 11]


Get rid of a particular element.


```python
del odds[0]
print('odds after removing the first element:', odds)
```

    odds after removing the first element: [3, 5, 7, 11]


Reverse the order.


```python
odds.reverse()
print('odds after reversing:', odds)
```

    odds after reversing: [11, 7, 5, 3]


### Careful with Copies!

Be careful with the warning above.  When you make copies of lists, modifications of one list can propagate to the copy.


```python
odds = [1, 3, 5, 7]
primes = odds
primes += [2]
print('primes:', primes)
print('odds:', odds)
```

    primes: [1, 3, 5, 7, 2]
    odds: [1, 3, 5, 7, 2]


Use `list()` to make a completely independent copy.


```python
odds = [1, 3, 5, 7]
primes = list(odds)
primes += [2]
print('primes:', primes)
print('odds:', odds)
```

    primes: [1, 3, 5, 7, 2]
    odds: [1, 3, 5, 7]


## The Real Fun: Slicing!

Access ranges using the `:`-notation for indices.


```python
binomial_name = "Drosophila melanogaster"
group = binomial_name[0:10]
print("group:", group)

species = binomial_name[11:24]
print("species:", species)

chromosomes = ["X", "Y", "2", "3", "4"]
autosomes = chromosomes[2:5]
print("autosomes:", autosomes)

last = chromosomes[-1]
print("last:", last)
```

    group: Drosophila
    species: melanogaster
    autosomes: ['2', '3', '4']
    last: 4


If you want to start at the beginning, don't bother with the first index.


```python
date = "Monday 4 January 2016"
day = date[0:6]
print("Using 0 to begin range:", day)
day = date[:6]
print("Omitting beginning index:", day)
```

    Using 0 to begin range: Monday
    Omitting beginning index: Monday


If you want to go out to the very end, skip the last index.


```python
months = ["jan", "feb", "mar", "apr", "may", "jun", "jul", "aug", "sep", "oct", "nov", "dec"]
sond = months[8:12]
print("With known last position:", sond)
sond = months[8:len(months)]
print("Using len() to get last entry:", sond)
sond = months[8:]
print("Omitting ending index:", sond)
```

    With known last position: ['sep', 'oct', 'nov', 'dec']
    Using len() to get last entry: ['sep', 'oct', 'nov', 'dec']
    Omitting ending index: ['sep', 'oct', 'nov', 'dec']



```python

```
