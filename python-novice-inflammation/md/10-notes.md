
# Lesson 10 Notes: Command-Line Programs

These are some notes for [Software Carpentry](https://software-carpentry.org/)'s tutorial [*Programming with Python*](http://swcarpentry.github.io/python-novice-inflammation/).  The web page for this lesson can be found [here](http://swcarpentry.github.io/python-novice-inflammation/10-cmdline/).

## The Goal

> Interact with Python from the command line

## Think Ahead: How do you want things to work?

We want a program we can

* **call** from the command line;
* **feed** a file;
* **flag** to do various operations;
* **include** in a pipeline of data processing.

Something like the following (**NB:** we use **`$`** to represent the command prompt):

```bash
$ python code/readings_04.py --mean data/inflammation-01.csv
5.45
5.425
6.1
...
6.4
7.05
5.9
```

Here it's giving the **mean inflammation per patient**.

We might also want to **stitch it together** with other command line tools to look only at the **minimum of the first 4 lines**.

```bash
$ head -4 data/inflammation-01.csv | python code/readings_04.py --min
```

You've **gotta love piping**.

Or we could get the **maximum in several files** one after another:

```bash
$ python code/readings_04.py --max data/inflammation-*.csv
```

### Basic Functionality

Here are things we **want the program to do**:

* read a **file**, otherwise get data from **standard input**;
* read **several files** and report statistics for each **separately**;
* **select** the statistic using **flags** like `--max`, `--min`, `--mean`.

## Command-Line Arguments

In a text editor, create a file called `sys_version.py` and save the following text in the file.

```python
# inside sys_version.py
import sys
print('version is', sys.version)
```

`sys`, short for **system**, is a library that gives us access to our system.  In particular the function `.version` allows us to figure out the version of Python we're running.

Go to the command line, navigate to the **folder containing `sys_version.py`**, and type the following.

```bash
$ python sys_version.py
version is 3.4.3+ (default, Jul 28 2015, 13:17:50)
[GCC 4.9.3]
```

Create `argv_list.py` and save this in the file:

```python
# inside argv_list.py
import sys
print('sys.argv is', sys.argv)
```

**Translation:** `argv` stands for **argument values**, the parameters you feed to the function as arguments.

The output:

```bash
$ python argv_list.py
sys.argv is ['argv_list.py']
```

If we pass no parameters, then the list only contains the name of the program.  Otherwise we get

```bash
$ python argv_list.py first second third
sys.argv is ['argv_list.py', 'first', 'second', 'third']
```

## Creating Our Program

### Phase 1

Create a file `readings.py`:

```bash
$ touch readings_01.py
```

Then add some lines of code to it using the `cat` command (for reference [see here](http://www.linfo.org/cat.html) -- run the command on the file and then keep typing, press `[enter]` followed by `[ctrl]-d` when done):

```bash
$ cat >> readings_01.py
import sys
import numpy

def main():
    script = sys.argv[0]
    filename = sys.argv[1]
    data = numpy.loadtxt(filename, delimiter=',')
    for m in numpy.mean(data, axis=1):
        print(m)
```

We've called the "main" function `main()`, but you can really **call it whatever you want**.

Test it out:

```bash
$ python readings_01.py data/inflammation-01.csv
```

**Nothing happens!**  That's because we haven't **used** the function!

### Phase 2

Let's use the function.

Start with a new file.

```bash
$ touch readings_02.py
$ cat >> readings_02.py
import sys
import numpy

def main():
    script = sys.argv[0]
    filename = sys.argv[1]
    data = numpy.loadtxt(filename, delimiter=',')
    for m in numpy.mean(data, axis=1):
        print(m)

if __name__ == '__main__':
   main()
```

And run it:

```bash
$ python readings_02.py data/inflammation-01.csv
5.45
5.425
6.1
5.9
5.55
6.225
5.975
6.65
6.625
6.525
6.775
5.8
6.225
5.75
5.225
6.3
6.55
5.7
5.85
6.55
5.775
5.825
6.175
6.1
5.8
6.425
6.05
6.025
6.175
6.55
6.175
6.35
6.725
6.125
7.075
5.725
5.925
6.15
6.075
5.75
5.975
5.725
6.3
5.9
6.75
5.925
7.225
6.15
5.95
6.275
5.7
6.1
6.825
5.975
6.725
5.7
6.25
6.4
7.05
5.9
```

#### Note: the Magic `__name__ == __main__` Incantation

Two issues are at play here:

* when you **import** a file, its name is stored in `__name__`
    * so `import readings.py` sets `__name__ = readings`;
* when you **run** a script in `bash`, then `__name__` is sent to `__main__`
    * so the incantation says, "If the script is run **as a script**, then execute...".

## Handling Multiple Files

### Start Small

First start with smaller files, where you can check things by hand if necessary.

We have some files with just a couple lines of 3-days-worth of data.

```bash
$ ls data/small-*.csv
data/small-01.csv  data/small-02.csv  data/small-03.csv
```

Check the contents:

```bash
$ cat data/small-01.csv
0,0,1
0,1,2
```

Try the program:

```bash
$ python readings_02.py data/small-01.csv
0.333333333333
1.0
```

You can **check the calculation yourself!**  So ***now*** we know the program works as expected.

### Figure Out the Logic

We need to

* process files **one at a time**, independently
    * so we need a loop that executes **once per file**;
* the files are **arguments**
    * but `sys.argv[0]` contains the script name, so we need to **exclude that**;
* we don't know **how many files** beforehand
    * so we need to handle an indeterminate number of files.

Solution:

> slice the array starting at index 1: `sys.argv[1:]`.

Put that all together:

```bash
$ touch readings_03.py
$ cat >> readings_03.py
import sys
import numpy

def main():
    script = sys.argv[0]
    for filename in sys.argv[1:]:
        data = numpy.loadtxt(filename, delimiter=',')
        for m in numpy.mean(data, axis=1):
            print(m)

if __name__ == '__main__':
   main()
```

And run it:

```bash
$ python readings_03.py data/small-01.csv data/small-02.csv
0.333333333333
1.0
13.6666666667
11.0
```

## Handling Command-Line Flags

We want to change behavior based on the flags `--max`, `--min`, and `--mean`.

We could do this with simple `if`-statements like so:

```bash
$ touch readings_04.py
$ cat >> readings_04.py
import sys
import numpy

def main():
    script = sys.argv[0]
    action = sys.argv[1]
    filenames = sys.argv[2:]

    for f in filenames:
        data = numpy.loadtxt(f, delimiter=',')

        if action == '--min':
            values = numpy.min(data, axis=1)
        elif action == '--mean':
            values = numpy.mean(data, axis=1)
        elif action == '--max':
            values = numpy.max(data, axis=1)

        for m in values:
            print(m)

if __name__ == '__main__':
   main()
```

Test it out:

```bash
$ python readings_04.py --min data/small-01.csv data/small-02.csv
0.0
0.0
9.0
5.0
```

That works, but it has some **serious flaws**:

* `main()` contains a lot of logic, and the basic **idea** of the program isn't clear;
* the program will **run** even if we **use it wrong**
    * running with **only a flag** or **only a filename** will not throw an exception;
* the program **doesn't check the flags** to see if it can handle the action.

### Improved Version

The new version will

* **`assert` the flags** only have allowed values;
* handle **processing based on flags** in a separate function.

Like so:

```bash
$ touch readings_05.py
$ cat >> readings_05.py
import sys
import numpy

def main():
    script = sys.argv[0]
    action = sys.argv[1]
    filenames = sys.argv[2:]
    assert action in ['--min', '--mean', '--max'], \
           'Action is not one of --min, --mean, or --max: ' + action
    for f in filenames:
        process(f, action)

def process(filename, action):
    data = numpy.loadtxt(filename, delimiter=',')

    if action == '--min':
        values = numpy.min(data, axis=1)
    elif action == '--mean':
        values = numpy.mean(data, axis=1)
    elif action == '--max':
        values = numpy.max(data, axis=1)

    for m in values:
        print(m)

if __name__ == '__main__':
   main()
```

Slightly longer, **a lot clearer**.

## Handling Standard Input

### A Toy Script

Let's first just figure out how to deal with standard input.

Create a file `count_stdin.py` that counts the number of lines read into standard input.

```bash
$ touch count_stdin.py
$ cat >> count_stdin.py
import sys

count = 0
for line in sys.stdin:
    count += 1

print(count, 'lines in standard input')
```

**The Magic:** `sys.stdin` allows us to connect to standard input **as if we had opened a file.**

Try it.

But remember: **we *redirect* standard input with `<`.**

```bash
$ python count_stdin.py < data/small-01.csv
2 lines in standard input
```

**Warning:** if you forget the `<`, then there's no standard input, and your program will **wait forever.**

### Final Version

We modify the program so that

* **if** there are no filenames, it reads from **standard input**;
* **else** it processes the files normally.

**Useful tidbit:** `numpy.loadtxt` handles files and standard input in the same way, so **it doesn't care which we feed it.**

The new script:

```bash
$ touch readings_06.py
$ cat >> readings_06.py
import sys
import numpy

def main():
    script = sys.argv[0]
    action = sys.argv[1]
    filenames = sys.argv[2:]
    assert action in ['--min', '--mean', '--max'], \
           'Action is not one of --min, --mean, or --max: ' + action
    if len(filenames) == 0:
        process(sys.stdin, action)
    else:
        for f in filenames:
            process(f, action)

def process(filename, action):
    data = numpy.loadtxt(filename, delimiter=',')

    if action == '--min':
        values = numpy.min(data, axis=1)
    elif action == '--mean':
        values = numpy.mean(data, axis=1)
    elif action == '--max':
        values = numpy.max(data, axis=1)

    for m in values:
        print(m)

if __name__ == '__main__':
   main()
```

Try it:

```bash
$ python readings_06.py --mean < data/small-01.csv
0.333333333333
1.0
```

Nice.  **Done.**


```python

```
