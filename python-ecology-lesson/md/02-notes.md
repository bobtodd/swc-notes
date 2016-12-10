
# Lesson 2: Indexing, Slicing and Subsetting DataFrames in Python

These are some notes for [Data Carpentry](http://www.datacarpentry.org)'s tutorial [*Data Analysis and Visualization in Python*](http://www.datacarpentry.org/python-ecology-lesson/).  The web page for this lesson can be found [here](http://www.datacarpentry.org/python-ecology-lesson/02-index-slice-subset).

## Goal

> Select **subsets** of DataFrames

## Load the Data

If we just want the data **in memory**, we can use a trick to load it **straight from the web**.


```python
# first make sure pandas is loaded
import pandas as pd

# read in the survey csv
surveys_df = pd.read_csv("https://ndownloader.figshare.com/files/2292172")

# or if the internet is giving you a hard time,
# try the local file
surveys_df = pd.read_csv('data/surveys.csv')
```

But of course the **advisability** of the method **depends** on the file size and Internet speed.

And the data might have **changed** in between downloads...

## Selecting Data with Labels

When columns have labels, we can access the column using **square brackets** and the **title string**.


```python
surveys_df['species_id']
```




    0         NL
    1         NL
    2         DM
    3         DM
    4         DM
    5         PF
    6         PE
    7         DM
    8         DM
    9         PF
    10        DS
    11        DM
    12        DM
    13        DM
    14        DM
    15        DM
    16        DS
    17        PP
    18        PF
    19        DS
    20        DM
    21        NL
    22        DM
    23        SH
    24        DM
    25        DM
    26        DM
    27        DM
    28        PP
    29        DS
            ... 
    35519     SF
    35520     DM
    35521     DM
    35522     DM
    35523     PB
    35524     OL
    35525     OT
    35526     DO
    35527     US
    35528     PB
    35529     OT
    35530     PB
    35531     DM
    35532     DM
    35533     DM
    35534     DM
    35535     DM
    35536     DM
    35537     PB
    35538     SF
    35539     PB
    35540     PB
    35541     PB
    35542     PB
    35543     US
    35544     AH
    35545     AH
    35546     RM
    35547     DO
    35548    NaN
    Name: species_id, dtype: object



We can also use the title as an **attribute**.


```python
surveys_df.species_id
```




    0         NL
    1         NL
    2         DM
    3         DM
    4         DM
    5         PF
    6         PE
    7         DM
    8         DM
    9         PF
    10        DS
    11        DM
    12        DM
    13        DM
    14        DM
    15        DM
    16        DS
    17        PP
    18        PF
    19        DS
    20        DM
    21        NL
    22        DM
    23        SH
    24        DM
    25        DM
    26        DM
    27        DM
    28        PP
    29        DS
            ... 
    35519     SF
    35520     DM
    35521     DM
    35522     DM
    35523     PB
    35524     OL
    35525     OT
    35526     DO
    35527     US
    35528     PB
    35529     OT
    35530     PB
    35531     DM
    35532     DM
    35533     DM
    35534     DM
    35535     DM
    35536     DM
    35537     PB
    35538     SF
    35539     PB
    35540     PB
    35541     PB
    35542     PB
    35543     US
    35544     AH
    35545     AH
    35546     RM
    35547     DO
    35548    NaN
    Name: species_id, dtype: object



If we save the column to a variable, the variable has **type Series**.


```python
surveys_species = surveys_df['species_id']
type(surveys_species)
```




    pandas.core.series.Series



### Exercise

1. What happens if you pass a list containing multiple column names?
    ```python
    # select the species and plot columns from the DataFrame
    surveys_df[['species_id', 'plot_id']]
    ```
2. What happens if you flip the order?
    ```python
    # what happens when you flip the order?
    surveys_df[['plot_id', 'species_id']]
    ```
3. What if you misspell the column name?
    ```python
    #what happens if you ask for a column that doesn't exist?
    surveys_df['speciess']
    ```

## Slicing

Slicing in DataFrames derives from slicing in Python `list`s.

### Slicing Lists

When slicing Python `list`s, you give the **start point** and the **end point + 1** separated by a **colon**.

**Remember:** Python indices **start at 0**.


```python
# Create a list of numbers:
a = [1,2,3,4,5]
```


```python
a[1:4]
```




    [2, 3, 4]




```python
a[-1]
```




    5



#### Exercise

1. What value does `a[0]` return?
2. How about this: `a[5]`?
3. Or `a[len(a)]`?
4. In the example above, calling `a[5]` returns an error. Why is that?

### Slicing DataFrame Rows

Slicing in Pandas DataFrames works **the same** as Python `list` slicing, but we're **slicing rows**.  That is, we can **select rows** by **slicing**.

The **notation is** (essentially) **the same.**


```python
# select 1st, 2nd, 3rd rows
surveys_df[0:3]
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>record_id</th>
      <th>month</th>
      <th>day</th>
      <th>year</th>
      <th>plot_id</th>
      <th>species_id</th>
      <th>sex</th>
      <th>hindfoot_length</th>
      <th>weight</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>7</td>
      <td>16</td>
      <td>1977</td>
      <td>2</td>
      <td>NL</td>
      <td>M</td>
      <td>32.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>7</td>
      <td>16</td>
      <td>1977</td>
      <td>3</td>
      <td>NL</td>
      <td>M</td>
      <td>33.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>7</td>
      <td>16</td>
      <td>1977</td>
      <td>2</td>
      <td>DM</td>
      <td>F</td>
      <td>37.0</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
</div>




```python
# select 1st 5 rows
surveys_df[:5]
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>record_id</th>
      <th>month</th>
      <th>day</th>
      <th>year</th>
      <th>plot_id</th>
      <th>species_id</th>
      <th>sex</th>
      <th>hindfoot_length</th>
      <th>weight</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>7</td>
      <td>16</td>
      <td>1977</td>
      <td>2</td>
      <td>NL</td>
      <td>M</td>
      <td>32.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>7</td>
      <td>16</td>
      <td>1977</td>
      <td>3</td>
      <td>NL</td>
      <td>M</td>
      <td>33.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>7</td>
      <td>16</td>
      <td>1977</td>
      <td>2</td>
      <td>DM</td>
      <td>F</td>
      <td>37.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4</td>
      <td>7</td>
      <td>16</td>
      <td>1977</td>
      <td>7</td>
      <td>DM</td>
      <td>M</td>
      <td>36.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5</td>
      <td>7</td>
      <td>16</td>
      <td>1977</td>
      <td>3</td>
      <td>DM</td>
      <td>M</td>
      <td>35.0</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
</div>




```python
# select last row
surveys_df[-1:]
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>record_id</th>
      <th>month</th>
      <th>day</th>
      <th>year</th>
      <th>plot_id</th>
      <th>species_id</th>
      <th>sex</th>
      <th>hindfoot_length</th>
      <th>weight</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>35548</th>
      <td>35549</td>
      <td>12</td>
      <td>31</td>
      <td>2002</td>
      <td>5</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
</div>



#### Assigning Values

Before we make changes, let's **copy our data**.


```python
# copy the surveys dataframe so we don't modify the original DataFrame
surveys_copy = surveys_df
```

Now use **assignment** over **slices**.


```python
# set the first three rows of data in the DataFrame to 0
surveys_copy[0:3] = 0
```

Compare.


```python
surveys_copy.head()
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>record_id</th>
      <th>month</th>
      <th>day</th>
      <th>year</th>
      <th>plot_id</th>
      <th>species_id</th>
      <th>sex</th>
      <th>hindfoot_length</th>
      <th>weight</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4</td>
      <td>7</td>
      <td>16</td>
      <td>1977</td>
      <td>7</td>
      <td>DM</td>
      <td>M</td>
      <td>36.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5</td>
      <td>7</td>
      <td>16</td>
      <td>1977</td>
      <td>3</td>
      <td>DM</td>
      <td>M</td>
      <td>35.0</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
</div>




```python
surveys_df.head()
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>record_id</th>
      <th>month</th>
      <th>day</th>
      <th>year</th>
      <th>plot_id</th>
      <th>species_id</th>
      <th>sex</th>
      <th>hindfoot_length</th>
      <th>weight</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4</td>
      <td>7</td>
      <td>16</td>
      <td>1977</td>
      <td>7</td>
      <td>DM</td>
      <td>M</td>
      <td>36.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5</td>
      <td>7</td>
      <td>16</td>
      <td>1977</td>
      <td>3</td>
      <td>DM</td>
      <td>M</td>
      <td>35.0</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
</div>



**Crap!**  We **modified the original data!**

## Referencing vs. Copying

When we write

```python
pd.read_csv("https://ndownloader.figshare.com/files/2292172")
```

we are creating an **object in memory**.

When we write

```python
# read in the survey csv
surveys_df = pd.read_csv("https://ndownloader.figshare.com/files/2292172")
```

we are applying the **label** `surveys_df` to **that object**.  Now we can **reference** the object **via the label**.

### The Subtlety

When we write

```python
surveys_copy = surveys_df
```

we are creating a **new label**, `surveys_copy`, for the **same object**.

**The Upshot:**

> whether we modify **one label or the other**, either way the **object itself gets modified**.

That is, modify `surveys_copy` or `surveys_df` and **both get modified**.

**The Way Out**: Python `copy()`.

This function **duplicates the object** in memory.


```python
surveys_df = pd.read_csv("https://ndownloader.figshare.com/files/2292172")
surveys_copy= surveys_df.copy()
```

Now `surveys_df` and `surveys_copy` refer to **different objects**.

## Row-and-Column Slicing

Pandas has a couple ways of locating data by **column and row**.  But there are some subtle differences.

### Using `.iloc`

With `.iloc` ("**i**nteger **loc**ation") you can use "the usual" numerical indexing.


```python
surveys_df.head()
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>record_id</th>
      <th>month</th>
      <th>day</th>
      <th>year</th>
      <th>plot_id</th>
      <th>species_id</th>
      <th>sex</th>
      <th>hindfoot_length</th>
      <th>weight</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>7</td>
      <td>16</td>
      <td>1977</td>
      <td>2</td>
      <td>NL</td>
      <td>M</td>
      <td>32.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>7</td>
      <td>16</td>
      <td>1977</td>
      <td>3</td>
      <td>NL</td>
      <td>M</td>
      <td>33.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>7</td>
      <td>16</td>
      <td>1977</td>
      <td>2</td>
      <td>DM</td>
      <td>F</td>
      <td>37.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4</td>
      <td>7</td>
      <td>16</td>
      <td>1977</td>
      <td>7</td>
      <td>DM</td>
      <td>M</td>
      <td>36.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5</td>
      <td>7</td>
      <td>16</td>
      <td>1977</td>
      <td>3</td>
      <td>DM</td>
      <td>M</td>
      <td>35.0</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
</div>




```python
surveys_df.iloc[3,4]
```




    7




```python
surveys_df.iloc[1:4, 3:6]
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>year</th>
      <th>plot_id</th>
      <th>species_id</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1</th>
      <td>1977</td>
      <td>3</td>
      <td>NL</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1977</td>
      <td>2</td>
      <td>DM</td>
    </tr>
    <tr>
      <th>3</th>
      <td>1977</td>
      <td>7</td>
      <td>DM</td>
    </tr>
  </tbody>
</table>
</div>



**NB:** in a slice, the **last index** is **not included** with `iloc`.

### Using `.loc`

In the DataFrame `.loc` method all parameters refer to **position**.  That means you can use

* **titles** such as **column names**, or
* **integers**, but
    * they refer to **names** and **not order**.


```python
surveys_df.loc[[0, 10], :]
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>record_id</th>
      <th>month</th>
      <th>day</th>
      <th>year</th>
      <th>plot_id</th>
      <th>species_id</th>
      <th>sex</th>
      <th>hindfoot_length</th>
      <th>weight</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>7</td>
      <td>16</td>
      <td>1977</td>
      <td>2</td>
      <td>NL</td>
      <td>M</td>
      <td>32.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>10</th>
      <td>11</td>
      <td>7</td>
      <td>16</td>
      <td>1977</td>
      <td>5</td>
      <td>DS</td>
      <td>F</td>
      <td>53.0</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
</div>




```python
surveys_df.loc[1:4]
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>record_id</th>
      <th>month</th>
      <th>day</th>
      <th>year</th>
      <th>plot_id</th>
      <th>species_id</th>
      <th>sex</th>
      <th>hindfoot_length</th>
      <th>weight</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>7</td>
      <td>16</td>
      <td>1977</td>
      <td>3</td>
      <td>NL</td>
      <td>M</td>
      <td>33.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>7</td>
      <td>16</td>
      <td>1977</td>
      <td>2</td>
      <td>DM</td>
      <td>F</td>
      <td>37.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4</td>
      <td>7</td>
      <td>16</td>
      <td>1977</td>
      <td>7</td>
      <td>DM</td>
      <td>M</td>
      <td>36.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5</td>
      <td>7</td>
      <td>16</td>
      <td>1977</td>
      <td>3</td>
      <td>DM</td>
      <td>M</td>
      <td>35.0</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
</div>



**NB:** in a slice the **last index** in fact **is** included with `loc`.


```python
# This doesn't work, because the column labels aren't integer
#surveys_df.loc[1:4, 3:6]

# But this does work, because columns have names
surveys_df.loc[1:4, 'year':'species_id']
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>year</th>
      <th>plot_id</th>
      <th>species_id</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1</th>
      <td>1977</td>
      <td>3</td>
      <td>NL</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1977</td>
      <td>2</td>
      <td>DM</td>
    </tr>
    <tr>
      <th>3</th>
      <td>1977</td>
      <td>7</td>
      <td>DM</td>
    </tr>
    <tr>
      <th>4</th>
      <td>1977</td>
      <td>3</td>
      <td>DM</td>
    </tr>
  </tbody>
</table>
</div>



#### Exercise

1. What happens when you type the code below?
    ```python
    surveys_df.loc[[0, 10, 35549], :]
    ```
2. What happens when you type:
    ```python
    surveys_df[0:3]
    surveys_df[:5]
    surveys_df[-1:]
    ```
3. What happens when you call:
    ```python
    surveys_df.iloc[0:4, 1:4]
    surveys_df.loc[0:4, 1:4]
    ```
    How are the two commands different?


## Matching Criteria

We can extract data by **stating criteria** the data must **satisfy**.

For example, say we want **all rows** where the **`'year`' column contains `2002`**...


```python
surveys_df[surveys_df.year == 2002]
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>record_id</th>
      <th>month</th>
      <th>day</th>
      <th>year</th>
      <th>plot_id</th>
      <th>species_id</th>
      <th>sex</th>
      <th>hindfoot_length</th>
      <th>weight</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>33320</th>
      <td>33321</td>
      <td>1</td>
      <td>12</td>
      <td>2002</td>
      <td>1</td>
      <td>DM</td>
      <td>M</td>
      <td>38.0</td>
      <td>44.0</td>
    </tr>
    <tr>
      <th>33321</th>
      <td>33322</td>
      <td>1</td>
      <td>12</td>
      <td>2002</td>
      <td>1</td>
      <td>DO</td>
      <td>M</td>
      <td>37.0</td>
      <td>58.0</td>
    </tr>
    <tr>
      <th>33322</th>
      <td>33323</td>
      <td>1</td>
      <td>12</td>
      <td>2002</td>
      <td>1</td>
      <td>PB</td>
      <td>M</td>
      <td>28.0</td>
      <td>45.0</td>
    </tr>
    <tr>
      <th>33323</th>
      <td>33324</td>
      <td>1</td>
      <td>12</td>
      <td>2002</td>
      <td>1</td>
      <td>AB</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>33324</th>
      <td>33325</td>
      <td>1</td>
      <td>12</td>
      <td>2002</td>
      <td>1</td>
      <td>DO</td>
      <td>M</td>
      <td>35.0</td>
      <td>29.0</td>
    </tr>
    <tr>
      <th>33325</th>
      <td>33326</td>
      <td>1</td>
      <td>12</td>
      <td>2002</td>
      <td>2</td>
      <td>OT</td>
      <td>F</td>
      <td>20.0</td>
      <td>26.0</td>
    </tr>
    <tr>
      <th>33326</th>
      <td>33327</td>
      <td>1</td>
      <td>12</td>
      <td>2002</td>
      <td>2</td>
      <td>OT</td>
      <td>M</td>
      <td>20.0</td>
      <td>24.0</td>
    </tr>
    <tr>
      <th>33327</th>
      <td>33328</td>
      <td>1</td>
      <td>12</td>
      <td>2002</td>
      <td>2</td>
      <td>OT</td>
      <td>F</td>
      <td>21.0</td>
      <td>22.0</td>
    </tr>
    <tr>
      <th>33328</th>
      <td>33329</td>
      <td>1</td>
      <td>12</td>
      <td>2002</td>
      <td>2</td>
      <td>DM</td>
      <td>M</td>
      <td>37.0</td>
      <td>47.0</td>
    </tr>
    <tr>
      <th>33329</th>
      <td>33330</td>
      <td>1</td>
      <td>12</td>
      <td>2002</td>
      <td>2</td>
      <td>DO</td>
      <td>M</td>
      <td>35.0</td>
      <td>51.0</td>
    </tr>
    <tr>
      <th>33330</th>
      <td>33331</td>
      <td>1</td>
      <td>12</td>
      <td>2002</td>
      <td>2</td>
      <td>PE</td>
      <td>F</td>
      <td>21.0</td>
      <td>23.0</td>
    </tr>
    <tr>
      <th>33331</th>
      <td>33332</td>
      <td>1</td>
      <td>12</td>
      <td>2002</td>
      <td>2</td>
      <td>OT</td>
      <td>F</td>
      <td>20.0</td>
      <td>18.0</td>
    </tr>
    <tr>
      <th>33332</th>
      <td>33333</td>
      <td>1</td>
      <td>12</td>
      <td>2002</td>
      <td>2</td>
      <td>OT</td>
      <td>M</td>
      <td>20.0</td>
      <td>25.0</td>
    </tr>
    <tr>
      <th>33333</th>
      <td>33334</td>
      <td>1</td>
      <td>12</td>
      <td>2002</td>
      <td>2</td>
      <td>OT</td>
      <td>F</td>
      <td>20.0</td>
      <td>22.0</td>
    </tr>
    <tr>
      <th>33334</th>
      <td>33335</td>
      <td>1</td>
      <td>12</td>
      <td>2002</td>
      <td>2</td>
      <td>DO</td>
      <td>F</td>
      <td>36.0</td>
      <td>46.0</td>
    </tr>
    <tr>
      <th>33335</th>
      <td>33336</td>
      <td>1</td>
      <td>12</td>
      <td>2002</td>
      <td>2</td>
      <td>DM</td>
      <td>F</td>
      <td>35.0</td>
      <td>45.0</td>
    </tr>
    <tr>
      <th>33336</th>
      <td>33337</td>
      <td>1</td>
      <td>12</td>
      <td>2002</td>
      <td>2</td>
      <td>PB</td>
      <td>M</td>
      <td>28.0</td>
      <td>47.0</td>
    </tr>
    <tr>
      <th>33337</th>
      <td>33338</td>
      <td>1</td>
      <td>12</td>
      <td>2002</td>
      <td>2</td>
      <td>PB</td>
      <td>F</td>
      <td>26.0</td>
      <td>30.0</td>
    </tr>
    <tr>
      <th>33338</th>
      <td>33339</td>
      <td>1</td>
      <td>12</td>
      <td>2002</td>
      <td>2</td>
      <td>NL</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>33339</th>
      <td>33340</td>
      <td>1</td>
      <td>12</td>
      <td>2002</td>
      <td>12</td>
      <td>DO</td>
      <td>M</td>
      <td>34.0</td>
      <td>24.0</td>
    </tr>
    <tr>
      <th>33340</th>
      <td>33341</td>
      <td>1</td>
      <td>12</td>
      <td>2002</td>
      <td>12</td>
      <td>PE</td>
      <td>F</td>
      <td>20.0</td>
      <td>15.0</td>
    </tr>
    <tr>
      <th>33341</th>
      <td>33342</td>
      <td>1</td>
      <td>12</td>
      <td>2002</td>
      <td>12</td>
      <td>DO</td>
      <td>F</td>
      <td>36.0</td>
      <td>26.0</td>
    </tr>
    <tr>
      <th>33342</th>
      <td>33343</td>
      <td>1</td>
      <td>12</td>
      <td>2002</td>
      <td>12</td>
      <td>DO</td>
      <td>F</td>
      <td>37.0</td>
      <td>47.0</td>
    </tr>
    <tr>
      <th>33343</th>
      <td>33344</td>
      <td>1</td>
      <td>12</td>
      <td>2002</td>
      <td>12</td>
      <td>DM</td>
      <td>M</td>
      <td>36.0</td>
      <td>40.0</td>
    </tr>
    <tr>
      <th>33344</th>
      <td>33345</td>
      <td>1</td>
      <td>12</td>
      <td>2002</td>
      <td>12</td>
      <td>DO</td>
      <td>M</td>
      <td>37.0</td>
      <td>55.0</td>
    </tr>
    <tr>
      <th>33345</th>
      <td>33346</td>
      <td>1</td>
      <td>12</td>
      <td>2002</td>
      <td>12</td>
      <td>PE</td>
      <td>M</td>
      <td>21.0</td>
      <td>23.0</td>
    </tr>
    <tr>
      <th>33346</th>
      <td>33347</td>
      <td>1</td>
      <td>12</td>
      <td>2002</td>
      <td>12</td>
      <td>DM</td>
      <td>F</td>
      <td>37.0</td>
      <td>45.0</td>
    </tr>
    <tr>
      <th>33347</th>
      <td>33348</td>
      <td>1</td>
      <td>12</td>
      <td>2002</td>
      <td>19</td>
      <td>PB</td>
      <td>M</td>
      <td>29.0</td>
      <td>51.0</td>
    </tr>
    <tr>
      <th>33348</th>
      <td>33349</td>
      <td>1</td>
      <td>12</td>
      <td>2002</td>
      <td>19</td>
      <td>PB</td>
      <td>M</td>
      <td>27.0</td>
      <td>46.0</td>
    </tr>
    <tr>
      <th>33349</th>
      <td>33350</td>
      <td>1</td>
      <td>12</td>
      <td>2002</td>
      <td>19</td>
      <td>PP</td>
      <td>F</td>
      <td>20.0</td>
      <td>13.0</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>35519</th>
      <td>35520</td>
      <td>12</td>
      <td>31</td>
      <td>2002</td>
      <td>9</td>
      <td>SF</td>
      <td>NaN</td>
      <td>24.0</td>
      <td>36.0</td>
    </tr>
    <tr>
      <th>35520</th>
      <td>35521</td>
      <td>12</td>
      <td>31</td>
      <td>2002</td>
      <td>9</td>
      <td>DM</td>
      <td>M</td>
      <td>37.0</td>
      <td>48.0</td>
    </tr>
    <tr>
      <th>35521</th>
      <td>35522</td>
      <td>12</td>
      <td>31</td>
      <td>2002</td>
      <td>9</td>
      <td>DM</td>
      <td>F</td>
      <td>35.0</td>
      <td>45.0</td>
    </tr>
    <tr>
      <th>35522</th>
      <td>35523</td>
      <td>12</td>
      <td>31</td>
      <td>2002</td>
      <td>9</td>
      <td>DM</td>
      <td>F</td>
      <td>36.0</td>
      <td>44.0</td>
    </tr>
    <tr>
      <th>35523</th>
      <td>35524</td>
      <td>12</td>
      <td>31</td>
      <td>2002</td>
      <td>9</td>
      <td>PB</td>
      <td>F</td>
      <td>25.0</td>
      <td>27.0</td>
    </tr>
    <tr>
      <th>35524</th>
      <td>35525</td>
      <td>12</td>
      <td>31</td>
      <td>2002</td>
      <td>9</td>
      <td>OL</td>
      <td>M</td>
      <td>21.0</td>
      <td>26.0</td>
    </tr>
    <tr>
      <th>35525</th>
      <td>35526</td>
      <td>12</td>
      <td>31</td>
      <td>2002</td>
      <td>8</td>
      <td>OT</td>
      <td>F</td>
      <td>20.0</td>
      <td>24.0</td>
    </tr>
    <tr>
      <th>35526</th>
      <td>35527</td>
      <td>12</td>
      <td>31</td>
      <td>2002</td>
      <td>13</td>
      <td>DO</td>
      <td>F</td>
      <td>33.0</td>
      <td>43.0</td>
    </tr>
    <tr>
      <th>35527</th>
      <td>35528</td>
      <td>12</td>
      <td>31</td>
      <td>2002</td>
      <td>13</td>
      <td>US</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>35528</th>
      <td>35529</td>
      <td>12</td>
      <td>31</td>
      <td>2002</td>
      <td>13</td>
      <td>PB</td>
      <td>F</td>
      <td>25.0</td>
      <td>25.0</td>
    </tr>
    <tr>
      <th>35529</th>
      <td>35530</td>
      <td>12</td>
      <td>31</td>
      <td>2002</td>
      <td>13</td>
      <td>OT</td>
      <td>F</td>
      <td>20.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>35530</th>
      <td>35531</td>
      <td>12</td>
      <td>31</td>
      <td>2002</td>
      <td>13</td>
      <td>PB</td>
      <td>F</td>
      <td>27.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>35531</th>
      <td>35532</td>
      <td>12</td>
      <td>31</td>
      <td>2002</td>
      <td>14</td>
      <td>DM</td>
      <td>F</td>
      <td>34.0</td>
      <td>43.0</td>
    </tr>
    <tr>
      <th>35532</th>
      <td>35533</td>
      <td>12</td>
      <td>31</td>
      <td>2002</td>
      <td>14</td>
      <td>DM</td>
      <td>F</td>
      <td>36.0</td>
      <td>48.0</td>
    </tr>
    <tr>
      <th>35533</th>
      <td>35534</td>
      <td>12</td>
      <td>31</td>
      <td>2002</td>
      <td>14</td>
      <td>DM</td>
      <td>M</td>
      <td>37.0</td>
      <td>56.0</td>
    </tr>
    <tr>
      <th>35534</th>
      <td>35535</td>
      <td>12</td>
      <td>31</td>
      <td>2002</td>
      <td>14</td>
      <td>DM</td>
      <td>M</td>
      <td>37.0</td>
      <td>53.0</td>
    </tr>
    <tr>
      <th>35535</th>
      <td>35536</td>
      <td>12</td>
      <td>31</td>
      <td>2002</td>
      <td>14</td>
      <td>DM</td>
      <td>F</td>
      <td>35.0</td>
      <td>42.0</td>
    </tr>
    <tr>
      <th>35536</th>
      <td>35537</td>
      <td>12</td>
      <td>31</td>
      <td>2002</td>
      <td>14</td>
      <td>DM</td>
      <td>F</td>
      <td>36.0</td>
      <td>46.0</td>
    </tr>
    <tr>
      <th>35537</th>
      <td>35538</td>
      <td>12</td>
      <td>31</td>
      <td>2002</td>
      <td>15</td>
      <td>PB</td>
      <td>F</td>
      <td>26.0</td>
      <td>31.0</td>
    </tr>
    <tr>
      <th>35538</th>
      <td>35539</td>
      <td>12</td>
      <td>31</td>
      <td>2002</td>
      <td>15</td>
      <td>SF</td>
      <td>M</td>
      <td>26.0</td>
      <td>68.0</td>
    </tr>
    <tr>
      <th>35539</th>
      <td>35540</td>
      <td>12</td>
      <td>31</td>
      <td>2002</td>
      <td>15</td>
      <td>PB</td>
      <td>F</td>
      <td>26.0</td>
      <td>23.0</td>
    </tr>
    <tr>
      <th>35540</th>
      <td>35541</td>
      <td>12</td>
      <td>31</td>
      <td>2002</td>
      <td>15</td>
      <td>PB</td>
      <td>F</td>
      <td>24.0</td>
      <td>31.0</td>
    </tr>
    <tr>
      <th>35541</th>
      <td>35542</td>
      <td>12</td>
      <td>31</td>
      <td>2002</td>
      <td>15</td>
      <td>PB</td>
      <td>F</td>
      <td>26.0</td>
      <td>29.0</td>
    </tr>
    <tr>
      <th>35542</th>
      <td>35543</td>
      <td>12</td>
      <td>31</td>
      <td>2002</td>
      <td>15</td>
      <td>PB</td>
      <td>F</td>
      <td>27.0</td>
      <td>34.0</td>
    </tr>
    <tr>
      <th>35543</th>
      <td>35544</td>
      <td>12</td>
      <td>31</td>
      <td>2002</td>
      <td>15</td>
      <td>US</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>35544</th>
      <td>35545</td>
      <td>12</td>
      <td>31</td>
      <td>2002</td>
      <td>15</td>
      <td>AH</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>35545</th>
      <td>35546</td>
      <td>12</td>
      <td>31</td>
      <td>2002</td>
      <td>15</td>
      <td>AH</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>35546</th>
      <td>35547</td>
      <td>12</td>
      <td>31</td>
      <td>2002</td>
      <td>10</td>
      <td>RM</td>
      <td>F</td>
      <td>15.0</td>
      <td>14.0</td>
    </tr>
    <tr>
      <th>35547</th>
      <td>35548</td>
      <td>12</td>
      <td>31</td>
      <td>2002</td>
      <td>7</td>
      <td>DO</td>
      <td>M</td>
      <td>36.0</td>
      <td>51.0</td>
    </tr>
    <tr>
      <th>35548</th>
      <td>35549</td>
      <td>12</td>
      <td>31</td>
      <td>2002</td>
      <td>5</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
<p>2229 rows × 9 columns</p>
</div>



Or the rows **without `'2002'`**...


```python
surveys_df[surveys_df.year != 2002]
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>record_id</th>
      <th>month</th>
      <th>day</th>
      <th>year</th>
      <th>plot_id</th>
      <th>species_id</th>
      <th>sex</th>
      <th>hindfoot_length</th>
      <th>weight</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>7</td>
      <td>16</td>
      <td>1977</td>
      <td>2</td>
      <td>NL</td>
      <td>M</td>
      <td>32.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>7</td>
      <td>16</td>
      <td>1977</td>
      <td>3</td>
      <td>NL</td>
      <td>M</td>
      <td>33.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>7</td>
      <td>16</td>
      <td>1977</td>
      <td>2</td>
      <td>DM</td>
      <td>F</td>
      <td>37.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4</td>
      <td>7</td>
      <td>16</td>
      <td>1977</td>
      <td>7</td>
      <td>DM</td>
      <td>M</td>
      <td>36.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5</td>
      <td>7</td>
      <td>16</td>
      <td>1977</td>
      <td>3</td>
      <td>DM</td>
      <td>M</td>
      <td>35.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>5</th>
      <td>6</td>
      <td>7</td>
      <td>16</td>
      <td>1977</td>
      <td>1</td>
      <td>PF</td>
      <td>M</td>
      <td>14.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>6</th>
      <td>7</td>
      <td>7</td>
      <td>16</td>
      <td>1977</td>
      <td>2</td>
      <td>PE</td>
      <td>F</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>7</th>
      <td>8</td>
      <td>7</td>
      <td>16</td>
      <td>1977</td>
      <td>1</td>
      <td>DM</td>
      <td>M</td>
      <td>37.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>8</th>
      <td>9</td>
      <td>7</td>
      <td>16</td>
      <td>1977</td>
      <td>1</td>
      <td>DM</td>
      <td>F</td>
      <td>34.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>9</th>
      <td>10</td>
      <td>7</td>
      <td>16</td>
      <td>1977</td>
      <td>6</td>
      <td>PF</td>
      <td>F</td>
      <td>20.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>10</th>
      <td>11</td>
      <td>7</td>
      <td>16</td>
      <td>1977</td>
      <td>5</td>
      <td>DS</td>
      <td>F</td>
      <td>53.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>11</th>
      <td>12</td>
      <td>7</td>
      <td>16</td>
      <td>1977</td>
      <td>7</td>
      <td>DM</td>
      <td>M</td>
      <td>38.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>12</th>
      <td>13</td>
      <td>7</td>
      <td>16</td>
      <td>1977</td>
      <td>3</td>
      <td>DM</td>
      <td>M</td>
      <td>35.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>13</th>
      <td>14</td>
      <td>7</td>
      <td>16</td>
      <td>1977</td>
      <td>8</td>
      <td>DM</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>14</th>
      <td>15</td>
      <td>7</td>
      <td>16</td>
      <td>1977</td>
      <td>6</td>
      <td>DM</td>
      <td>F</td>
      <td>36.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>15</th>
      <td>16</td>
      <td>7</td>
      <td>16</td>
      <td>1977</td>
      <td>4</td>
      <td>DM</td>
      <td>F</td>
      <td>36.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>16</th>
      <td>17</td>
      <td>7</td>
      <td>16</td>
      <td>1977</td>
      <td>3</td>
      <td>DS</td>
      <td>F</td>
      <td>48.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>17</th>
      <td>18</td>
      <td>7</td>
      <td>16</td>
      <td>1977</td>
      <td>2</td>
      <td>PP</td>
      <td>M</td>
      <td>22.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>18</th>
      <td>19</td>
      <td>7</td>
      <td>16</td>
      <td>1977</td>
      <td>4</td>
      <td>PF</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>19</th>
      <td>20</td>
      <td>7</td>
      <td>17</td>
      <td>1977</td>
      <td>11</td>
      <td>DS</td>
      <td>F</td>
      <td>48.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>20</th>
      <td>21</td>
      <td>7</td>
      <td>17</td>
      <td>1977</td>
      <td>14</td>
      <td>DM</td>
      <td>F</td>
      <td>34.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>21</th>
      <td>22</td>
      <td>7</td>
      <td>17</td>
      <td>1977</td>
      <td>15</td>
      <td>NL</td>
      <td>F</td>
      <td>31.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>22</th>
      <td>23</td>
      <td>7</td>
      <td>17</td>
      <td>1977</td>
      <td>13</td>
      <td>DM</td>
      <td>M</td>
      <td>36.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>23</th>
      <td>24</td>
      <td>7</td>
      <td>17</td>
      <td>1977</td>
      <td>13</td>
      <td>SH</td>
      <td>M</td>
      <td>21.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>24</th>
      <td>25</td>
      <td>7</td>
      <td>17</td>
      <td>1977</td>
      <td>9</td>
      <td>DM</td>
      <td>M</td>
      <td>35.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>25</th>
      <td>26</td>
      <td>7</td>
      <td>17</td>
      <td>1977</td>
      <td>15</td>
      <td>DM</td>
      <td>M</td>
      <td>31.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>26</th>
      <td>27</td>
      <td>7</td>
      <td>17</td>
      <td>1977</td>
      <td>15</td>
      <td>DM</td>
      <td>M</td>
      <td>36.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>27</th>
      <td>28</td>
      <td>7</td>
      <td>17</td>
      <td>1977</td>
      <td>11</td>
      <td>DM</td>
      <td>M</td>
      <td>38.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>28</th>
      <td>29</td>
      <td>7</td>
      <td>17</td>
      <td>1977</td>
      <td>11</td>
      <td>PP</td>
      <td>M</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>29</th>
      <td>30</td>
      <td>7</td>
      <td>17</td>
      <td>1977</td>
      <td>10</td>
      <td>DS</td>
      <td>F</td>
      <td>52.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>33290</th>
      <td>33291</td>
      <td>12</td>
      <td>15</td>
      <td>2001</td>
      <td>23</td>
      <td>PE</td>
      <td>M</td>
      <td>20.0</td>
      <td>18.0</td>
    </tr>
    <tr>
      <th>33291</th>
      <td>33292</td>
      <td>12</td>
      <td>15</td>
      <td>2001</td>
      <td>23</td>
      <td>RM</td>
      <td>F</td>
      <td>16.0</td>
      <td>8.0</td>
    </tr>
    <tr>
      <th>33292</th>
      <td>33293</td>
      <td>12</td>
      <td>15</td>
      <td>2001</td>
      <td>20</td>
      <td>PE</td>
      <td>F</td>
      <td>20.0</td>
      <td>22.0</td>
    </tr>
    <tr>
      <th>33293</th>
      <td>33294</td>
      <td>12</td>
      <td>15</td>
      <td>2001</td>
      <td>20</td>
      <td>SH</td>
      <td>M</td>
      <td>25.0</td>
      <td>43.0</td>
    </tr>
    <tr>
      <th>33294</th>
      <td>33295</td>
      <td>12</td>
      <td>15</td>
      <td>2001</td>
      <td>20</td>
      <td>PB</td>
      <td>F</td>
      <td>27.0</td>
      <td>33.0</td>
    </tr>
    <tr>
      <th>33295</th>
      <td>33296</td>
      <td>12</td>
      <td>15</td>
      <td>2001</td>
      <td>20</td>
      <td>PB</td>
      <td>M</td>
      <td>25.0</td>
      <td>35.0</td>
    </tr>
    <tr>
      <th>33296</th>
      <td>33297</td>
      <td>12</td>
      <td>15</td>
      <td>2001</td>
      <td>20</td>
      <td>RM</td>
      <td>M</td>
      <td>16.0</td>
      <td>11.0</td>
    </tr>
    <tr>
      <th>33297</th>
      <td>33298</td>
      <td>12</td>
      <td>15</td>
      <td>2001</td>
      <td>20</td>
      <td>RM</td>
      <td>F</td>
      <td>16.0</td>
      <td>8.0</td>
    </tr>
    <tr>
      <th>33298</th>
      <td>33299</td>
      <td>12</td>
      <td>15</td>
      <td>2001</td>
      <td>20</td>
      <td>PB</td>
      <td>F</td>
      <td>25.0</td>
      <td>28.0</td>
    </tr>
    <tr>
      <th>33299</th>
      <td>33300</td>
      <td>12</td>
      <td>15</td>
      <td>2001</td>
      <td>20</td>
      <td>PB</td>
      <td>F</td>
      <td>26.0</td>
      <td>30.0</td>
    </tr>
    <tr>
      <th>33300</th>
      <td>33301</td>
      <td>12</td>
      <td>15</td>
      <td>2001</td>
      <td>20</td>
      <td>PB</td>
      <td>F</td>
      <td>27.0</td>
      <td>31.0</td>
    </tr>
    <tr>
      <th>33301</th>
      <td>33302</td>
      <td>12</td>
      <td>15</td>
      <td>2001</td>
      <td>24</td>
      <td>PE</td>
      <td>M</td>
      <td>20.0</td>
      <td>24.0</td>
    </tr>
    <tr>
      <th>33302</th>
      <td>33303</td>
      <td>12</td>
      <td>15</td>
      <td>2001</td>
      <td>24</td>
      <td>PE</td>
      <td>M</td>
      <td>20.0</td>
      <td>23.0</td>
    </tr>
    <tr>
      <th>33303</th>
      <td>33304</td>
      <td>12</td>
      <td>15</td>
      <td>2001</td>
      <td>24</td>
      <td>RM</td>
      <td>M</td>
      <td>16.0</td>
      <td>10.0</td>
    </tr>
    <tr>
      <th>33304</th>
      <td>33305</td>
      <td>12</td>
      <td>15</td>
      <td>2001</td>
      <td>7</td>
      <td>PB</td>
      <td>M</td>
      <td>29.0</td>
      <td>44.0</td>
    </tr>
    <tr>
      <th>33305</th>
      <td>33306</td>
      <td>12</td>
      <td>15</td>
      <td>2001</td>
      <td>7</td>
      <td>OT</td>
      <td>M</td>
      <td>19.0</td>
      <td>21.0</td>
    </tr>
    <tr>
      <th>33306</th>
      <td>33307</td>
      <td>12</td>
      <td>15</td>
      <td>2001</td>
      <td>7</td>
      <td>OT</td>
      <td>M</td>
      <td>20.0</td>
      <td>19.0</td>
    </tr>
    <tr>
      <th>33307</th>
      <td>33308</td>
      <td>12</td>
      <td>15</td>
      <td>2001</td>
      <td>7</td>
      <td>PP</td>
      <td>M</td>
      <td>24.0</td>
      <td>16.0</td>
    </tr>
    <tr>
      <th>33308</th>
      <td>33309</td>
      <td>12</td>
      <td>16</td>
      <td>2001</td>
      <td>3</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>33309</th>
      <td>33310</td>
      <td>12</td>
      <td>16</td>
      <td>2001</td>
      <td>4</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>33310</th>
      <td>33311</td>
      <td>12</td>
      <td>16</td>
      <td>2001</td>
      <td>5</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>33311</th>
      <td>33312</td>
      <td>12</td>
      <td>16</td>
      <td>2001</td>
      <td>6</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>33312</th>
      <td>33313</td>
      <td>12</td>
      <td>16</td>
      <td>2001</td>
      <td>8</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>33313</th>
      <td>33314</td>
      <td>12</td>
      <td>16</td>
      <td>2001</td>
      <td>9</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>33314</th>
      <td>33315</td>
      <td>12</td>
      <td>16</td>
      <td>2001</td>
      <td>10</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>33315</th>
      <td>33316</td>
      <td>12</td>
      <td>16</td>
      <td>2001</td>
      <td>11</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>33316</th>
      <td>33317</td>
      <td>12</td>
      <td>16</td>
      <td>2001</td>
      <td>13</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>33317</th>
      <td>33318</td>
      <td>12</td>
      <td>16</td>
      <td>2001</td>
      <td>14</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>33318</th>
      <td>33319</td>
      <td>12</td>
      <td>16</td>
      <td>2001</td>
      <td>15</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>33319</th>
      <td>33320</td>
      <td>12</td>
      <td>16</td>
      <td>2001</td>
      <td>16</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
<p>33320 rows × 9 columns</p>
</div>



Or the rows **after 1980** but **before 1985**...


```python
surveys_df[(surveys_df.year >= 1980) & (surveys_df.year <= 1985)]
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>record_id</th>
      <th>month</th>
      <th>day</th>
      <th>year</th>
      <th>plot_id</th>
      <th>species_id</th>
      <th>sex</th>
      <th>hindfoot_length</th>
      <th>weight</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2270</th>
      <td>2271</td>
      <td>1</td>
      <td>15</td>
      <td>1980</td>
      <td>8</td>
      <td>DO</td>
      <td>M</td>
      <td>35.0</td>
      <td>53.0</td>
    </tr>
    <tr>
      <th>2271</th>
      <td>2272</td>
      <td>1</td>
      <td>15</td>
      <td>1980</td>
      <td>11</td>
      <td>PF</td>
      <td>F</td>
      <td>16.0</td>
      <td>10.0</td>
    </tr>
    <tr>
      <th>2272</th>
      <td>2273</td>
      <td>1</td>
      <td>15</td>
      <td>1980</td>
      <td>18</td>
      <td>DM</td>
      <td>F</td>
      <td>34.0</td>
      <td>33.0</td>
    </tr>
    <tr>
      <th>2273</th>
      <td>2274</td>
      <td>1</td>
      <td>15</td>
      <td>1980</td>
      <td>11</td>
      <td>DM</td>
      <td>M</td>
      <td>38.0</td>
      <td>37.0</td>
    </tr>
    <tr>
      <th>2274</th>
      <td>2275</td>
      <td>1</td>
      <td>15</td>
      <td>1980</td>
      <td>8</td>
      <td>DO</td>
      <td>F</td>
      <td>33.0</td>
      <td>29.0</td>
    </tr>
    <tr>
      <th>2275</th>
      <td>2276</td>
      <td>1</td>
      <td>15</td>
      <td>1980</td>
      <td>11</td>
      <td>DS</td>
      <td>M</td>
      <td>47.0</td>
      <td>132.0</td>
    </tr>
    <tr>
      <th>2276</th>
      <td>2277</td>
      <td>1</td>
      <td>15</td>
      <td>1980</td>
      <td>8</td>
      <td>PF</td>
      <td>M</td>
      <td>15.0</td>
      <td>8.0</td>
    </tr>
    <tr>
      <th>2277</th>
      <td>2278</td>
      <td>1</td>
      <td>15</td>
      <td>1980</td>
      <td>9</td>
      <td>OT</td>
      <td>M</td>
      <td>21.0</td>
      <td>23.0</td>
    </tr>
    <tr>
      <th>2278</th>
      <td>2279</td>
      <td>1</td>
      <td>15</td>
      <td>1980</td>
      <td>11</td>
      <td>DM</td>
      <td>F</td>
      <td>36.0</td>
      <td>36.0</td>
    </tr>
    <tr>
      <th>2279</th>
      <td>2280</td>
      <td>1</td>
      <td>15</td>
      <td>1980</td>
      <td>21</td>
      <td>OT</td>
      <td>F</td>
      <td>20.0</td>
      <td>21.0</td>
    </tr>
    <tr>
      <th>2280</th>
      <td>2281</td>
      <td>1</td>
      <td>15</td>
      <td>1980</td>
      <td>11</td>
      <td>OL</td>
      <td>M</td>
      <td>20.0</td>
      <td>29.0</td>
    </tr>
    <tr>
      <th>2281</th>
      <td>2282</td>
      <td>1</td>
      <td>15</td>
      <td>1980</td>
      <td>17</td>
      <td>DM</td>
      <td>F</td>
      <td>36.0</td>
      <td>49.0</td>
    </tr>
    <tr>
      <th>2282</th>
      <td>2283</td>
      <td>1</td>
      <td>15</td>
      <td>1980</td>
      <td>11</td>
      <td>OL</td>
      <td>M</td>
      <td>21.0</td>
      <td>23.0</td>
    </tr>
    <tr>
      <th>2283</th>
      <td>2284</td>
      <td>1</td>
      <td>15</td>
      <td>1980</td>
      <td>9</td>
      <td>OL</td>
      <td>M</td>
      <td>20.0</td>
      <td>32.0</td>
    </tr>
    <tr>
      <th>2284</th>
      <td>2285</td>
      <td>1</td>
      <td>15</td>
      <td>1980</td>
      <td>10</td>
      <td>OL</td>
      <td>F</td>
      <td>20.0</td>
      <td>24.0</td>
    </tr>
    <tr>
      <th>2285</th>
      <td>2286</td>
      <td>1</td>
      <td>15</td>
      <td>1980</td>
      <td>11</td>
      <td>DM</td>
      <td>M</td>
      <td>38.0</td>
      <td>47.0</td>
    </tr>
    <tr>
      <th>2286</th>
      <td>2287</td>
      <td>1</td>
      <td>15</td>
      <td>1980</td>
      <td>21</td>
      <td>OT</td>
      <td>M</td>
      <td>19.0</td>
      <td>22.0</td>
    </tr>
    <tr>
      <th>2287</th>
      <td>2288</td>
      <td>1</td>
      <td>15</td>
      <td>1980</td>
      <td>19</td>
      <td>RM</td>
      <td>F</td>
      <td>17.0</td>
      <td>12.0</td>
    </tr>
    <tr>
      <th>2288</th>
      <td>2289</td>
      <td>1</td>
      <td>15</td>
      <td>1980</td>
      <td>20</td>
      <td>DS</td>
      <td>F</td>
      <td>52.0</td>
      <td>150.0</td>
    </tr>
    <tr>
      <th>2289</th>
      <td>2290</td>
      <td>1</td>
      <td>15</td>
      <td>1980</td>
      <td>11</td>
      <td>DM</td>
      <td>M</td>
      <td>37.0</td>
      <td>49.0</td>
    </tr>
    <tr>
      <th>2290</th>
      <td>2291</td>
      <td>1</td>
      <td>15</td>
      <td>1980</td>
      <td>9</td>
      <td>OL</td>
      <td>F</td>
      <td>21.0</td>
      <td>34.0</td>
    </tr>
    <tr>
      <th>2291</th>
      <td>2292</td>
      <td>1</td>
      <td>15</td>
      <td>1980</td>
      <td>12</td>
      <td>DM</td>
      <td>F</td>
      <td>35.0</td>
      <td>40.0</td>
    </tr>
    <tr>
      <th>2292</th>
      <td>2293</td>
      <td>1</td>
      <td>15</td>
      <td>1980</td>
      <td>18</td>
      <td>DS</td>
      <td>F</td>
      <td>51.0</td>
      <td>132.0</td>
    </tr>
    <tr>
      <th>2293</th>
      <td>2294</td>
      <td>1</td>
      <td>15</td>
      <td>1980</td>
      <td>22</td>
      <td>DM</td>
      <td>F</td>
      <td>34.0</td>
      <td>25.0</td>
    </tr>
    <tr>
      <th>2294</th>
      <td>2295</td>
      <td>1</td>
      <td>15</td>
      <td>1980</td>
      <td>9</td>
      <td>OL</td>
      <td>M</td>
      <td>21.0</td>
      <td>36.0</td>
    </tr>
    <tr>
      <th>2295</th>
      <td>2296</td>
      <td>1</td>
      <td>15</td>
      <td>1980</td>
      <td>8</td>
      <td>DO</td>
      <td>F</td>
      <td>34.0</td>
      <td>50.0</td>
    </tr>
    <tr>
      <th>2296</th>
      <td>2297</td>
      <td>1</td>
      <td>15</td>
      <td>1980</td>
      <td>11</td>
      <td>DM</td>
      <td>M</td>
      <td>37.0</td>
      <td>45.0</td>
    </tr>
    <tr>
      <th>2297</th>
      <td>2298</td>
      <td>1</td>
      <td>15</td>
      <td>1980</td>
      <td>17</td>
      <td>DM</td>
      <td>M</td>
      <td>35.0</td>
      <td>47.0</td>
    </tr>
    <tr>
      <th>2298</th>
      <td>2299</td>
      <td>1</td>
      <td>15</td>
      <td>1980</td>
      <td>9</td>
      <td>DM</td>
      <td>M</td>
      <td>38.0</td>
      <td>46.0</td>
    </tr>
    <tr>
      <th>2299</th>
      <td>2300</td>
      <td>1</td>
      <td>15</td>
      <td>1980</td>
      <td>18</td>
      <td>DM</td>
      <td>F</td>
      <td>32.0</td>
      <td>29.0</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>11197</th>
      <td>11198</td>
      <td>12</td>
      <td>8</td>
      <td>1985</td>
      <td>4</td>
      <td>DS</td>
      <td>M</td>
      <td>45.0</td>
      <td>129.0</td>
    </tr>
    <tr>
      <th>11198</th>
      <td>11199</td>
      <td>12</td>
      <td>8</td>
      <td>1985</td>
      <td>8</td>
      <td>DM</td>
      <td>F</td>
      <td>38.0</td>
      <td>42.0</td>
    </tr>
    <tr>
      <th>11199</th>
      <td>11200</td>
      <td>12</td>
      <td>8</td>
      <td>1985</td>
      <td>7</td>
      <td>AB</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>11200</th>
      <td>11201</td>
      <td>12</td>
      <td>8</td>
      <td>1985</td>
      <td>5</td>
      <td>OL</td>
      <td>M</td>
      <td>21.0</td>
      <td>29.0</td>
    </tr>
    <tr>
      <th>11201</th>
      <td>11202</td>
      <td>12</td>
      <td>8</td>
      <td>1985</td>
      <td>9</td>
      <td>DM</td>
      <td>F</td>
      <td>35.0</td>
      <td>39.0</td>
    </tr>
    <tr>
      <th>11202</th>
      <td>11203</td>
      <td>12</td>
      <td>8</td>
      <td>1985</td>
      <td>7</td>
      <td>PE</td>
      <td>F</td>
      <td>17.0</td>
      <td>19.0</td>
    </tr>
    <tr>
      <th>11203</th>
      <td>11204</td>
      <td>12</td>
      <td>8</td>
      <td>1985</td>
      <td>3</td>
      <td>PP</td>
      <td>F</td>
      <td>22.0</td>
      <td>16.0</td>
    </tr>
    <tr>
      <th>11204</th>
      <td>11205</td>
      <td>12</td>
      <td>8</td>
      <td>1985</td>
      <td>5</td>
      <td>DO</td>
      <td>M</td>
      <td>37.0</td>
      <td>56.0</td>
    </tr>
    <tr>
      <th>11205</th>
      <td>11206</td>
      <td>12</td>
      <td>8</td>
      <td>1985</td>
      <td>11</td>
      <td>DM</td>
      <td>F</td>
      <td>38.0</td>
      <td>38.0</td>
    </tr>
    <tr>
      <th>11206</th>
      <td>11207</td>
      <td>12</td>
      <td>8</td>
      <td>1985</td>
      <td>2</td>
      <td>PE</td>
      <td>M</td>
      <td>18.0</td>
      <td>19.0</td>
    </tr>
    <tr>
      <th>11207</th>
      <td>11208</td>
      <td>12</td>
      <td>8</td>
      <td>1985</td>
      <td>8</td>
      <td>DS</td>
      <td>F</td>
      <td>50.0</td>
      <td>120.0</td>
    </tr>
    <tr>
      <th>11208</th>
      <td>11209</td>
      <td>12</td>
      <td>8</td>
      <td>1985</td>
      <td>2</td>
      <td>DO</td>
      <td>F</td>
      <td>37.0</td>
      <td>52.0</td>
    </tr>
    <tr>
      <th>11209</th>
      <td>11210</td>
      <td>12</td>
      <td>8</td>
      <td>1985</td>
      <td>2</td>
      <td>DM</td>
      <td>F</td>
      <td>35.0</td>
      <td>40.0</td>
    </tr>
    <tr>
      <th>11210</th>
      <td>11211</td>
      <td>12</td>
      <td>8</td>
      <td>1985</td>
      <td>13</td>
      <td>DM</td>
      <td>M</td>
      <td>37.0</td>
      <td>45.0</td>
    </tr>
    <tr>
      <th>11211</th>
      <td>11212</td>
      <td>12</td>
      <td>8</td>
      <td>1985</td>
      <td>4</td>
      <td>DS</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>121.0</td>
    </tr>
    <tr>
      <th>11212</th>
      <td>11213</td>
      <td>12</td>
      <td>8</td>
      <td>1985</td>
      <td>13</td>
      <td>AH</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>11213</th>
      <td>11214</td>
      <td>12</td>
      <td>8</td>
      <td>1985</td>
      <td>1</td>
      <td>DM</td>
      <td>F</td>
      <td>37.0</td>
      <td>44.0</td>
    </tr>
    <tr>
      <th>11214</th>
      <td>11215</td>
      <td>12</td>
      <td>8</td>
      <td>1985</td>
      <td>2</td>
      <td>NL</td>
      <td>F</td>
      <td>32.0</td>
      <td>160.0</td>
    </tr>
    <tr>
      <th>11215</th>
      <td>11216</td>
      <td>12</td>
      <td>8</td>
      <td>1985</td>
      <td>3</td>
      <td>RM</td>
      <td>M</td>
      <td>17.0</td>
      <td>9.0</td>
    </tr>
    <tr>
      <th>11216</th>
      <td>11217</td>
      <td>12</td>
      <td>8</td>
      <td>1985</td>
      <td>4</td>
      <td>OL</td>
      <td>M</td>
      <td>24.0</td>
      <td>34.0</td>
    </tr>
    <tr>
      <th>11217</th>
      <td>11218</td>
      <td>12</td>
      <td>8</td>
      <td>1985</td>
      <td>9</td>
      <td>DM</td>
      <td>F</td>
      <td>36.0</td>
      <td>39.0</td>
    </tr>
    <tr>
      <th>11218</th>
      <td>11219</td>
      <td>12</td>
      <td>8</td>
      <td>1985</td>
      <td>8</td>
      <td>DM</td>
      <td>F</td>
      <td>38.0</td>
      <td>41.0</td>
    </tr>
    <tr>
      <th>11219</th>
      <td>11220</td>
      <td>12</td>
      <td>8</td>
      <td>1985</td>
      <td>5</td>
      <td>DO</td>
      <td>F</td>
      <td>37.0</td>
      <td>56.0</td>
    </tr>
    <tr>
      <th>11220</th>
      <td>11221</td>
      <td>12</td>
      <td>8</td>
      <td>1985</td>
      <td>13</td>
      <td>AH</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>11221</th>
      <td>11222</td>
      <td>12</td>
      <td>8</td>
      <td>1985</td>
      <td>7</td>
      <td>AB</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>11222</th>
      <td>11223</td>
      <td>12</td>
      <td>8</td>
      <td>1985</td>
      <td>4</td>
      <td>DM</td>
      <td>M</td>
      <td>36.0</td>
      <td>40.0</td>
    </tr>
    <tr>
      <th>11223</th>
      <td>11224</td>
      <td>12</td>
      <td>8</td>
      <td>1985</td>
      <td>11</td>
      <td>DM</td>
      <td>M</td>
      <td>37.0</td>
      <td>49.0</td>
    </tr>
    <tr>
      <th>11224</th>
      <td>11225</td>
      <td>12</td>
      <td>8</td>
      <td>1985</td>
      <td>7</td>
      <td>PE</td>
      <td>M</td>
      <td>20.0</td>
      <td>18.0</td>
    </tr>
    <tr>
      <th>11225</th>
      <td>11226</td>
      <td>12</td>
      <td>8</td>
      <td>1985</td>
      <td>1</td>
      <td>DM</td>
      <td>M</td>
      <td>38.0</td>
      <td>47.0</td>
    </tr>
    <tr>
      <th>11226</th>
      <td>11227</td>
      <td>12</td>
      <td>8</td>
      <td>1985</td>
      <td>15</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
<p>8957 rows × 9 columns</p>
</div>



### Exercise

1. Select a subset of rows in the `surveys_df` from the **year 1999** and that contain **weight values less than or equal to 8**. How many columns did you end up with? What did your neighbor get?
2. You can use the `isin` command to query a DataFrame based upon a list of values as follows:

    ```python
    surveys_df[surveys_df['species_id'].isin([listGoesHere])]
    ```
    
    Use `isin` to find all **plots** that contain **particular species**. How many records contain these values?
3. Experiment with other queries. Create a query that finds all rows with a weight value > or equal to 0.
4. The `~` symbol can return the **OPPOSITE** of the selection that you specify. It is equivalent to **is not in**. Write a query that selects all rows that are **NOT equal** to `'M'` or `'F'` in the surveys data.

## Masks

### Boolean Variables

Set a variable equal to a fixed numerical value.


```python
x = 5
```

Now look at this...


```python
x > 5
```




    False




```python
x == 5
```




    True



The sequences

* `x > 5`
* `x == 5`

are **logical statements**.

That is, they are either **true** or **false**.

Another way to think about this:

> statements like `x == 5` **ask a question**: is this true or not?

Python has a **built-in data type** called a **Boolean** to handle this.  A Boolean variable is either `True` or `False`.

Look at this.


```python
y = (x == 5)
```


```python
y
```




    True




```python
x = 7
```


```python
y = (x == 5)
```


```python
y
```




    False



### Masking in Pandas

We see in the data that some rows have an animal weighing 10 units.  How can we find all rows with this?

Define a boolean variable:

> where is `surveys_df.weight == 10.0`?

Look for all the rows where that's true:


```python
surveys_df[ (surveys_df.weight == 10.0) ]
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>record_id</th>
      <th>month</th>
      <th>day</th>
      <th>year</th>
      <th>plot_id</th>
      <th>species_id</th>
      <th>sex</th>
      <th>hindfoot_length</th>
      <th>weight</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1077</th>
      <td>1078</td>
      <td>7</td>
      <td>8</td>
      <td>1978</td>
      <td>15</td>
      <td>PP</td>
      <td>F</td>
      <td>23.0</td>
      <td>10.0</td>
    </tr>
    <tr>
      <th>1087</th>
      <td>1088</td>
      <td>7</td>
      <td>8</td>
      <td>1978</td>
      <td>14</td>
      <td>PP</td>
      <td>M</td>
      <td>23.0</td>
      <td>10.0</td>
    </tr>
    <tr>
      <th>1897</th>
      <td>1898</td>
      <td>7</td>
      <td>4</td>
      <td>1979</td>
      <td>2</td>
      <td>PP</td>
      <td>M</td>
      <td>20.0</td>
      <td>10.0</td>
    </tr>
    <tr>
      <th>1909</th>
      <td>1910</td>
      <td>7</td>
      <td>24</td>
      <td>1979</td>
      <td>20</td>
      <td>PF</td>
      <td>M</td>
      <td>17.0</td>
      <td>10.0</td>
    </tr>
    <tr>
      <th>2271</th>
      <td>2272</td>
      <td>1</td>
      <td>15</td>
      <td>1980</td>
      <td>11</td>
      <td>PF</td>
      <td>F</td>
      <td>16.0</td>
      <td>10.0</td>
    </tr>
    <tr>
      <th>2326</th>
      <td>2327</td>
      <td>1</td>
      <td>15</td>
      <td>1980</td>
      <td>10</td>
      <td>RM</td>
      <td>M</td>
      <td>16.0</td>
      <td>10.0</td>
    </tr>
    <tr>
      <th>2378</th>
      <td>2379</td>
      <td>1</td>
      <td>16</td>
      <td>1980</td>
      <td>15</td>
      <td>RM</td>
      <td>F</td>
      <td>15.0</td>
      <td>10.0</td>
    </tr>
    <tr>
      <th>2418</th>
      <td>2419</td>
      <td>2</td>
      <td>24</td>
      <td>1980</td>
      <td>19</td>
      <td>RM</td>
      <td>M</td>
      <td>15.0</td>
      <td>10.0</td>
    </tr>
    <tr>
      <th>2441</th>
      <td>2442</td>
      <td>2</td>
      <td>24</td>
      <td>1980</td>
      <td>10</td>
      <td>RM</td>
      <td>M</td>
      <td>16.0</td>
      <td>10.0</td>
    </tr>
    <tr>
      <th>2536</th>
      <td>2537</td>
      <td>3</td>
      <td>9</td>
      <td>1980</td>
      <td>3</td>
      <td>RM</td>
      <td>M</td>
      <td>NaN</td>
      <td>10.0</td>
    </tr>
    <tr>
      <th>2622</th>
      <td>2623</td>
      <td>3</td>
      <td>9</td>
      <td>1980</td>
      <td>12</td>
      <td>RM</td>
      <td>M</td>
      <td>NaN</td>
      <td>10.0</td>
    </tr>
    <tr>
      <th>2645</th>
      <td>2646</td>
      <td>3</td>
      <td>9</td>
      <td>1980</td>
      <td>2</td>
      <td>RM</td>
      <td>M</td>
      <td>NaN</td>
      <td>10.0</td>
    </tr>
    <tr>
      <th>2651</th>
      <td>2652</td>
      <td>3</td>
      <td>9</td>
      <td>1980</td>
      <td>19</td>
      <td>RM</td>
      <td>M</td>
      <td>NaN</td>
      <td>10.0</td>
    </tr>
    <tr>
      <th>2792</th>
      <td>2793</td>
      <td>3</td>
      <td>22</td>
      <td>1980</td>
      <td>3</td>
      <td>RM</td>
      <td>M</td>
      <td>NaN</td>
      <td>10.0</td>
    </tr>
    <tr>
      <th>2796</th>
      <td>2797</td>
      <td>3</td>
      <td>22</td>
      <td>1980</td>
      <td>3</td>
      <td>RM</td>
      <td>M</td>
      <td>NaN</td>
      <td>10.0</td>
    </tr>
    <tr>
      <th>2833</th>
      <td>2834</td>
      <td>4</td>
      <td>17</td>
      <td>1980</td>
      <td>19</td>
      <td>RM</td>
      <td>M</td>
      <td>NaN</td>
      <td>10.0</td>
    </tr>
    <tr>
      <th>2835</th>
      <td>2836</td>
      <td>4</td>
      <td>17</td>
      <td>1980</td>
      <td>10</td>
      <td>OT</td>
      <td>F</td>
      <td>17.0</td>
      <td>10.0</td>
    </tr>
    <tr>
      <th>2854</th>
      <td>2855</td>
      <td>4</td>
      <td>17</td>
      <td>1980</td>
      <td>10</td>
      <td>OT</td>
      <td>M</td>
      <td>19.0</td>
      <td>10.0</td>
    </tr>
    <tr>
      <th>2871</th>
      <td>2872</td>
      <td>4</td>
      <td>18</td>
      <td>1980</td>
      <td>3</td>
      <td>RM</td>
      <td>M</td>
      <td>NaN</td>
      <td>10.0</td>
    </tr>
    <tr>
      <th>3221</th>
      <td>3222</td>
      <td>8</td>
      <td>14</td>
      <td>1980</td>
      <td>3</td>
      <td>PF</td>
      <td>M</td>
      <td>16.0</td>
      <td>10.0</td>
    </tr>
    <tr>
      <th>3227</th>
      <td>3228</td>
      <td>8</td>
      <td>14</td>
      <td>1980</td>
      <td>3</td>
      <td>PF</td>
      <td>F</td>
      <td>16.0</td>
      <td>10.0</td>
    </tr>
    <tr>
      <th>3238</th>
      <td>3239</td>
      <td>8</td>
      <td>14</td>
      <td>1980</td>
      <td>13</td>
      <td>PF</td>
      <td>F</td>
      <td>14.0</td>
      <td>10.0</td>
    </tr>
    <tr>
      <th>3297</th>
      <td>3298</td>
      <td>9</td>
      <td>8</td>
      <td>1980</td>
      <td>3</td>
      <td>PF</td>
      <td>M</td>
      <td>16.0</td>
      <td>10.0</td>
    </tr>
    <tr>
      <th>3907</th>
      <td>3908</td>
      <td>3</td>
      <td>8</td>
      <td>1981</td>
      <td>19</td>
      <td>RM</td>
      <td>M</td>
      <td>17.0</td>
      <td>10.0</td>
    </tr>
    <tr>
      <th>3915</th>
      <td>3916</td>
      <td>3</td>
      <td>8</td>
      <td>1981</td>
      <td>17</td>
      <td>OT</td>
      <td>M</td>
      <td>21.0</td>
      <td>10.0</td>
    </tr>
    <tr>
      <th>4512</th>
      <td>4513</td>
      <td>6</td>
      <td>4</td>
      <td>1981</td>
      <td>1</td>
      <td>PP</td>
      <td>F</td>
      <td>21.0</td>
      <td>10.0</td>
    </tr>
    <tr>
      <th>4737</th>
      <td>4738</td>
      <td>7</td>
      <td>31</td>
      <td>1981</td>
      <td>1</td>
      <td>PP</td>
      <td>F</td>
      <td>22.0</td>
      <td>10.0</td>
    </tr>
    <tr>
      <th>4965</th>
      <td>4966</td>
      <td>11</td>
      <td>22</td>
      <td>1981</td>
      <td>17</td>
      <td>RM</td>
      <td>M</td>
      <td>18.0</td>
      <td>10.0</td>
    </tr>
    <tr>
      <th>4970</th>
      <td>4971</td>
      <td>11</td>
      <td>22</td>
      <td>1981</td>
      <td>15</td>
      <td>PE</td>
      <td>M</td>
      <td>19.0</td>
      <td>10.0</td>
    </tr>
    <tr>
      <th>5005</th>
      <td>5006</td>
      <td>11</td>
      <td>22</td>
      <td>1981</td>
      <td>19</td>
      <td>RM</td>
      <td>M</td>
      <td>17.0</td>
      <td>10.0</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>28946</th>
      <td>28947</td>
      <td>12</td>
      <td>22</td>
      <td>1998</td>
      <td>18</td>
      <td>RM</td>
      <td>M</td>
      <td>17.0</td>
      <td>10.0</td>
    </tr>
    <tr>
      <th>29195</th>
      <td>29196</td>
      <td>2</td>
      <td>20</td>
      <td>1999</td>
      <td>18</td>
      <td>RM</td>
      <td>M</td>
      <td>18.0</td>
      <td>10.0</td>
    </tr>
    <tr>
      <th>29213</th>
      <td>29214</td>
      <td>2</td>
      <td>20</td>
      <td>1999</td>
      <td>20</td>
      <td>RM</td>
      <td>F</td>
      <td>17.0</td>
      <td>10.0</td>
    </tr>
    <tr>
      <th>29257</th>
      <td>29258</td>
      <td>2</td>
      <td>21</td>
      <td>1999</td>
      <td>6</td>
      <td>RM</td>
      <td>M</td>
      <td>17.0</td>
      <td>10.0</td>
    </tr>
    <tr>
      <th>29334</th>
      <td>29335</td>
      <td>3</td>
      <td>14</td>
      <td>1999</td>
      <td>18</td>
      <td>RM</td>
      <td>M</td>
      <td>18.0</td>
      <td>10.0</td>
    </tr>
    <tr>
      <th>29346</th>
      <td>29347</td>
      <td>3</td>
      <td>14</td>
      <td>1999</td>
      <td>20</td>
      <td>RM</td>
      <td>F</td>
      <td>17.0</td>
      <td>10.0</td>
    </tr>
    <tr>
      <th>29686</th>
      <td>29687</td>
      <td>5</td>
      <td>16</td>
      <td>1999</td>
      <td>15</td>
      <td>RM</td>
      <td>M</td>
      <td>17.0</td>
      <td>10.0</td>
    </tr>
    <tr>
      <th>29810</th>
      <td>29811</td>
      <td>6</td>
      <td>13</td>
      <td>1999</td>
      <td>15</td>
      <td>PP</td>
      <td>F</td>
      <td>21.0</td>
      <td>10.0</td>
    </tr>
    <tr>
      <th>29986</th>
      <td>29987</td>
      <td>11</td>
      <td>6</td>
      <td>1999</td>
      <td>22</td>
      <td>PP</td>
      <td>M</td>
      <td>21.0</td>
      <td>10.0</td>
    </tr>
    <tr>
      <th>30641</th>
      <td>30642</td>
      <td>4</td>
      <td>30</td>
      <td>2000</td>
      <td>23</td>
      <td>RM</td>
      <td>M</td>
      <td>16.0</td>
      <td>10.0</td>
    </tr>
    <tr>
      <th>30732</th>
      <td>30733</td>
      <td>6</td>
      <td>3</td>
      <td>2000</td>
      <td>2</td>
      <td>PP</td>
      <td>M</td>
      <td>27.0</td>
      <td>10.0</td>
    </tr>
    <tr>
      <th>30786</th>
      <td>30787</td>
      <td>6</td>
      <td>3</td>
      <td>2000</td>
      <td>21</td>
      <td>PP</td>
      <td>M</td>
      <td>20.0</td>
      <td>10.0</td>
    </tr>
    <tr>
      <th>30799</th>
      <td>30800</td>
      <td>6</td>
      <td>3</td>
      <td>2000</td>
      <td>24</td>
      <td>RM</td>
      <td>M</td>
      <td>17.0</td>
      <td>10.0</td>
    </tr>
    <tr>
      <th>31036</th>
      <td>31037</td>
      <td>7</td>
      <td>2</td>
      <td>2000</td>
      <td>9</td>
      <td>PP</td>
      <td>M</td>
      <td>21.0</td>
      <td>10.0</td>
    </tr>
    <tr>
      <th>31609</th>
      <td>31610</td>
      <td>11</td>
      <td>26</td>
      <td>2000</td>
      <td>5</td>
      <td>RM</td>
      <td>M</td>
      <td>15.0</td>
      <td>10.0</td>
    </tr>
    <tr>
      <th>31610</th>
      <td>31611</td>
      <td>11</td>
      <td>26</td>
      <td>2000</td>
      <td>5</td>
      <td>RM</td>
      <td>M</td>
      <td>17.0</td>
      <td>10.0</td>
    </tr>
    <tr>
      <th>32189</th>
      <td>32190</td>
      <td>6</td>
      <td>25</td>
      <td>2001</td>
      <td>17</td>
      <td>PP</td>
      <td>F</td>
      <td>21.0</td>
      <td>10.0</td>
    </tr>
    <tr>
      <th>32713</th>
      <td>32714</td>
      <td>9</td>
      <td>23</td>
      <td>2001</td>
      <td>4</td>
      <td>PF</td>
      <td>F</td>
      <td>16.0</td>
      <td>10.0</td>
    </tr>
    <tr>
      <th>33303</th>
      <td>33304</td>
      <td>12</td>
      <td>15</td>
      <td>2001</td>
      <td>24</td>
      <td>RM</td>
      <td>M</td>
      <td>16.0</td>
      <td>10.0</td>
    </tr>
    <tr>
      <th>33482</th>
      <td>33483</td>
      <td>2</td>
      <td>9</td>
      <td>2002</td>
      <td>20</td>
      <td>RM</td>
      <td>M</td>
      <td>18.0</td>
      <td>10.0</td>
    </tr>
    <tr>
      <th>33553</th>
      <td>33554</td>
      <td>2</td>
      <td>10</td>
      <td>2002</td>
      <td>15</td>
      <td>RM</td>
      <td>F</td>
      <td>17.0</td>
      <td>10.0</td>
    </tr>
    <tr>
      <th>34014</th>
      <td>34015</td>
      <td>5</td>
      <td>15</td>
      <td>2002</td>
      <td>20</td>
      <td>RM</td>
      <td>M</td>
      <td>18.0</td>
      <td>10.0</td>
    </tr>
    <tr>
      <th>34332</th>
      <td>34333</td>
      <td>6</td>
      <td>16</td>
      <td>2002</td>
      <td>11</td>
      <td>PP</td>
      <td>F</td>
      <td>22.0</td>
      <td>10.0</td>
    </tr>
    <tr>
      <th>34344</th>
      <td>34345</td>
      <td>6</td>
      <td>16</td>
      <td>2002</td>
      <td>9</td>
      <td>PP</td>
      <td>M</td>
      <td>21.0</td>
      <td>10.0</td>
    </tr>
    <tr>
      <th>34389</th>
      <td>34390</td>
      <td>6</td>
      <td>16</td>
      <td>2002</td>
      <td>15</td>
      <td>PP</td>
      <td>M</td>
      <td>22.0</td>
      <td>10.0</td>
    </tr>
    <tr>
      <th>34438</th>
      <td>34439</td>
      <td>7</td>
      <td>13</td>
      <td>2002</td>
      <td>12</td>
      <td>PP</td>
      <td>F</td>
      <td>21.0</td>
      <td>10.0</td>
    </tr>
    <tr>
      <th>34452</th>
      <td>34453</td>
      <td>7</td>
      <td>13</td>
      <td>2002</td>
      <td>19</td>
      <td>PP</td>
      <td>M</td>
      <td>22.0</td>
      <td>10.0</td>
    </tr>
    <tr>
      <th>34760</th>
      <td>34761</td>
      <td>10</td>
      <td>5</td>
      <td>2002</td>
      <td>1</td>
      <td>PP</td>
      <td>F</td>
      <td>22.0</td>
      <td>10.0</td>
    </tr>
    <tr>
      <th>34881</th>
      <td>34882</td>
      <td>10</td>
      <td>6</td>
      <td>2002</td>
      <td>4</td>
      <td>PF</td>
      <td>F</td>
      <td>15.0</td>
      <td>10.0</td>
    </tr>
    <tr>
      <th>35419</th>
      <td>35420</td>
      <td>12</td>
      <td>29</td>
      <td>2002</td>
      <td>19</td>
      <td>RO</td>
      <td>M</td>
      <td>15.0</td>
      <td>10.0</td>
    </tr>
  </tbody>
</table>
<p>759 rows × 9 columns</p>
</div>



What about rows with a **null** entry, i.e. `NaN` (not a number)?

There's a function that checks for null entries:


```python
pd.isnull(surveys_df)
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>record_id</th>
      <th>month</th>
      <th>day</th>
      <th>year</th>
      <th>plot_id</th>
      <th>species_id</th>
      <th>sex</th>
      <th>hindfoot_length</th>
      <th>weight</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>True</td>
    </tr>
    <tr>
      <th>1</th>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>True</td>
    </tr>
    <tr>
      <th>2</th>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>True</td>
    </tr>
    <tr>
      <th>3</th>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>True</td>
    </tr>
    <tr>
      <th>4</th>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>True</td>
    </tr>
    <tr>
      <th>5</th>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>True</td>
    </tr>
    <tr>
      <th>6</th>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>True</td>
      <td>True</td>
    </tr>
    <tr>
      <th>7</th>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>True</td>
    </tr>
    <tr>
      <th>8</th>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>True</td>
    </tr>
    <tr>
      <th>9</th>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>True</td>
    </tr>
    <tr>
      <th>10</th>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>True</td>
    </tr>
    <tr>
      <th>11</th>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>True</td>
    </tr>
    <tr>
      <th>12</th>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>True</td>
    </tr>
    <tr>
      <th>13</th>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
    </tr>
    <tr>
      <th>14</th>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>True</td>
    </tr>
    <tr>
      <th>15</th>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>True</td>
    </tr>
    <tr>
      <th>16</th>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>True</td>
    </tr>
    <tr>
      <th>17</th>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>True</td>
    </tr>
    <tr>
      <th>18</th>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
    </tr>
    <tr>
      <th>19</th>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>True</td>
    </tr>
    <tr>
      <th>20</th>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>True</td>
    </tr>
    <tr>
      <th>21</th>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>True</td>
    </tr>
    <tr>
      <th>22</th>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>True</td>
    </tr>
    <tr>
      <th>23</th>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>True</td>
    </tr>
    <tr>
      <th>24</th>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>True</td>
    </tr>
    <tr>
      <th>25</th>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>True</td>
    </tr>
    <tr>
      <th>26</th>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>True</td>
    </tr>
    <tr>
      <th>27</th>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>True</td>
    </tr>
    <tr>
      <th>28</th>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>True</td>
      <td>True</td>
    </tr>
    <tr>
      <th>29</th>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>True</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>35519</th>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>True</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <th>35520</th>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <th>35521</th>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <th>35522</th>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <th>35523</th>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <th>35524</th>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <th>35525</th>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <th>35526</th>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <th>35527</th>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
    </tr>
    <tr>
      <th>35528</th>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <th>35529</th>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>True</td>
    </tr>
    <tr>
      <th>35530</th>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>True</td>
    </tr>
    <tr>
      <th>35531</th>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <th>35532</th>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <th>35533</th>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <th>35534</th>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <th>35535</th>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <th>35536</th>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <th>35537</th>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <th>35538</th>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <th>35539</th>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <th>35540</th>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <th>35541</th>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <th>35542</th>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <th>35543</th>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
    </tr>
    <tr>
      <th>35544</th>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
    </tr>
    <tr>
      <th>35545</th>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
    </tr>
    <tr>
      <th>35546</th>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <th>35547</th>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <th>35548</th>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
    </tr>
  </tbody>
</table>
<p>35549 rows × 9 columns</p>
</div>



Note how this gives a DataFrame the **same size as the original**, and it has `True` in **those cells containing a null value**.

To select the **rows** that have null values, we try this...


```python
#To select just the rows with NaN values, we can use the .any method
surveys_df[pd.isnull(surveys_df).any(axis=1)]
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>record_id</th>
      <th>month</th>
      <th>day</th>
      <th>year</th>
      <th>plot_id</th>
      <th>species_id</th>
      <th>sex</th>
      <th>hindfoot_length</th>
      <th>weight</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>7</td>
      <td>16</td>
      <td>1977</td>
      <td>2</td>
      <td>NL</td>
      <td>M</td>
      <td>32.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>7</td>
      <td>16</td>
      <td>1977</td>
      <td>3</td>
      <td>NL</td>
      <td>M</td>
      <td>33.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>7</td>
      <td>16</td>
      <td>1977</td>
      <td>2</td>
      <td>DM</td>
      <td>F</td>
      <td>37.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4</td>
      <td>7</td>
      <td>16</td>
      <td>1977</td>
      <td>7</td>
      <td>DM</td>
      <td>M</td>
      <td>36.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5</td>
      <td>7</td>
      <td>16</td>
      <td>1977</td>
      <td>3</td>
      <td>DM</td>
      <td>M</td>
      <td>35.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>5</th>
      <td>6</td>
      <td>7</td>
      <td>16</td>
      <td>1977</td>
      <td>1</td>
      <td>PF</td>
      <td>M</td>
      <td>14.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>6</th>
      <td>7</td>
      <td>7</td>
      <td>16</td>
      <td>1977</td>
      <td>2</td>
      <td>PE</td>
      <td>F</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>7</th>
      <td>8</td>
      <td>7</td>
      <td>16</td>
      <td>1977</td>
      <td>1</td>
      <td>DM</td>
      <td>M</td>
      <td>37.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>8</th>
      <td>9</td>
      <td>7</td>
      <td>16</td>
      <td>1977</td>
      <td>1</td>
      <td>DM</td>
      <td>F</td>
      <td>34.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>9</th>
      <td>10</td>
      <td>7</td>
      <td>16</td>
      <td>1977</td>
      <td>6</td>
      <td>PF</td>
      <td>F</td>
      <td>20.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>10</th>
      <td>11</td>
      <td>7</td>
      <td>16</td>
      <td>1977</td>
      <td>5</td>
      <td>DS</td>
      <td>F</td>
      <td>53.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>11</th>
      <td>12</td>
      <td>7</td>
      <td>16</td>
      <td>1977</td>
      <td>7</td>
      <td>DM</td>
      <td>M</td>
      <td>38.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>12</th>
      <td>13</td>
      <td>7</td>
      <td>16</td>
      <td>1977</td>
      <td>3</td>
      <td>DM</td>
      <td>M</td>
      <td>35.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>13</th>
      <td>14</td>
      <td>7</td>
      <td>16</td>
      <td>1977</td>
      <td>8</td>
      <td>DM</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>14</th>
      <td>15</td>
      <td>7</td>
      <td>16</td>
      <td>1977</td>
      <td>6</td>
      <td>DM</td>
      <td>F</td>
      <td>36.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>15</th>
      <td>16</td>
      <td>7</td>
      <td>16</td>
      <td>1977</td>
      <td>4</td>
      <td>DM</td>
      <td>F</td>
      <td>36.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>16</th>
      <td>17</td>
      <td>7</td>
      <td>16</td>
      <td>1977</td>
      <td>3</td>
      <td>DS</td>
      <td>F</td>
      <td>48.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>17</th>
      <td>18</td>
      <td>7</td>
      <td>16</td>
      <td>1977</td>
      <td>2</td>
      <td>PP</td>
      <td>M</td>
      <td>22.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>18</th>
      <td>19</td>
      <td>7</td>
      <td>16</td>
      <td>1977</td>
      <td>4</td>
      <td>PF</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>19</th>
      <td>20</td>
      <td>7</td>
      <td>17</td>
      <td>1977</td>
      <td>11</td>
      <td>DS</td>
      <td>F</td>
      <td>48.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>20</th>
      <td>21</td>
      <td>7</td>
      <td>17</td>
      <td>1977</td>
      <td>14</td>
      <td>DM</td>
      <td>F</td>
      <td>34.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>21</th>
      <td>22</td>
      <td>7</td>
      <td>17</td>
      <td>1977</td>
      <td>15</td>
      <td>NL</td>
      <td>F</td>
      <td>31.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>22</th>
      <td>23</td>
      <td>7</td>
      <td>17</td>
      <td>1977</td>
      <td>13</td>
      <td>DM</td>
      <td>M</td>
      <td>36.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>23</th>
      <td>24</td>
      <td>7</td>
      <td>17</td>
      <td>1977</td>
      <td>13</td>
      <td>SH</td>
      <td>M</td>
      <td>21.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>24</th>
      <td>25</td>
      <td>7</td>
      <td>17</td>
      <td>1977</td>
      <td>9</td>
      <td>DM</td>
      <td>M</td>
      <td>35.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>25</th>
      <td>26</td>
      <td>7</td>
      <td>17</td>
      <td>1977</td>
      <td>15</td>
      <td>DM</td>
      <td>M</td>
      <td>31.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>26</th>
      <td>27</td>
      <td>7</td>
      <td>17</td>
      <td>1977</td>
      <td>15</td>
      <td>DM</td>
      <td>M</td>
      <td>36.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>27</th>
      <td>28</td>
      <td>7</td>
      <td>17</td>
      <td>1977</td>
      <td>11</td>
      <td>DM</td>
      <td>M</td>
      <td>38.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>28</th>
      <td>29</td>
      <td>7</td>
      <td>17</td>
      <td>1977</td>
      <td>11</td>
      <td>PP</td>
      <td>M</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>29</th>
      <td>30</td>
      <td>7</td>
      <td>17</td>
      <td>1977</td>
      <td>10</td>
      <td>DS</td>
      <td>F</td>
      <td>52.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>35187</th>
      <td>35188</td>
      <td>11</td>
      <td>10</td>
      <td>2002</td>
      <td>10</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>35256</th>
      <td>35257</td>
      <td>12</td>
      <td>7</td>
      <td>2002</td>
      <td>22</td>
      <td>PB</td>
      <td>M</td>
      <td>26.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>35259</th>
      <td>35260</td>
      <td>12</td>
      <td>7</td>
      <td>2002</td>
      <td>21</td>
      <td>PB</td>
      <td>F</td>
      <td>24.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>35277</th>
      <td>35278</td>
      <td>12</td>
      <td>7</td>
      <td>2002</td>
      <td>20</td>
      <td>AH</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>35279</th>
      <td>35280</td>
      <td>12</td>
      <td>7</td>
      <td>2002</td>
      <td>16</td>
      <td>PB</td>
      <td>M</td>
      <td>28.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>35322</th>
      <td>35323</td>
      <td>12</td>
      <td>8</td>
      <td>2002</td>
      <td>11</td>
      <td>AH</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>35328</th>
      <td>35329</td>
      <td>12</td>
      <td>8</td>
      <td>2002</td>
      <td>11</td>
      <td>PP</td>
      <td>M</td>
      <td>NaN</td>
      <td>16.0</td>
    </tr>
    <tr>
      <th>35370</th>
      <td>35371</td>
      <td>12</td>
      <td>8</td>
      <td>2002</td>
      <td>14</td>
      <td>AH</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>35378</th>
      <td>35379</td>
      <td>12</td>
      <td>8</td>
      <td>2002</td>
      <td>15</td>
      <td>PB</td>
      <td>F</td>
      <td>26.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>35384</th>
      <td>35385</td>
      <td>12</td>
      <td>8</td>
      <td>2002</td>
      <td>10</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>35387</th>
      <td>35388</td>
      <td>12</td>
      <td>29</td>
      <td>2002</td>
      <td>1</td>
      <td>DO</td>
      <td>M</td>
      <td>35.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>35403</th>
      <td>35404</td>
      <td>12</td>
      <td>29</td>
      <td>2002</td>
      <td>2</td>
      <td>NL</td>
      <td>F</td>
      <td>30.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>35448</th>
      <td>35449</td>
      <td>12</td>
      <td>29</td>
      <td>2002</td>
      <td>20</td>
      <td>OT</td>
      <td>F</td>
      <td>20.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>35452</th>
      <td>35453</td>
      <td>12</td>
      <td>29</td>
      <td>2002</td>
      <td>20</td>
      <td>PB</td>
      <td>M</td>
      <td>28.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>35457</th>
      <td>35458</td>
      <td>12</td>
      <td>29</td>
      <td>2002</td>
      <td>20</td>
      <td>AH</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>35477</th>
      <td>35478</td>
      <td>12</td>
      <td>29</td>
      <td>2002</td>
      <td>24</td>
      <td>AH</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>35485</th>
      <td>35486</td>
      <td>12</td>
      <td>29</td>
      <td>2002</td>
      <td>16</td>
      <td>DO</td>
      <td>M</td>
      <td>37.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>35495</th>
      <td>35496</td>
      <td>12</td>
      <td>31</td>
      <td>2002</td>
      <td>4</td>
      <td>PB</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>35510</th>
      <td>35511</td>
      <td>12</td>
      <td>31</td>
      <td>2002</td>
      <td>11</td>
      <td>DX</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>35511</th>
      <td>35512</td>
      <td>12</td>
      <td>31</td>
      <td>2002</td>
      <td>11</td>
      <td>US</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>35512</th>
      <td>35513</td>
      <td>12</td>
      <td>31</td>
      <td>2002</td>
      <td>11</td>
      <td>US</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>35514</th>
      <td>35515</td>
      <td>12</td>
      <td>31</td>
      <td>2002</td>
      <td>11</td>
      <td>SF</td>
      <td>F</td>
      <td>27.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>35519</th>
      <td>35520</td>
      <td>12</td>
      <td>31</td>
      <td>2002</td>
      <td>9</td>
      <td>SF</td>
      <td>NaN</td>
      <td>24.0</td>
      <td>36.0</td>
    </tr>
    <tr>
      <th>35527</th>
      <td>35528</td>
      <td>12</td>
      <td>31</td>
      <td>2002</td>
      <td>13</td>
      <td>US</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>35529</th>
      <td>35530</td>
      <td>12</td>
      <td>31</td>
      <td>2002</td>
      <td>13</td>
      <td>OT</td>
      <td>F</td>
      <td>20.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>35530</th>
      <td>35531</td>
      <td>12</td>
      <td>31</td>
      <td>2002</td>
      <td>13</td>
      <td>PB</td>
      <td>F</td>
      <td>27.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>35543</th>
      <td>35544</td>
      <td>12</td>
      <td>31</td>
      <td>2002</td>
      <td>15</td>
      <td>US</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>35544</th>
      <td>35545</td>
      <td>12</td>
      <td>31</td>
      <td>2002</td>
      <td>15</td>
      <td>AH</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>35545</th>
      <td>35546</td>
      <td>12</td>
      <td>31</td>
      <td>2002</td>
      <td>15</td>
      <td>AH</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>35548</th>
      <td>35549</td>
      <td>12</td>
      <td>31</td>
      <td>2002</td>
      <td>5</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
<p>4873 rows × 9 columns</p>
</div>



Now let's find **weights with null values**.

We could take the above process, then **retrict to the weight column**.


```python
# what does this do?
empty_weights = surveys_df[pd.isnull(surveys_df).any(axis=1)]['weight']
```


```python
empty_weights
```




    0         NaN
    1         NaN
    2         NaN
    3         NaN
    4         NaN
    5         NaN
    6         NaN
    7         NaN
    8         NaN
    9         NaN
    10        NaN
    11        NaN
    12        NaN
    13        NaN
    14        NaN
    15        NaN
    16        NaN
    17        NaN
    18        NaN
    19        NaN
    20        NaN
    21        NaN
    22        NaN
    23        NaN
    24        NaN
    25        NaN
    26        NaN
    27        NaN
    28        NaN
    29        NaN
             ... 
    35187     NaN
    35256     NaN
    35259     NaN
    35277     NaN
    35279     NaN
    35322     NaN
    35328    16.0
    35370     NaN
    35378     NaN
    35384     NaN
    35387     NaN
    35403     NaN
    35448     NaN
    35452     NaN
    35457     NaN
    35477     NaN
    35485     NaN
    35495     NaN
    35510     NaN
    35511     NaN
    35512     NaN
    35514     NaN
    35519    36.0
    35527     NaN
    35529     NaN
    35530     NaN
    35543     NaN
    35544     NaN
    35545     NaN
    35548     NaN
    Name: weight, dtype: float64




```python
len(empty_weights)
```




    4873



### Exercise

1. Create a new DataFrame that only contains observations with sex values that are **not** female or male. Assign each sex value in the new DataFrame to a new value of `'x'`. Determine the number of null values in the subset.

2. Create a new DataFrame that contains only observations that are of sex male or female and where weight values are greater than 0. Create a stacked bar plot of average weight by plot with male vs female values stacked for each plot.


```python

```
