
# Lesson 3: Data Types and Formats

These are some notes for [Data Carpentry](http://www.datacarpentry.org)'s tutorial [*Data Analysis and Visualization in Python*](http://www.datacarpentry.org/python-ecology-lesson/).  The web page for this lesson can be found [here](http://www.datacarpentry.org/python-ecology-lesson/03-data-types-and-format).

## Goal

> Learn how to deal with different data types

## Numerical Data Types

There are two main types of numerical data in Python:

* **Floating Point** number (or **`float`**): a number which **can** have a **fractional part**, i.e. something **after the decimal** point:
    * `1.0, 3.25, -7536.3`;
* **Integer** number (or **`int`**): a number which **cannot** have a **fractional part**, i.e. **nothing** after the decimal point:
    * `1, -2, 1177325`.

Note:

* Sometimes you'll see **32** or **64** in the name of the numeric data type.
    * That's to say how much **memory** -- how many **digits** -- the computer allocates for each number.
* If Pandas sees **one** column entry is floating point, it'll assign **all entries** to the floating point data type to **avoid losing precision**.

## Character Data Types

We also have the following important Python data type:

* **`string`**: a data type which can hold **characters** of **any sort**.
    * By "characters" we mean **letters**, **punctuation**, and **spaces**, like
        * `'w', 'NASA', 'a ska-style drum solo'`.
    * But we also mean **digits** when they're used as **text**:
        * `'Dec. 7, 1941', 'my 12th birthday', '3.14'`.
        * You can **not do math** with strings.

Pandas and Python **terminology differs**:

Pandas and base Python use slightly different names for data types. More on this is in the table below:

| **Pandas Type** | **Native Python Type** | **Description** |
| :-- | :-- | :-- |
| `object` | `string` | The most general dtype. Will be assigned to your column if column has mixed types (numbers and strings). |
| `int64` | `int` | Numeric characters. 64 refers to the memory allocated to hold this character. |
| `float64` | `float` | Numeric characters with decimals. If a column contains numbers and NaNs(see below), pandas will default to float64, in case your missing value has a decimal. |
| `datetime64, timedelta[ns]` | N/A (but see the [datetime](http://doc.python.org/2/library/datetime.html) module in Python's standard library) | Values meant to hold time data. Look into these for time series experiments. |

## Checking Data Formats

Let's check our data...


```python
import pandas as pd
```


```python
# note that pd.read_csv is used because we imported pandas as pd
#surveys_df = pd.read_csv("https://ndownloader.figshare.com/files/2292172")
surveys_df = pd.read_csv('data/surveys.csv')
```


```python
type(surveys_df)
```




    pandas.core.frame.DataFrame



What data type is a single column?


```python
surveys_df['sex'].dtype
```




    dtype('O')



`'O'` stands for Python **`object`** data, i.e. **`string`s**.

Try another column...


```python
surveys_df['record_id'].dtype
```




    dtype('int64')



Or simply **all columns** at once...


```python
surveys_df.dtypes
```




    record_id            int64
    month                int64
    day                  int64
    year                 int64
    plot_id              int64
    species_id          object
    sex                 object
    hindfoot_length    float64
    weight             float64
    dtype: object



## Working with `int`s & `float`s


```python
5 + 5
```




    10




```python
24 - 7
```




    17



Basic math operations are the same as usual...

But be careful with division...


```python
# division of integers in Python 3
5/9
```




    0.5555555555555556




```python
# so-called "integer division" in Python 3
5//9
```




    0




```python
13/6
```




    2.1666666666666665




```python
13//6
```




    2



Convert between types...


```python
# convert a to integer
a = 7.83
int(a)
```




    7




```python
# convert to float
b = 7
float(b)
```




    7.0



## Working with Survey Data

### Converting Types

Let's try converting an **entire column**...


```python
# convert the record_id field from an integer to a float
surveys_df['record_id'] = surveys_df['record_id'].astype('float64')
surveys_df['record_id'].dtype
```




    dtype('float64')



Try the weight values...


```python
surveys_df['weight'].astype('int')
```


    ---------------------------------------------------------------------------

    ValueError                                Traceback (most recent call last)

    <ipython-input-16-10a3faf50c4d> in <module>()
    ----> 1 surveys_df['weight'].astype('int')
    

    /Users/bobtodd/anaconda/lib/python3.5/site-packages/pandas/core/generic.py in astype(self, dtype, copy, raise_on_error, **kwargs)
       3052         # else, only a single dtype is given
       3053         new_data = self._data.astype(dtype=dtype, copy=copy,
    -> 3054                                      raise_on_error=raise_on_error, **kwargs)
       3055         return self._constructor(new_data).__finalize__(self)
       3056 


    /Users/bobtodd/anaconda/lib/python3.5/site-packages/pandas/core/internals.py in astype(self, dtype, **kwargs)
       3187 
       3188     def astype(self, dtype, **kwargs):
    -> 3189         return self.apply('astype', dtype=dtype, **kwargs)
       3190 
       3191     def convert(self, **kwargs):


    /Users/bobtodd/anaconda/lib/python3.5/site-packages/pandas/core/internals.py in apply(self, f, axes, filter, do_integrity_check, consolidate, **kwargs)
       3054 
       3055             kwargs['mgr'] = self
    -> 3056             applied = getattr(b, f)(**kwargs)
       3057             result_blocks = _extend_blocks(applied, result_blocks)
       3058 


    /Users/bobtodd/anaconda/lib/python3.5/site-packages/pandas/core/internals.py in astype(self, dtype, copy, raise_on_error, values, **kwargs)
        459                **kwargs):
        460         return self._astype(dtype, copy=copy, raise_on_error=raise_on_error,
    --> 461                             values=values, **kwargs)
        462 
        463     def _astype(self, dtype, copy=False, raise_on_error=True, values=None,


    /Users/bobtodd/anaconda/lib/python3.5/site-packages/pandas/core/internals.py in _astype(self, dtype, copy, raise_on_error, values, klass, mgr, **kwargs)
        502 
        503                 # _astype_nansafe works fine with 1-d only
    --> 504                 values = _astype_nansafe(values.ravel(), dtype, copy=True)
        505                 values = values.reshape(self.shape)
        506 


    /Users/bobtodd/anaconda/lib/python3.5/site-packages/pandas/types/cast.py in _astype_nansafe(arr, dtype, copy)
        529 
        530         if np.isnan(arr).any():
    --> 531             raise ValueError('Cannot convert NA to integer')
        532     elif arr.dtype == np.object_ and np.issubdtype(dtype.type, np.integer):
        533         # work around NumPy brokenness, #1987


    ValueError: Cannot convert NA to integer


**Problem:** the converter encountered `NaN` (**N**ot **a** **N**umber) and doesn't know how to convert that to a number.

`NaN`s can arise from

* data that was **uninterpretable**, or simply
* **empty cells** in a spreadsheet.

**NB:** if we **average without replacing** `NaN`s, Pandas skips those values.


```python
surveys_df['weight'].mean()
```




    42.672428212991356



### Missing Values

The **big issue:**

> what does **missing data** mean?

Does it mean

* **unreadable** by the computer?
* **not entered** by the person collecting the data?

When data is missing, should we

* leave the cell **blank**?
* insert a **`0`**?
* insert **`-9999`**?  (This is the practice in Remote Sensing.)
    * This could make for some **odd averaging**...

**Good practice:**

> Put in something that clearly **screams "Data is missing!"**

### Finding `NaN`s

Find out **how many `NaN`s** in the **weight** column...


```python
len(surveys_df[pd.isnull(surveys_df.weight)])
```




    3266



So how many rows **do have** weight values?


```python
len(surveys_df[surveys_df.weight > 0])
```




    32283



**Substitute** `NaN`s with `0`.


```python
df1 = surveys_df.copy()
# fill all NaN values with 0
df1['weight'] = df1['weight'].fillna(0)
```

**NB:** Note the **effect on the average**.

As `NaN`s these entries were skipped.  Now they're **counted**.


```python
df1['weight'].mean()
```




    38.751976145601844



We can, in principle, **substitute anything**.

Like the average over all values, as below...


```python
df1['weight'] = surveys_df['weight'].fillna(surveys_df['weight'].mean())
```

**Upshot:**

> be careful **how you handle missing data**, since that can **affect analysis**.


```python

```
