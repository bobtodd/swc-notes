
# Lesson 6 Notes: Creating Functions

These are some notes for [Software Carpentry](https://software-carpentry.org/)'s tutorial [*Programming with Python*](http://swcarpentry.github.io/python-novice-inflammation/).  The web page for this lesson can be found [here](http://swcarpentry.github.io/python-novice-inflammation/06-func/).

## The Goal

> How to package repeated code into functions

## Assessment: Where are we so far?

Why our code is ***slick:***

* We can perform multiple checks and graph multiple files.

Why our code ***sucks:***

* We have to write everything longhand each time we want to use it.

## Functions: Holding onto things you might want to do again...

Suppose you want to convert a temperature measurement from degrees Fahrenheit to Kelvin.  It's in the nature of temperature measurements that

> if you need to measure the temperature once, you probably need to measure it **many times**.

So you'll probably need to convert lots of measurements.  Let's package the process into a function.

A function consists of a few basic parts:

* definition keyword,
* function name,
* parameters,
* return value.


```python
def fahr_to_kelvin(temp):
    return ((temp - 32)*(5/9)) + 273.15
```

Analysis:

* `def`: keyword
* `fahr_to_kelvin`: name
* `temp`: parameter
* `((temp - 32)*(5/9)) + 273.15`: return value

Use it.


```python
print('freezing point of water:', fahr_to_kelvin(32))
print('boiling point of water:', fahr_to_kelvin(212))
```

    freezing point of water: 273.15
    boiling point of water: 373.15


Understand it.

* `fahr_to_kelvin(32))`
    * Now we've set `temp = 32`.
    * Then `temp - 32` becomes 0.
    * Hence `((temp - 32)*(5/9)) + 273.15` becomes 273.15.
    * So `fahr_to_kelvin(32))` returns the value 273.15.

## Aside: Integer vs. Floating-Point Division


```python
# Python 3
print(5/9)
```

    0.5555555555555556



```python
# Python 3
print(5//9)
```

    0


In Python 3:

* `5/9` gives the answer as a **real number** (decimal);
* `5//9` gives the **whole-number part** of the answer (discarding the remainder).

In Python 2:

* `5/9` gives the **whole-number part** (discarding the remainder);
* You need to **convert to floating-point numbers** for real number division:
    * `float(5)/9`
    * `5/float(9)`
    * `5.0/9`
    * `5/9.0`

## Composition: Functions within Functions

There's no prohibition to using a function within a function.

Let's convert Kelvin to degrees Celsius.


```python
def kelvin_to_celsius(temp_k):
    return temp_k - 273.15
```

**Note:** it's helpful to name parameters in a way that reminds you of how the function should work.  Here think about why we write `temp_k` instead of `temp`.


```python
print('absolute zero in Celsius:', kelvin_to_celsius(0.0))
```

    absolute zero in Celsius: -273.15


Let's convert degrees Fahrenheit to degress Celsius.


```python
def fahr_to_celsius(temp_f):
    temp_k = fahr_to_kelvin(temp_f)
    result = kelvin_to_celsius(temp_k)
    return result
```


```python
print('freezing point of water in Celsius:', fahr_to_celsius(32.0))
```

    freezing point of water in Celsius: 0.0


Template:

* Break down process into bite-sized chunks.
* Package those chunks into functions.
* Reuse chunks as needed.
* Build up bigger chunks from smaller chunks.

## Cleaning Up: Let's Chunkerize Our Code!

Our method of creating figures is something we need to use again and again.  It makes for a nice, self-contained part of the process.  Put it in a function.


```python
def analyze(filename):

    data = numpy.loadtxt(fname=filename, delimiter=',')

    fig = matplotlib.pyplot.figure(figsize=(10.0, 3.0))

    axes1 = fig.add_subplot(1, 3, 1)
    axes2 = fig.add_subplot(1, 3, 2)
    axes3 = fig.add_subplot(1, 3, 3)

    axes1.set_ylabel('average')
    axes1.plot(numpy.mean(data, axis=0))

    axes2.set_ylabel('max')
    axes2.plot(numpy.max(data, axis=0))

    axes3.set_ylabel('min')
    axes3.plot(numpy.min(data, axis=0))

    fig.tight_layout()
    matplotlib.pyplot.show()
```

We also needed to check for problems in each file, and that process too was repetitive.  Put it in a function.


```python
def detect_problems(filename):

    data = numpy.loadtxt(fname=filename, delimiter=',')

    if numpy.max(data, axis=0)[0] == 0 and numpy.max(data, axis=0)[20] == 20:
        print('Suspicious looking maxima!')
    elif numpy.sum(numpy.min(data, axis=0)) == 0:
        print('Minima add up to zero!')
    else:
        print('Seems OK!')
```

Now let's try the analysis again.


```python
import numpy
import matplotlib.pyplot
import glob
```


```python
filenames = sorted(glob.glob('data/inflammation*.csv'))
```

Now the logic of each loop is **much** clearer.


```python
for f in filenames[:3]:
    print(f)
    analyze(f)
    detect_problems(f)
```

    data/inflammation-01.csv



![png](06-notes_files/06-notes_37_1.png)


    Suspicious looking maxima!
    data/inflammation-02.csv



![png](06-notes_files/06-notes_37_3.png)


    Suspicious looking maxima!
    data/inflammation-03.csv



![png](06-notes_files/06-notes_37_5.png)


    Minima add up to zero!


## Testing

Let's center a dataset on a different value.


```python
# When possible, let the structure of the program document what's happening

def center(data, desired):
    # Find the natural center and write everything as offsets from that
    offsets = data - numpy.mean(data)
    
    # pick a new center and add the offsets from there
    shifted = offsets + desired
    return shifted
```

Check to see if it works.  *Use data you **understand**!*


```python
z = numpy.zeros((2,2))
```


```python
print(z)
```

    [[ 0.  0.]
     [ 0.  0.]]



```python
print(center(z, 3))
```

    [[ 3.  3.]
     [ 3.  3.]]



```python
print(center(z, -8))
```

    [[-8. -8.]
     [-8. -8.]]


That looks sensible.

Try it on our real data.


```python
data = numpy.loadtxt(fname='data/inflammation-01.csv', delimiter=',')
print(center(data, 0))
```

    [[-6.14875 -6.14875 -5.14875 ..., -3.14875 -6.14875 -6.14875]
     [-6.14875 -5.14875 -4.14875 ..., -5.14875 -6.14875 -5.14875]
     [-6.14875 -5.14875 -5.14875 ..., -4.14875 -5.14875 -5.14875]
     ..., 
     [-6.14875 -5.14875 -5.14875 ..., -5.14875 -5.14875 -5.14875]
     [-6.14875 -6.14875 -6.14875 ..., -6.14875 -4.14875 -6.14875]
     [-6.14875 -6.14875 -5.14875 ..., -5.14875 -5.14875 -6.14875]]


Huh?

Who knows what the answers should look like?

Investigate some salient data...


```python
print('original min, mean, and max are:', numpy.min(data), numpy.mean(data), numpy.max(data))
```

    original min, mean, and max are: 0.0 6.14875 20.0



```python
centered = center(data, 0)
```


```python
print('min, mean, and max of centered data are:', numpy.min(centered), numpy.mean(centered), numpy.max(centered))
```

    min, mean, and max of centered data are: -6.14875 2.84217094304e-16 13.85125


Think about it:

* the mean was roughly 6.1
    * now the minimum is roughly -6.1
* the mean is now almost 0
    * that's what we were trying to center around


```python
print('std dev before and after:', numpy.std(data), numpy.std(centered))
```

    std dev before and after: 4.61383319712 4.61383319712


The standard deviation **looks** the same before and after.  But sometimes it's hard to tell... look at the difference.


```python
print('difference in standard deviations before and after:', numpy.std(data) - numpy.std(centered))
```

    difference in standard deviations before and after: 0.0


## Documentation

**Code** should be commented.

But **functions** have a special additional documentation: **doc(umentation) string**.

The docstring

* comes right after the line defining the function name;
* is triple-quoted.


```python
def center(data, desired):
    '''Return a new array containing the original data centered around the desired value.'''
    
    # Find the natural center and write everything as offsets from that
    offsets = data - numpy.mean(data)
    
    # pick a new center and add the offsets from there
    shifted = offsets + desired
    return shifted
```

Use the docstring as **true documentation**, e.g. with **example usage**.


```python
def center(data, desired):
    '''Return a new array containing the original data centered around the desired value.
    Example: center([1, 2, 3], 0) => [-1, 0, 1]'''
    
    # Find the natural center and write everything as offsets from that
    offsets = data - numpy.mean(data)
    
    # pick a new center and add the offsets from there
    shifted = offsets + desired
    return shifted
```

With triple-quotes you can use multiple lines of text in the docstring.

Now the `help()` function lets you access the docstring.


```python
help(center)
```

    Help on function center in module __main__:
    
    center(data, desired)
        Return a new array containing the original data centered around the desired value.
        Example: center([1, 2, 3], 0) => [-1, 0, 1]
    


## Default Parameters

We've been writing...


```python
data = numpy.loadtxt(fname='data/inflammation-01.csv', delimiter=',')
```

We can omit `fname=`


```python
data = numpy.loadtxt('data/inflammation-01.csv', delimiter=',')
```

But not `delimiter=`


```python
data = numpy.loadtxt('data/inflammation-01.csv', ',')
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-37-4231adbb0eae> in <module>()
    ----> 1 data = numpy.loadtxt('data/inflammation-01.csv', ',')
    

    /Users/bobtodd/anaconda/lib/python3.5/site-packages/numpy/lib/npyio.py in loadtxt(fname, dtype, comments, delimiter, converters, skiprows, usecols, unpack, ndmin)
        873     try:
        874         # Make sure we're dealing with a proper dtype
    --> 875         dtype = np.dtype(dtype)
        876         defconv = _getconv(dtype)
        877 


    TypeError: data type "," not understood


Let's rewrite our function `center()` using keywords with default values.


```python
def center(data, desired=0.0):
    '''Return a new array containing the original data centered around the desired value.
    Example: center([1, 2, 3], 0) => [-1, 0, 1]'''
    
    # Find the natural center and write everything as offsets from that
    offsets = data - numpy.mean(data)
    
    # pick a new center and add the offsets from there
    shifted = offsets + desired
    return shifted
```

Test it out.


```python
test_data = numpy.zeros((2, 2))
```


```python
print(test_data)
```

    [[ 0.  0.]
     [ 0.  0.]]



```python
print(center(test_data, 3))
```

    [[ 3.  3.]
     [ 3.  3.]]



```python
more_data = 5 + numpy.zeros((2, 2))
```


```python
print(more_data)
```

    [[ 5.  5.]
     [ 5.  5.]]



```python
# now we don't need to give a second parameter
# if we omit it, it uses the default 0.0
print(center(more_data))
```

    [[ 0.  0.]
     [ 0.  0.]]


Matching passed values to parameters...


```python
def display(a=1, b=2, c=3):
    print('a:', a, 'b:', b, 'c:', c)
```


```python
print('no parameters:')
display()
```

    no parameters:
    a: 1 b: 2 c: 3



```python
print('one parameter:')
display(55)
```

    one parameter:
    a: 55 b: 2 c: 3



```python
print('two parameters:')
display(55, 66)
```

    two parameters:
    a: 55 b: 66 c: 3


Parameters are

* matched left to right
* given their default value if nothing matches

To override this, give the parameter name.


```python
print('only setting the value of c')
display(c=77)
```

    only setting the value of c
    a: 1 b: 2 c: 77


Compare the `numpy.loadtxt()` docstring.  There's only one parameter, `fname`, without a default value.

The second parameter passed, if the parameter name isn't given, will be assigned to the parameter `dype`.  That's what `','` was assigned to in our calls where we didn't write `delimiter=`.


```python
help(numpy.loadtxt)
```

    Help on function loadtxt in module numpy.lib.npyio:
    
    loadtxt(fname, dtype=<class 'float'>, comments='#', delimiter=None, converters=None, skiprows=0, usecols=None, unpack=False, ndmin=0)
        Load data from a text file.
        
        Each row in the text file must have the same number of values.
        
        Parameters
        ----------
        fname : file or str
            File, filename, or generator to read.  If the filename extension is
            ``.gz`` or ``.bz2``, the file is first decompressed. Note that
            generators should return byte strings for Python 3k.
        dtype : data-type, optional
            Data-type of the resulting array; default: float.  If this is a
            structured data-type, the resulting array will be 1-dimensional, and
            each row will be interpreted as an element of the array.  In this
            case, the number of columns used must match the number of fields in
            the data-type.
        comments : str or sequence, optional
            The characters or list of characters used to indicate the start of a
            comment;
            default: '#'.
        delimiter : str, optional
            The string used to separate values.  By default, this is any
            whitespace.
        converters : dict, optional
            A dictionary mapping column number to a function that will convert
            that column to a float.  E.g., if column 0 is a date string:
            ``converters = {0: datestr2num}``.  Converters can also be used to
            provide a default value for missing data (but see also `genfromtxt`):
            ``converters = {3: lambda s: float(s.strip() or 0)}``.  Default: None.
        skiprows : int, optional
            Skip the first `skiprows` lines; default: 0.
        usecols : sequence, optional
            Which columns to read, with 0 being the first.  For example,
            ``usecols = (1,4,5)`` will extract the 2nd, 5th and 6th columns.
            The default, None, results in all columns being read.
        unpack : bool, optional
            If True, the returned array is transposed, so that arguments may be
            unpacked using ``x, y, z = loadtxt(...)``.  When used with a structured
            data-type, arrays are returned for each field.  Default is False.
        ndmin : int, optional
            The returned array will have at least `ndmin` dimensions.
            Otherwise mono-dimensional axes will be squeezed.
            Legal values: 0 (default), 1 or 2.
        
            .. versionadded:: 1.6.0
        
        Returns
        -------
        out : ndarray
            Data read from the text file.
        
        See Also
        --------
        load, fromstring, fromregex
        genfromtxt : Load data with missing values handled as specified.
        scipy.io.loadmat : reads MATLAB data files
        
        Notes
        -----
        This function aims to be a fast reader for simply formatted files.  The
        `genfromtxt` function provides more sophisticated handling of, e.g.,
        lines with missing values.
        
        .. versionadded:: 1.10.0
        
        The strings produced by the Python float.hex method can be used as
        input for floats.
        
        Examples
        --------
        >>> from io import StringIO   # StringIO behaves like a file object
        >>> c = StringIO("0 1\n2 3")
        >>> np.loadtxt(c)
        array([[ 0.,  1.],
               [ 2.,  3.]])
        
        >>> d = StringIO("M 21 72\nF 35 58")
        >>> np.loadtxt(d, dtype={'names': ('gender', 'age', 'weight'),
        ...                      'formats': ('S1', 'i4', 'f4')})
        array([('M', 21, 72.0), ('F', 35, 58.0)],
              dtype=[('gender', '|S1'), ('age', '<i4'), ('weight', '<f4')])
        
        >>> c = StringIO("1,0,2\n3,0,4")
        >>> x, y = np.loadtxt(c, delimiter=',', usecols=(0, 2), unpack=True)
        >>> x
        array([ 1.,  3.])
        >>> y
        array([ 2.,  4.])
    


## Readability

If your function **executes**, then it's **machine readable**.

But the machine **doesn't write** programs.  **People** do.

Make your code **human readable**.


```python
# Bad example
def s(p):
    a = 0
    for v in p:
        a += v
    m = a / len(p)
    d = 0
    for v in p:
        d += (v - m) * (v - m)
    return numpy.sqrt(d / (len(p) - 1))
```

In the above

* the name doesn't tell you what it does;
* the variable names don't give any clue to what they represent.


```python
# Good example of the same function
def std_dev(sample):
    sample_sum = 0
    for value in sample:
        sample_sum += value

    sample_mean = sample_sum / len(sample)

    sum_squared_devs = 0
    for value in sample:
        sum_squared_devs += (value - sample_mean) * (value - sample_mean)

    return numpy.sqrt(sum_squared_devs / (len(sample) - 1))
```


```python

```
