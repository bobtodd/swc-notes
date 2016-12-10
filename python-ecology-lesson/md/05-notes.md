
# Lesson 5: Data workflows and automation

These are some notes for [Data Carpentry](http://www.datacarpentry.org)'s tutorial [*Data Analysis and Visualization in Python*](http://www.datacarpentry.org/python-ecology-lesson/).  The web page for this lesson can be found [here](http://www.datacarpentry.org/python-ecology-lesson/05-loops-and-functions).

## Goal

> Work with loops, functions, and conditions

## Basic Idea

We can use Pandas to work with data as in a **spreadsheet**.

But we'd like to use Python as a programming language to **automate tasks**.

## `for` Loops

The `for` loop allows us to **repeatedly apply** a **collection of commands**.  This can include

* calculations
* opening files
* saving files
* renaming files
* etc.

This ability to repeat commands allows us to

* **save time** and
* **reduce errors**.

Let's look at **things we see in the zoo**.


```python
animals = ['lion', 'tiger', 'crocodile', 'vulture', 'hippo']
```


```python
for creature in animals:
    print(creature)
```

    lion
    tiger
    crocodile
    vulture
    hippo


**The idea:**

* Take the **collection** `animals`
    * **Assign** the first element to the variable `creature`, i.e. `creature = 'lion'`
        * **Execute** the **code block** using this value of `creature`
    * **Assign** the second element to the variable `creature`, i.e. `creature = 'tiger'`
        * **Execute** the code block using the new value of `creature`
    * ...
    * ...
    * **Assign** the last element to the variable `creature`, i.e. `creature = 'hippo'`
        * **Execute** the code block using the new value of `creature`
    * **Exit** the loop
* The variable `creature` **still exists**
    * It retains the **last assigned value**


```python
for creature in animals:
    pass # do nothing and skip to the next iteration

print('The loop variable is now: ' + creature)
```

    The loop variable is now: hippo


### Exercise

1. What happens if we don't include the `pass` statement?

2. Rewrite the loop so that the animals are separated by commas, not new lines (Hint: You can concatenate strings using a plus sign. For example, `print(string1 + string2)` outputs `'string1string2'`).

## Automating data processing using `for` Loops

**Task:** separate the `surveys.csv` data into **files by year**.

It's **25 years of data**, so that's a lot of files.  **Automate!**

### Prepare

Let's **create a directory** to store the data.

Use the **`os`** library to access **Unix shell** commands.


```python
import os

# like Unix mkdir
# comment out if directory already exists
#os.mkdir('data/yearly_files')
```

**Check** that it worked.


```python
# like Unix ls
os.listdir('data')
```




    ['out.csv',
     'plots.csv',
     'species.csv',
     'speciesSubset.csv',
     'survey2001.csv',
     'survey2002.csv',
     'surveys.csv',
     'yearly_files']



### Process

We want to...

* **load** the data into memory from the file,
* **select** a subset of the data using **criteria**,
* **write** the selected data to a CSV file.


```python
import pandas as pd
```

An example of the **basic steps** for **one year**.


```python
# Load the data into a DataFrame
#surveys_df = pd.read_csv('https://ndownloader.figshare.com/files/2292172')
surveys_df = pd.read_csv('data/surveys.csv')

# Select only data for 2002
surveys2002 = surveys_df[surveys_df.year == 2002]

# Write the new DataFrame to a csv file
surveys2002.to_csv('data/yearly_files/surveys2002.csv')
```

Our **job**: get the **last two lines** to repeat **for each year**.

**Advice:** build up the procedure **step by step**.

We could just **look** at the years contained in the data...


```python
#surveys_df['year']
surveys_df['year'][:5]
```




    0    1977
    1    1977
    2    1977
    3    1977
    4    1977
    Name: year, dtype: int64




```python
surveys_df['year'][-5:]
```




    35544    2002
    35545    2002
    35546    2002
    35547    2002
    35548    2002
    Name: year, dtype: int64



The years are 1977 through 2002.  We **could** create a list **by hand** containing those years.

But we want the process to be **automatic**.  We should get the years **directly from the data**.

Use the **`unique()`** method.


```python
surveys_df['year'].unique()
```




    array([1977, 1978, 1979, 1980, 1981, 1982, 1983, 1984, 1985, 1986, 1987,
           1988, 1989, 1990, 1991, 1992, 1993, 1994, 1995, 1996, 1997, 1998,
           1999, 2000, 2001, 2002])



That's **exactly** the list we want.  Stick it in the **loop**.

Now let's try to **get file names working**.


```python
for year in surveys_df['year'].unique():
    filename = 'data/yearly_files/surveys' + str(year) + '.csv'
    print(filename)
```

    data/yearly_files/surveys1977.csv
    data/yearly_files/surveys1978.csv
    data/yearly_files/surveys1979.csv
    data/yearly_files/surveys1980.csv
    data/yearly_files/surveys1981.csv
    data/yearly_files/surveys1982.csv
    data/yearly_files/surveys1983.csv
    data/yearly_files/surveys1984.csv
    data/yearly_files/surveys1985.csv
    data/yearly_files/surveys1986.csv
    data/yearly_files/surveys1987.csv
    data/yearly_files/surveys1988.csv
    data/yearly_files/surveys1989.csv
    data/yearly_files/surveys1990.csv
    data/yearly_files/surveys1991.csv
    data/yearly_files/surveys1992.csv
    data/yearly_files/surveys1993.csv
    data/yearly_files/surveys1994.csv
    data/yearly_files/surveys1995.csv
    data/yearly_files/surveys1996.csv
    data/yearly_files/surveys1997.csv
    data/yearly_files/surveys1998.csv
    data/yearly_files/surveys1999.csv
    data/yearly_files/surveys2000.csv
    data/yearly_files/surveys2001.csv
    data/yearly_files/surveys2002.csv


Now take a stab at the **whole loop**...


```python
# Load the data into a DataFrame
surveys_df = pd.read_csv('data/surveys.csv')

for year in surveys_df['year'].unique():

    # Select data for the year
    surveys_year = surveys_df[surveys_df.year == year]

    # Write the new DataFrame to a csv file
    filename = 'data/yearly_files/surveys' + str(year) + '.csv'
    surveys_year.to_csv(filename)
```

## Writing Unique File Names

Notice how we **generated** the **file names**...

* a string identifying **location**
    ```python
    'data/yearly_files/'
    ```
* a string giving a **grouping** for the **topic of investigation**
    ```python
    'surveys'
    ```
* a string highlighting the particular **processing applied** to get the output
    ```python
    str(year)
    ```
* a suffix denoting the **type of data**
    ```python
    '.csv'
    ```

That is,

> the **file name recapitulates** the **data processing**.

As an added bonus, we used the **`+` operator** for **string concatenation**.

### Exercise

1. Some of the surveys you saved are missing data (they have null values that show up as `NaN` - Not A Number - in the DataFrames and do not show up in the text files). Modify the for loop so that the entries with null values are not included in the yearly files.

2. What happens if there is no data for a year in the sequence (for example, imagine we had used 1976 as the start year in `range`)?

3. Let's say you only want to look at data from a given multiple of years. How would you modify your loop in order to generate a data file for only every 5th year, starting from 1977?

4. Instead of splitting out the data by years, a colleague wants to do analyses each species separately. How would you write a unique `csv` file for each species?

## Repackaging & Reusing Code: Functions

### Basic Idea

That's **not the last time** you're going to separate data into multiple files.

You **do not** want to **cut and paste** that code loop into other programs each time you want to use it.  That would be

* tedious
* error-prone.

**Functions** allow us to repackage code **for later use**.  Functions can

* take **arguments**,
* produce **output**,

but might **not** do **either**.

The **variables inside** a function **only live inside** the function.

If the **local** variable name  -- i.e. the name of the variable **inside** the function -- happens to be the **same** as a **variable outside**, the function **ignores the outside variable**.

More generally,

* **methods** are just functions, and
* **libraries** are just collections of functions.

**Format:**

* start with **`def`**
* then the function **name**
* **arguments**
* indented **code block**
* finally a **`return`** statement


```python
def this_is_the_function_name(input_argument1, input_argument2):

    # The body of the function is indented
    # This function prints the two arguments to screen
    print('The function arguments are:', input_argument1, input_argument2, '(this is done inside the function!)')

    # And returns their product
    return input_argument1 * input_argument2
```


```python
product_of_inputs = this_is_the_function_name(2,5)
```

    The function arguments are: 2 5 (this is done inside the function!)



```python
print('Their product is:', product_of_inputs, '(this is done outside the function!)')
```

    Their product is: 10 (this is done outside the function!)


#### Exercise

1. Change the values of the arguments in the function and check its output.
2. Try calling the function by giving it the wrong number of arguments (not 2) or not assigning the function call to a variable (no `product_of_inputs =`).
3. Declare a variable inside the function and test to see where it exists. (Hint: can you print it from outside the function?)
4. Explore what happens when a variable both inside and outside the function have the same name. What happens to the global variable when you change the value of the local variable?

### Breakdown of the Procedure & a First Function

What do we need to get done?

* go through each year,
* for each year,
    * get data,
    * write output.

Each of those **chunks** could be a **separate function**.

**Start simple:** let's focus on **outputting data for one year**.


```python
def one_year_csv_writer(this_year, all_data):
    """
    Writes a CSV file for data from a given year.

    this_year --- year for which data is extracted
    all_data --- DataFrame with multi-year data
    """

    # Select data for the year
    surveys_year = all_data[all_data.year == this_year]

    # Write the new DataFrame to a csv file
    filename = 'data/yearly_files/function_surveys' + str(this_year) + '.csv'
    surveys_year.to_csv(filename)
```

Note the **docstring**...


```python
one_year_csv_writer?
```


    [0;31mSignature:[0m [0mone_year_csv_writer[0m[0;34m([0m[0mthis_year[0m[0;34m,[0m [0mall_data[0m[0;34m)[0m[0;34m[0m[0m
    [0;31mDocstring:[0m
    Writes a CSV file for data from a given year.
    
    this_year --- year for which data is extracted
    all_data --- DataFrame with multi-year data
    [0;31mFile:[0m      ~/Public/Box Sync/BtPjkt/Computing/SciPy2016/SWC/python-ecology-lesson/<ipython-input-16-a70444c27d4a>
    [0;31mType:[0m      function



Now **try it** and **check the result**.


```python
one_year_csv_writer(2002,surveys_df)
```

### Repackage the Entire Loop

Now create a function that **encapsulates the entire loop**.

We'll use the function **`range(m, n)`**.  This essentially gives a **tuple** of **whole numbers** from `m` to `n`.

But it's like a Python **slice**: include the **first argument**, exclude the **last**.


```python
def yearly_data_csv_writer(start_year, end_year, all_data):
    """
    Writes separate csv files for each year of data.

    start_year --- the first year of data we want
    end_year --- the last year of data we want
    all_data --- DataFrame with multi-year data
    """

    # "end_year" is the last year of data we want to pull, so we loop to end_year+1
    for year in range(start_year, end_year+1):
        one_year_csv_writer(year, all_data)
```

This code is

* **reusable**,
* **more general** than our original loop:
    * we can extract a **subset of years** rather than all at once.


```python
# Load the data into a DataFrame
surveys_df = pd.read_csv('data/surveys.csv')

# Create csv files
yearly_data_csv_writer(1977, 2002, surveys_df)
```

#### Warning

> If you **edit** a function, **rerun the cell** containing the definition for changes to **take effect**.

#### Exercise

1. Add two arguments to the functions we wrote that take the path of the directory where the files will be written and the root of the file name. Create a new set of files with a different name in a different directory.
2. How could you use the function `yearly_data_csv_writer` to create a csv file for only one year? (Hint: think about the syntax for `range`.)
3. Make the functions return a list of the files they have written. There are many ways you can do this (and you should try them all!): either of the functions can print to screen, either can use a return statement to give back numbers or strings to their function call, or you can use some combination of the two. You could also try using the `os` library to list the contents of directories.
4. Explore what happens when variables are declared inside each of the functions versus in the main (non-indented) body of your code. What is the scope of the variables (where are they visible)? What happens when they have the same name but are given different values?

### Simplify the Interface

Let's make the functions **easier to use**.

Make the functions **default to full range of years** if not specified otherwise.

Use **keyword arguments**... arguments with an equal sign & default value.

#### Test the Basic Idea


```python
def yearly_data_arg_test(all_data, start_year = 1977, end_year = 2002):
    """
    Modified from yearly_data_csv_writer to test default argument values!
    
    start_year --- the first year of data we want --- default: 1977
    end_year --- the last year of data we want --- default: 2002
    all_data --- DataFrame with multi-year data
    """
    
    return start_year, end_year
```

Check.


```python
start,end = yearly_data_arg_test(surveys_df, 1988, 1993)
print('Both optional arguments:\t', start, end)
```

    Both optional arguments:	 1988 1993



```python
start,end = yearly_data_arg_test(surveys_df)
print('Default values:\t\t\t', start, end)
```

    Default values:			 1977 2002


#### More General Still

The function should **check the data** to get the **default values!**

Use **`None`** to signal that **values are missing**.


```python
def yearly_data_arg_test(all_data, start_year = None, end_year = None):
    """
    Modified from yearly_data_csv_writer to test default argument values!
    
    start_year --- the first year of data we want --- default: None - check all_data
    end_year --- the last year of data we want --- default: None - check all_data
    all_data --- DataFrame with multi-year data
    """
    
    if not start_year:
        start_year = min(all_data.year)
    if not end_year:
        end_year = max(all_data.year)
    
    return start_year, end_year
```

Check.


```python
start,end = yearly_data_arg_test(surveys_df, 1988, 1993)
print('Both optional arguments:\t', start, end)

start,end = yearly_data_arg_test(surveys_df)
print('Default values:\t\t\t', start, end)
```

    Both optional arguments:	 1988 1993
    Default values:			 1977 2002


##### Exercise

1. What type of object corresponds to a variable declared as `None`? (Hint: create a variable set to `None` and use the function `type()`.)

2. Compare the behavior of the function `yearly_data_arg_test` when the arguments have `None` as a default and when they do not have default values.

3. What happens if you only include a value for `start_year` in the function call? Can you write the function call with only a value for `end_year`? (Hint: think about how the function must be assigning values to each of the arguments - this is related to the need to put the arguments without default values before those with default values in the function definition!)

## `if` Conditions

**The Point:** only **execute** a code block if a **certain condition** is met.

**The Structure:**

* the **condition** needs to be something with a **Boolean value**, either `True` or `False`;
* the **code block** must be **indented**;
* you have **optional** follow-ups:
    * **else if:** if the previous condition isn't true, **try another condition**;
    * **else:** when **all else fails**, do this.

Example.


```python
a = 5

if (a < 0): # meets first condition?
    # if a IS less than zero
    print('a is a negative number')

elif (a > 0): # did not meet first condition. meets second condition?
    # if a ISN'T less than zero and IS more than zero
    print('a is a positive number')

else: # met neither condition
    # if a ISN'T less than zero and ISN'T more than zero
    print('a must be zero!')
```

    a is a positive number


**Examine** the code of our function:

```python
if not start_year:
    start_year = min(all_data.year)
if not end_year:
    end_year = max(all_data.year)
```

**The Logic:**

* `start_year`'s **default value** is `None`.
    * `None` has Boolean value **`False`**
    * `not None` must be **`True`**
        * So this code **executes** when **`start_year` is `None`**
* If `start_year`'s value is **some year**,
    * a year is a **positive number**,
        * non-zero numbers have **Boolean value `True`**,
        * zero has **Boolean value `False`**,
        * so a **year** is **`True`**;
    * then **`not start_year`** is **`False`**
        * so this code **does not** execute when **`start_year`** is some year.

**Note to self:** the lesson doesn't really explain here how we know what variables get evaluated as `True` and what variables don't.

## Keywords

When we **pass values** values to a function, they **get assigned** in the **order they are passed**.

In our function:

* the first value passed goes to **`all_data`**,
* the second value to **`start_year`**,
* the last value to **`end_year`**.

If we only give **two values**, then

* these are assigned to the **first two arguments**, and
* the **third argument** takes its **default value**.

If we only give **one value**, then

* this is assigned to the **first argument**, and
* the **second argument** takes its **default value**, and
* the **third argument** takes its **default value**.

If we want to **change this**, we can use **argument names** or **keywords** directly:

> tell the function **which argument** should get **which value**.


```python
start,end = yearly_data_arg_test(surveys_df)
print('Default values:\t\t\t', start, end)

start,end = yearly_data_arg_test(surveys_df, 1988, 1993)
print('No keywords:\t\t\t', start, end)

start,end = yearly_data_arg_test(surveys_df, start_year = 1988, end_year = 1993)
print('Both keywords, in order:\t', start, end)

start,end = yearly_data_arg_test(surveys_df, end_year = 1993, start_year = 1988)
print('Both keywords, flipped:\t\t', start, end)

start,end = yearly_data_arg_test(surveys_df, start_year = 1988)
print('One keyword, default end:\t', start, end)

start,end = yearly_data_arg_test(surveys_df, end_year = 1993)
print('One keyword, default start:\t', start, end)
```

    Default values:			 1977 2002
    No keywords:			 1988 1993
    Both keywords, in order:	 1988 1993
    Both keywords, flipped:		 1988 1993
    One keyword, default end:	 1988 2002
    One keyword, default start:	 1977 1993


### Exercise

1. Rewrite the `one_year_csv_writer` and `yearly_data_csv_writer` functions to have keyword arguments with default values.

2. Modify the functions so that they don't create yearly files if there is no data for a given year and display an alert to the user. (Hint: use conditional statements and `if` loops to do this. For an extra challenge, use `try` statements!)

3. The code below checks to see whether a directory exists and creates one if it doesn't. Add some code to your function that writes out the CSV files, to check for a directory to write to.
    ```python
    if 'dirNameHere' in os.listdir('.'):
        print('Processed directory exists')
    else:
        os.mkdir('dirNameHere')
        print('Processed directory created')
    ```

4. The code that you have written so far to loop through the years is good, however it is not necessarily reproducible with different datasets. For instance, what happens to the code if we have additional years of data in our CSV files? Using the tools that you learned in the previous activities, make a list of all years represented in the data. Then create a loop to process your data, that begins at the earliest year and ends at the latest year using that list.

    * HINT: you can create a loop with a list as follows:
        ```python
        for years in yearList:
        ```


```python

```
