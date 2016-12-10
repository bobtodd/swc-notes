
# Lesson 8: Accessing SQLite Databases Using Python & Pandas

These are some notes for [Data Carpentry](http://www.datacarpentry.org)'s tutorial [*Data Analysis and Visualization in Python*](http://www.datacarpentry.org/python-ecology-lesson/).  The web page for this lesson can be found [here](http://www.datacarpentry.org/python-ecology-lesson/08-working-with-sql).

## Goal

> Interact with a SQL database from Python

## The Idea

So far we've imported an **entire data table as a whole**.  We **store** it and **manipulate** it in memory **as a whole**.

For **big databases**, that can be **prohibitive**.

If the data is in a **SQL database**, you can query to receive only the **data you want**.

## The `sqlite3` Module

The [`sqlite3`](https://docs.python.org/3/library/sqlite3.html) module allows Python to **interact with** a SQLite database.


```python
import sqlite3

# Create a SQL connection to our SQLite database
con = sqlite3.connect("data/portal_mammals.sqlite")

cur = con.cursor()

# the result of a "cursor.execute" can be iterated over by row
for row in cur.execute('SELECT * FROM species;'):
    print(row)

#Be sure to close the connection.
con.close()
```

    ('AB', 'Amphispiza', 'bilineata', 'Bird')
    ('AH', 'Ammospermophilus', 'harrisi', 'Rodent-not censused')
    ('AS', 'Ammodramus', 'savannarum', 'Bird')
    ('BA', 'Baiomys', 'taylori', 'Rodent')
    ('CB', 'Campylorhynchus', 'brunneicapillus', 'Bird')
    ('CM', 'Calamospiza', 'melanocorys', 'Bird')
    ('CQ', 'Callipepla', 'squamata', 'Bird')
    ('CS', 'Crotalus', 'scutalatus', 'Reptile')
    ('CT', 'Cnemidophorus', 'tigris', 'Reptile')
    ('CU', 'Cnemidophorus', 'uniparens', 'Reptile')
    ('CV', 'Crotalus', 'viridis', 'Reptile')
    ('DM', 'Dipodomys', 'merriami', 'Rodent')
    ('DO', 'Dipodomys', 'ordii', 'Rodent')
    ('DS', 'Dipodomys', 'spectabilis', 'Rodent')
    ('DX', 'Dipodomys', 'sp.', 'Rodent')
    ('EO', 'Eumeces', 'obsoletus', 'Reptile')
    ('GS', 'Gambelia', 'silus', 'Reptile')
    ('NA', 'Neotoma', 'albigula', 'Rodent')
    ('NX', 'Neotoma', 'sp.', 'Rodent')
    ('OL', 'Onychomys', 'leucogaster', 'Rodent')
    ('OT', 'Onychomys', 'torridus', 'Rodent')
    ('OX', 'Onychomys', 'sp.', 'Rodent')
    ('PB', 'Chaetodipus', 'baileyi', 'Rodent')
    ('PC', 'Pipilo', 'chlorurus', 'Bird')
    ('PE', 'Peromyscus', 'eremicus', 'Rodent')
    ('PF', 'Perognathus', 'flavus', 'Rodent')
    ('PG', 'Pooecetes', 'gramineus', 'Bird')
    ('PH', 'Perognathus', 'hispidus', 'Rodent')
    ('PI', 'Chaetodipus', 'intermedius', 'Rodent')
    ('PL', 'Peromyscus', 'leucopus', 'Rodent')
    ('PM', 'Peromyscus', 'maniculatus', 'Rodent')
    ('PP', 'Chaetodipus', 'penicillatus', 'Rodent')
    ('PU', 'Pipilo', 'fuscus', 'Bird')
    ('PX', 'Chaetodipus', 'sp.', 'Rodent')
    ('RF', 'Reithrodontomys', 'fulvescens', 'Rodent')
    ('RM', 'Reithrodontomys', 'megalotis', 'Rodent')
    ('RO', 'Reithrodontomys', 'montanus', 'Rodent')
    ('RX', 'Reithrodontomys', 'sp.', 'Rodent')
    ('SA', 'Sylvilagus', 'audubonii', 'Rabbit')
    ('SB', 'Spizella', 'breweri', 'Bird')
    ('SC', 'Sceloporus', 'clarki', 'Reptile')
    ('SF', 'Sigmodon', 'fulviventer', 'Rodent')
    ('SH', 'Sigmodon', 'hispidus', 'Rodent')
    ('SO', 'Sigmodon', 'ochrognathus', 'Rodent')
    ('SS', 'Spermophilus', 'spilosoma', 'Rodent-not censused')
    ('ST', 'Spermophilus', 'tereticaudus', 'Rodent-not censused')
    ('SU', 'Sceloporus', 'undulatus', 'Reptile')
    ('SX', 'Sigmodon', 'sp.', 'Rodent')
    ('UL', 'Lizard', 'sp.', 'Reptile')
    ('UP', 'Pipilo', 'sp.', 'Bird')
    ('UR', 'Rodent', 'sp.', 'Rodent')
    ('US', 'Sparrow', 'sp.', 'Bird')
    ('XX', None, None, 'Zero Trapping Success')
    ('ZL', 'Zonotrichia', 'leucophrys', 'Bird')
    ('ZM', 'Zenaida', 'macroura', 'Bird')


## Interface between SQLite & Pandas

We can read a SQLite query into a Pandas DataFrame.


```python
import pandas as pd
import sqlite3

# Read sqlite query results into a pandas DataFrame
con = sqlite3.connect("data/portal_mammals.sqlite")
df = pd.read_sql_query("SELECT * from surveys", con)

# verify that result of SQL query is stored in the dataframe
print(df.head())

con.close()
```

       record_id  month  day  year  plot species sex  wgt
    0          1      7   16  1977     2      NA   M  NaN
    1          2      7   16  1977     3      NA   M  NaN
    2          3      7   16  1977     2      DM   F  NaN
    3          4      7   16  1977     7      DM   M  NaN
    4          5      7   16  1977     3      DM   M  NaN


## Data Storage: CSV vs. SQLite

Read/write times can be **quicker** when accessing **SQLite** than when accessing CSV.

The time difference generally **increases with the size** of the database.

See [these benchmarks](http://sebastianraschka.com/Articles/2013_sqlite_database.html#results-and-conclusions).

### Exercise

1. Create a query that contains survey data collected between 1998 - 2001 for observations of sex "male" or "female" that includes observation's genus and species and plot type for the sample. How many records are returned?

2. Create a dataframe that contains the total number of observations (count) made for all years, and sum of observation weights for each plot, ordered by plot ID.


```python

```
